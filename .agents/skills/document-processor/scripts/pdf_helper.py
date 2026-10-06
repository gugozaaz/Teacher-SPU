#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PDF Helper Script for Antigravity
Provides utilities for extracting text/tables, merging/splitting, and converting PDF pages.
"""

import sys
import os
import io
import argparse
import pypdf

# Force UTF-8
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


def merge_pdfs(input_files: list, output_path: str):
    merger = pypdf.PdfMerger()
    for pdf in input_files:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()
    print(f"Merged {len(input_files)} PDFs into: {output_path}")


def split_pdf(input_file: str, output_dir: str):
    reader = pypdf.PdfReader(input_file)
    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    
    for idx, page in enumerate(reader.pages, start=1):
        writer = pypdf.PdfWriter()
        writer.add_page(page)
        out_path = os.path.join(output_dir, f"{base_name}_page_{idx}.pdf")
        with open(out_path, "wb") as f:
            writer.write(f)
    print(f"Split {len(reader.pages)} pages into: {output_dir}")


def extract_pdf_images(input_file: str, output_dir: str):
    try:
        import fitz  # PyMuPDF
        doc = fitz.open(input_file)
        os.makedirs(output_dir, exist_ok=True)
        img_count = 0
        for p_idx, page in enumerate(doc, start=1):
            pix = page.get_pixmap(dpi=150)
            img_path = os.path.join(output_dir, f"page_{p_idx}.png")
            pix.save(img_path)
            img_count += 1
        print(f"Rendered {img_count} page image(s) into: {output_dir}")
    except Exception as e:
        print(f"Error rendering images: {e}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description="PDF Helper")
    subparsers = parser.add_subparsers(dest="action", required=True)
    
    merge_p = subparsers.add_parser("merge", help="Merge multiple PDFs")
    merge_p.add_argument("inputs", nargs="+", help="Input PDF files")
    merge_p.add_argument("--output", required=True, help="Output PDF file")
    
    split_p = subparsers.add_parser("split", help="Split PDF into pages")
    split_p.add_argument("input", help="Input PDF file")
    split_p.add_argument("--output-dir", required=True, help="Output directory")
    
    render_p = subparsers.add_parser("render-images", help="Render pages as images")
    render_p.add_argument("input", help="Input PDF file")
    render_p.add_argument("--output-dir", required=True, help="Output directory")
    
    args = parser.parse_args()
    if args.action == "merge":
        merge_pdfs(args.inputs, args.output)
    elif args.action == "split":
        split_pdf(args.input, args.output_dir)
    elif args.action == "render-images":
        extract_pdf_images(args.input, args.output_dir)


if __name__ == "__main__":
    main()
