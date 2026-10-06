#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Model Context Protocol (MCP) Document Server for Antigravity
Provides fast native tools for reading, analyzing, and generating .docx, .pptx, .xlsx, .pdf files.
"""

import sys
import os
import io
import json
from pathlib import Path
from mcp.server.fastmcp import FastMCP

# Ensure UTF-8 streams
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

mcp = FastMCP("document-tools")


@mcp.tool()
def read_document(file_path: str, format: str = "markdown", sheet: str = None, pages: str = None) -> str:
    """
    Reads any Word (.docx), PowerPoint (.pptx), Excel (.xlsx/.xls), or PDF (.pdf) file and returns clean Markdown.
    
    Args:
        file_path: Absolute or relative path to the document file.
        format: Output format ('markdown' or 'text').
        sheet: Optional target sheet name for Excel spreadsheets.
        pages: Optional page range for PDF (e.g. '1-5').
    """
    file_path = os.path.abspath(file_path)
    if not os.path.exists(file_path):
        return f"Error: File not found: {file_path}"
        
    ext = Path(file_path).suffix.lower()
    
    # 1. Word DOCX
    if ext == ".docx":
        import docx
        doc = docx.Document(file_path)
        lines = [f"# {os.path.basename(file_path)}\n"]
        for element in doc.element.body:
            if element.tag.endswith('p'):
                p = docx.text.paragraph.Paragraph(element, doc)
                txt = p.text.strip()
                if not txt:
                    continue
                style_name = p.style.name.lower() if p.style else ""
                if "heading 1" in style_name:
                    lines.append(f"## {txt}\n")
                elif "heading 2" in style_name:
                    lines.append(f"### {txt}\n")
                elif "heading 3" in style_name:
                    lines.append(f"#### {txt}\n")
                elif "list" in style_name or "bullet" in style_name:
                    lines.append(f"- {txt}")
                else:
                    lines.append(f"{txt}\n")
            elif element.tag.endswith('tbl'):
                table = docx.table.Table(element, doc)
                rows = [[c.text.strip().replace('\n', ' ') for c in r.cells] for r in table.rows]
                if rows:
                    cols = max(len(r) for r in rows)
                    norm = [r + [""] * (cols - len(r)) for r in rows]
                    lines.append("| " + " | ".join(norm[0]) + " |")
                    lines.append("| " + " | ".join(["---"] * cols) + " |")
                    for r in norm[1:]:
                        lines.append("| " + " | ".join(r) + " |")
                    lines.append("")
        return "\n".join(lines)

    # 2. PowerPoint PPTX
    elif ext == ".pptx":
        from pptx import Presentation
        prs = Presentation(file_path)
        lines = [f"# {os.path.basename(file_path)}\n"]
        for idx, slide in enumerate(prs.slides, start=1):
            title = slide.shapes.title.text.strip() if (slide.shapes.title and slide.shapes.title.text) else f"Slide {idx}"
            lines.append(f"## Slide {idx}: {title}\n")
            for shape in slide.shapes:
                if shape == slide.shapes.title:
                    continue
                if shape.has_text_frame:
                    for p in shape.text_frame.paragraphs:
                        if p.text.strip():
                            indent = "  " * p.level
                            lines.append(f"{indent}- {p.text.strip()}")
                elif shape.has_table:
                    rows = [[c.text.strip().replace('\n', ' ') for c in r.cells] for r in shape.table.rows]
                    if rows:
                        cols = max(len(r) for r in rows)
                        norm = [r + [""] * (cols - len(r)) for r in rows]
                        lines.append("| " + " | ".join(norm[0]) + " |")
                        lines.append("| " + " | ".join(["---"] * cols) + " |")
                        for r in norm[1:]:
                            lines.append("| " + " | ".join(r) + " |")
            if slide.has_notes_slide and slide.notes_slide.notes_text_frame:
                n_text = slide.notes_slide.notes_text_frame.text.strip()
                if n_text:
                    lines.append(f"\n> **Speaker Notes:** {n_text}")
            lines.append("\n---\n")
        return "\n".join(lines)

    # 3. Excel XLSX
    elif ext in [".xlsx", ".xls"]:
        import openpyxl
        wb = openpyxl.load_workbook(file_path, data_only=True)
        sheets = wb.sheetnames
        lines = [f"# {os.path.basename(file_path)}\n", f"**Sheets Available:** {', '.join(sheets)}\n"]
        target_sheets = [sheet] if (sheet and sheet in sheets) else sheets
        for s_name in target_sheets:
            ws = wb[s_name]
            lines.append(f"### Sheet: {s_name}\n")
            rows = []
            for row in ws.iter_rows(values_only=True):
                if all(c is None or str(c).strip() == "" for c in row):
                    continue
                rows.append([str(c) if c is not None else "" for c in row])
            if rows:
                cols = max(len(r) for r in rows)
                norm = [r + [""] * (cols - len(r)) for r in rows]
                lines.append("| " + " | ".join(norm[0]) + " |")
                lines.append("| " + " | ".join(["---"] * cols) + " |")
                for r in norm[1:]:
                    lines.append("| " + " | ".join(r) + " |")
            lines.append("")
        return "\n".join(lines)

    # 4. PDF
    elif ext == ".pdf":
        import pdfplumber
        lines = [f"# {os.path.basename(file_path)}\n"]
        with pdfplumber.open(file_path) as pdf:
            total_pages = len(pdf.pages)
            start_p, end_p = 1, total_pages
            if pages:
                parts = pages.split("-")
                start_p = max(1, min(int(parts[0]), total_pages))
                end_p = max(start_p, min(int(parts[1]) if len(parts) > 1 else start_p, total_pages))
            for p_num in range(start_p, end_p + 1):
                page = pdf.pages[p_num - 1]
                lines.append(f"## Page {p_num}\n")
                txt = page.extract_text()
                if txt:
                    lines.append(txt.strip() + "\n")
                tables = page.extract_tables() or []
                for tbl in tables:
                    if tbl:
                        cleaned = [[str(c or '').strip().replace('\n', ' ') for c in r] for r in tbl]
                        cols = max(len(r) for r in cleaned)
                        norm = [r + [""] * (cols - len(r)) for r in cleaned]
                        lines.append("| " + " | ".join(norm[0]) + " |")
                        lines.append("| " + " | ".join(["---"] * cols) + " |")
                        for r in norm[1:]:
                            lines.append("| " + " | ".join(r) + " |")
                lines.append("\n---\n")
        return "\n".join(lines)

    # Fallback to MarkItDown
    try:
        from markitdown import MarkItDown
        md = MarkItDown()
        result = md.convert(file_path)
        return result.text_content
    except Exception as e:
        return f"Error reading document: {e}"


@mcp.tool()
def inspect_document(file_path: str) -> str:
    """
    Quickly returns metadata and structure outline for a document without extracting entire contents.
    """
    file_path = os.path.abspath(file_path)
    if not os.path.exists(file_path):
        return f"Error: File not found: {file_path}"
        
    ext = Path(file_path).suffix.lower()
    res = {
        "file_name": os.path.basename(file_path),
        "file_path": file_path,
        "file_size_bytes": os.path.getsize(file_path),
        "extension": ext
    }
    
    if ext == ".docx":
        import docx
        doc = docx.Document(file_path)
        res["paragraph_count"] = len(doc.paragraphs)
        res["table_count"] = len(doc.tables)
        res["headings"] = [p.text for p in doc.paragraphs if "heading" in (p.style.name.lower() if p.style else "")]
    elif ext == ".pptx":
        from pptx import Presentation
        prs = Presentation(file_path)
        res["slide_count"] = len(prs.slides)
        res["slide_titles"] = [s.shapes.title.text.strip() if (s.shapes.title and s.shapes.title.text) else f"Slide {i}" for i, s in enumerate(prs.slides, 1)]
    elif ext in [".xlsx", ".xls"]:
        import openpyxl
        wb = openpyxl.load_workbook(file_path, read_only=True)
        res["sheet_names"] = wb.sheetnames
    elif ext == ".pdf":
        import pypdf
        reader = pypdf.PdfReader(file_path)
        res["page_count"] = len(reader.pages)
        res["is_encrypted"] = reader.is_encrypted
        
    return json.dumps(res, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    mcp.run()
