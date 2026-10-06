#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Excel (.xlsx) Helper Script for Antigravity
Provides utilities for creating professional spreadsheets, styling tables, formatting numbers, and managing multi-sheet workbooks.
"""

import sys
import os
import io
import json
import argparse
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Force UTF-8
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


def style_worksheet(ws, title="Sheet", header_color="1E293B", text_color="FFFFFF"):
    """Applies clean modern styling, borders, and auto column widths to an openpyxl worksheet."""
    header_fill = PatternFill(start_color=header_color, end_color=header_color, fill_type="solid")
    header_font = Font(name="Segoe UI", size=11, bold=True, color=text_color)
    data_font = Font(name="Segoe UI", size=10)
    
    thin_border = Border(
        left=Side(style='thin', color='CBD5E1'),
        right=Side(style='thin', color='CBD5E1'),
        top=Side(style='thin', color='CBD5E1'),
        bottom=Side(style='thin', color='CBD5E1')
    )
    
    # Style header row (Row 1)
    for col in range(1, ws.max_column + 1):
        cell = ws.cell(row=1, column=col)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = thin_border
        
    # Style data rows
    zebra_fill = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")
    white_fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")
    
    for row in range(2, ws.max_row + 1):
        is_even = (row % 2 == 0)
        row_fill = zebra_fill if is_even else white_fill
        for col in range(1, ws.max_column + 1):
            cell = ws.cell(row=row, column=col)
            cell.font = data_font
            cell.border = thin_border
            if not cell.fill.start_color.rgb or cell.fill.start_color.rgb == "00000000":
                cell.fill = row_fill
            # Align numbers right, text left
            if isinstance(cell.value, (int, float)):
                cell.alignment = Alignment(horizontal="right", vertical="center")
            else:
                cell.alignment = Alignment(horizontal="left", vertical="center")
                
    # Auto-fit column widths
    for col in ws.columns:
        max_len = 0
        col_letter = get_column_letter(col[0].column)
        for cell in col:
            val_str = str(cell.value or '')
            max_len = max(max_len, len(val_str))
        ws.column_dimensions[col_letter].width = max(max_len + 4, 12)
        
    ws.row_dimensions[1].height = 28


def create_styled_excel(output_path: str, data_json: str, sheet_name="Data"):
    """
    data_json: JSON string representing list of objects or list of lists
    """
    records = json.loads(data_json)
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = sheet_name
    
    if isinstance(records, list) and len(records) > 0:
        if isinstance(records[0], dict):
            headers = list(records[0].keys())
            ws.append(headers)
            for item in records:
                ws.append([item.get(h, "") for h in headers])
        elif isinstance(records[0], list):
            for row in records:
                ws.append(row)
                
    style_worksheet(ws, title=sheet_name)
    wb.save(output_path)
    print(f"Created styled Excel file: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Excel (.xlsx) Helper")
    subparsers = parser.add_subparsers(dest="action", required=True)
    
    create_p = subparsers.add_parser("create", help="Create styled Excel from JSON")
    create_p.add_argument("output", help="Output .xlsx file")
    create_p.add_argument("--json-data", required=True, help="JSON array of rows/objects")
    create_p.add_argument("--sheet", default="Data", help="Sheet name")
    
    args = parser.parse_args()
    if args.action == "create":
        create_styled_excel(args.output, args.json_data, sheet_name=args.sheet)


if __name__ == "__main__":
    main()
