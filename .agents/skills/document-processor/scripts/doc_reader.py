#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Universal Document Reader & Extractor for Antigravity
Supports: .docx, .pptx, .xlsx, .pdf, .csv
Outputs: Markdown (default), JSON, Plain Text
"""

import sys
import os
import io
import json
import argparse
from pathlib import Path

# Force UTF-8 on Windows stdout/stderr
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


def read_docx(file_path: str) -> dict:
    import docx
    doc = docx.Document(file_path)
    content = []
    
    for element in doc.element.body:
        # Check paragraph
        if element.tag.endswith('p'):
            p = docx.text.paragraph.Paragraph(element, doc)
            text = p.text.strip()
            if not text:
                continue
            style_name = p.style.name.lower() if p.style else ""
            if "heading 1" in style_name:
                content.append({"type": "heading", "level": 1, "text": text})
            elif "heading 2" in style_name:
                content.append({"type": "heading", "level": 2, "text": text})
            elif "heading 3" in style_name:
                content.append({"type": "heading", "level": 3, "text": text})
            elif "list" in style_name or "bullet" in style_name:
                content.append({"type": "bullet", "text": text})
            else:
                content.append({"type": "paragraph", "text": text})
        # Check table
        elif element.tag.endswith('tbl'):
            table = docx.table.Table(element, doc)
            table_data = []
            for row in table.rows:
                row_cells = [cell.text.strip().replace('\n', ' ') for cell in row.cells]
                table_data.append(row_cells)
            if table_data:
                content.append({"type": "table", "data": table_data})
                
    return {"file_type": "docx", "file_name": os.path.basename(file_path), "content": content}


def read_pptx(file_path: str) -> dict:
    from pptx import Presentation
    prs = Presentation(file_path)
    slides_data = []
    
    for idx, slide in enumerate(prs.slides, start=1):
        slide_title = ""
        items = []
        notes = ""
        
        # Check for title shape
        if slide.shapes.title and slide.shapes.title.text:
            slide_title = slide.shapes.title.text.strip()
            
        for shape in slide.shapes:
            if shape == slide.shapes.title:
                continue
            if shape.has_text_frame:
                for paragraph in shape.text_frame.paragraphs:
                    text = paragraph.text.strip()
                    if text:
                        items.append({"type": "text", "level": paragraph.level, "text": text})
            elif shape.has_table:
                table_data = []
                for row in shape.table.rows:
                    row_cells = [cell.text.strip().replace('\n', ' ') for cell in row.cells]
                    table_data.append(row_cells)
                if table_data:
                    items.append({"type": "table", "data": table_data})
                    
        if slide.has_notes_slide and slide.notes_slide.notes_text_frame:
            notes = slide.notes_slide.notes_text_frame.text.strip()
            
        slides_data.append({
            "slide_number": idx,
            "title": slide_title,
            "items": items,
            "notes": notes
        })
        
    return {
        "file_type": "pptx",
        "file_name": os.path.basename(file_path),
        "total_slides": len(slides_data),
        "slides": slides_data
    }


def read_xlsx(file_path: str, target_sheet: str = None, max_rows: int = 100) -> dict:
    import openpyxl
    wb = openpyxl.load_workbook(file_path, data_only=True)
    sheets_info = wb.sheetnames
    
    sheets_data = {}
    sheets_to_process = [target_sheet] if (target_sheet and target_sheet in sheets_info) else sheets_info
    
    for sheet_name in sheets_to_process:
        ws = wb[sheet_name]
        rows = []
        for row_idx, row in enumerate(ws.iter_rows(values_only=True), start=1):
            if row_idx > max_rows:
                break
            # check if row is empty
            if all(cell is None or str(cell).strip() == "" for cell in row):
                continue
            cleaned_row = [str(cell) if cell is not None else "" for cell in row]
            rows.append(cleaned_row)
        sheets_data[sheet_name] = rows
        
    return {
        "file_type": "xlsx",
        "file_name": os.path.basename(file_path),
        "sheets": sheets_info,
        "data": sheets_data
    }


def read_pdf(file_path: str, page_range: str = None) -> dict:
    # Try pdfplumber for best layout/table extraction, fallback to pypdf or pymupdf
    pages_data = []
    try:
        import pdfplumber
        with pdfplumber.open(file_path) as pdf:
            total_pages = len(pdf.pages)
            start_p, end_p = 1, total_pages
            if page_range:
                parts = page_range.split("-")
                start_p = int(parts[0])
                end_p = int(parts[1]) if len(parts) > 1 else start_p
                start_p = max(1, min(start_p, total_pages))
                end_p = max(start_p, min(end_p, total_pages))
                
            for p_num in range(start_p, end_p + 1):
                page = pdf.pages[p_num - 1]
                text = page.extract_text() or ""
                tables = page.extract_tables() or []
                pages_data.append({
                    "page_number": p_num,
                    "text": text.strip(),
                    "tables": tables
                })
    except ImportError:
        import pypdf
        reader = pypdf.PdfReader(file_path)
        total_pages = len(reader.pages)
        for idx, page in enumerate(reader.pages, start=1):
            pages_data.append({
                "page_number": idx,
                "text": (page.extract_text() or "").strip(),
                "tables": []
            })
            
    return {
        "file_type": "pdf",
        "file_name": os.path.basename(file_path),
        "total_pages": len(pages_data),
        "pages": pages_data
    }


def format_table_markdown(table_data: list) -> str:
    if not table_data:
        return ""
    col_count = max(len(row) for row in table_data)
    # Normalize rows
    norm_rows = [row + [""] * (col_count - len(row)) for row in table_data]
    
    header = norm_rows[0]
    separator = ["---"] * col_count
    
    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(separator) + " |"
    ]
    for row in norm_rows[1:]:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def to_markdown(doc_dict: dict) -> str:
    ftype = doc_dict.get("file_type")
    fname = doc_dict.get("file_name", "Document")
    md = [f"# {fname}\n"]
    
    if ftype == "docx":
        for item in doc_dict.get("content", []):
            itype = item.get("type")
            if itype == "heading":
                hashes = "#" * (item.get("level", 1) + 1)
                md.append(f"{hashes} {item.get('text')}\n")
            elif itype == "bullet":
                md.append(f"- {item.get('text')}")
            elif itype == "paragraph":
                md.append(f"{item.get('text')}\n")
            elif itype == "table":
                md.append(format_table_markdown(item.get("data", [])) + "\n")
                
    elif ftype == "pptx":
        for slide in doc_dict.get("slides", []):
            s_num = slide.get("slide_number")
            s_title = slide.get("title") or f"Slide {s_num}"
            md.append(f"## Slide {s_num}: {s_title}\n")
            for item in slide.get("items", []):
                if item.get("type") == "text":
                    indent = "  " * item.get("level", 0)
                    md.append(f"{indent}- {item.get('text')}")
                elif item.get("type") == "table":
                    md.append(format_table_markdown(item.get("data", [])) + "\n")
            if slide.get("notes"):
                md.append(f"\n> **Speaker Notes:** {slide.get('notes')}\n")
            md.append("\n---\n")
            
    elif ftype == "xlsx":
        md.append(f"**Sheets Available:** {', '.join(doc_dict.get('sheets', []))}\n")
        for sheet_name, rows in doc_dict.get("data", {}).items():
            md.append(f"### Sheet: {sheet_name}\n")
            if rows:
                md.append(format_table_markdown(rows) + "\n")
            else:
                md.append("*[Empty Sheet]*\n")
                
    elif ftype == "pdf":
        for page in doc_dict.get("pages", []):
            p_num = page.get("page_number")
            md.append(f"## Page {p_num}\n")
            if page.get("text"):
                md.append(page.get("text") + "\n")
            for tbl in page.get("tables", []):
                if tbl:
                    cleaned_tbl = [[str(c or '').strip().replace('\n', ' ') for c in r] for r in tbl]
                    md.append(format_table_markdown(cleaned_tbl) + "\n")
            md.append("\n---\n")
            
    return "\n".join(md)


def main():
    parser = argparse.ArgumentParser(description="Universal Document Reader for Antigravity")
    parser.add_argument("file_path", help="Path to document file (.docx, .pptx, .xlsx, .pdf)")
    parser.add_argument("--format", choices=["markdown", "json", "text"], default="markdown", help="Output format")
    parser.add_argument("--pages", help="Page range for PDF (e.g. 1-5)")
    parser.add_argument("--sheet", help="Target sheet name for Excel")
    parser.add_argument("--max-rows", type=int, default=100, help="Max rows per sheet for Excel")
    parser.add_argument("--output", help="Save output to file instead of printing")
    
    args = parser.parse_args()
    file_path = os.path.abspath(args.file_path)
    
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(1)
        
    ext = Path(file_path).suffix.lower()
    
    if ext == ".docx":
        data = read_docx(file_path)
    elif ext == ".pptx":
        data = read_pptx(file_path)
    elif ext in [".xlsx", ".xls"]:
        data = read_xlsx(file_path, target_sheet=args.sheet, max_rows=args.max_rows)
    elif ext == ".pdf":
        data = read_pdf(file_path, page_range=args.pages)
    else:
        print(f"Unsupported file format: {ext}", file=sys.stderr)
        sys.exit(1)
        
    if args.format == "json":
        output_str = json.dumps(data, indent=2, ensure_ascii=False)
    else:
        output_str = to_markdown(data)
        
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output_str)
        print(f"Content saved to: {args.output}")
    else:
        print(output_str)


if __name__ == "__main__":
    main()
