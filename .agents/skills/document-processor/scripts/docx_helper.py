#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Word (.docx) Helper Script for Antigravity
Provides utilities for creating, modifying, and converting Word documents.
"""

import sys
import os
import io
import argparse
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

# Force UTF-8
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


def set_cell_background(cell, fill_hex):
    """Set background color of a table cell (e.g. '0F52BA')"""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex.replace('#', ''))
    tcPr.append(shd)


def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Set cell padding in twips (1 pt = 20 twips)"""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)


def create_document(output_path: str, title: str, subtitle: str = None, author: str = None):
    doc = Document()
    
    # Page setup (A4 standard)
    section = doc.sections[0]
    section.page_width = Inches(8.27)
    section.page_height = Inches(11.69)
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)
    
    # Title
    t_para = doc.add_paragraph()
    t_run = t_para.add_run(title)
    t_run.font.name = 'Arial'
    t_run.font.size = Pt(24)
    t_run.font.bold = True
    t_run.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
    t_para.paragraph_format.space_after = Pt(6)
    
    if subtitle:
        s_para = doc.add_paragraph()
        s_run = s_para.add_run(subtitle)
        s_run.font.name = 'Arial'
        s_run.font.size = Pt(13)
        s_run.font.italic = True
        s_run.font.color.rgb = RGBColor(0x64, 0x74, 0x8B)
        s_para.paragraph_format.space_after = Pt(18)
        
    doc.save(output_path)
    print(f"Created Word document: {output_path}")
    return doc


def add_table_styled(doc, headers: list, rows: list, header_bg='1E293B', header_color='FFFFFF'):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = 'Table Grid'
    
    # Format header
    hdr_cells = table.rows[0].cells
    for i, h_text in enumerate(headers):
        hdr_cells[i].text = str(h_text)
        set_cell_background(hdr_cells[i], header_bg)
        set_cell_margins(hdr_cells[i], top=120, bottom=120, left=150, right=150)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.bold = True
            r.font.color.rgb = RGBColor.from_string(header_color.replace('#', ''))
            
    # Format data rows
    for r_idx, row_data in enumerate(rows):
        row_cells = table.rows[r_idx + 1].cells
        bg_color = 'F8FAFC' if r_idx % 2 == 1 else 'FFFFFF'
        for c_idx, val in enumerate(row_data):
            if c_idx < len(row_cells):
                row_cells[c_idx].text = str(val)
                set_cell_background(row_cells[c_idx], bg_color)
                set_cell_margins(row_cells[c_idx], top=100, bottom=100, left=150, right=150)
    return table


def replace_text(file_path: str, find_str: str, replace_str: str, output_path: str = None):
    doc = Document(file_path)
    count = 0
    
    # Replace in paragraphs
    for p in doc.paragraphs:
        if find_str in p.text:
            p.text = p.text.replace(find_str, replace_str)
            count += 1
            
    # Replace in tables
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    if find_str in p.text:
                        p.text = p.text.replace(find_str, replace_str)
                        count += 1
                        
    out_file = output_path or file_path
    doc.save(out_file)
    print(f"Replaced {count} occurrence(s). Saved to {out_file}")


def main():
    parser = argparse.ArgumentParser(description="Word (.docx) Helper")
    subparsers = parser.add_subparsers(dest="action", required=True)
    
    # Create command
    create_p = subparsers.add_parser("create", help="Create a new document")
    create_p.add_argument("output", help="Output file path")
    create_p.add_argument("--title", required=True, help="Document title")
    create_p.add_argument("--subtitle", help="Document subtitle")
    
    # Replace command
    replace_p = subparsers.add_parser("replace", help="Find and replace text")
    replace_p.add_argument("file", help="Target document")
    replace_p.add_argument("--find", required=True, help="Text to find")
    replace_p.add_argument("--replace", required=True, help="Replacement text")
    replace_p.add_argument("--output", help="Output path (default: overwrite)")
    
    args = parser.parse_args()
    
    if args.action == "create":
        create_document(args.output, args.title, args.subtitle)
    elif args.action == "replace":
        replace_text(args.file, args.find, args.replace, args.output)


if __name__ == "__main__":
    main()
