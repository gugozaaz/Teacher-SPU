---
name: document-processor
description: >-
  Universal document processing skill for reading, extracting, creating, editing, and converting Office documents (.docx, .pptx, .xlsx) and Adobe PDF (.pdf) files, including Quizizz quiz spreadsheet conversion.
  Activate when the user asks to inspect, read, parse, generate, format, or manipulate Word documents, PowerPoint presentations, Excel spreadsheets, or PDF files.
---

# Universal Document Processor Skill

This skill provides powerful and automated workflows for reading, analyzing, modifying, and generating modern Office documents, spreadsheets, PDFs, and quiz import templates.

## Quick CLI Helpers

Helper scripts are available in [`scripts/`](./scripts/):

- **Quiz to Quizizz Excel (.xlsx) Converter** *(Automated & Windows-Native)*:
  ```powershell
  powershell -ExecutionPolicy Bypass -File ".\.agents\skills\document-processor\scripts\quiz_to_xlsx.ps1" -InputMarkdown "<path-to-quiz.md>" [-OutputXlsx "<path-to-quiz.xlsx>"]
  ```
  Parses any Markdown Quiz (`session-XX-quiz.md`) and generates a fully compliant Quizizz import spreadsheet using `QuizizzSampleSpreadsheetUpdated_v2.xlsx`.
  [See Quiz to Excel Guide](./references/quiz_to_xlsx_guide.md)

- **Universal Document Reader**:
  ```bash
  python ".\.agents\skills\document-processor\scripts\doc_reader.py" "<file-path>" [--format markdown|json|text] [--pages 1-5] [--sheet SheetName]
  ```
  Converts `.docx`, `.pptx`, `.xlsx`, `.pdf` to clean Markdown, JSON, or plain text for inspection.

- **Word (.docx) Helper**:
  ```bash
  python ".\.agents\skills\document-processor\scripts\docx_helper.py" <action> [options]
  ```
  [See Word Guide](./references/docx_guide.md)

- **PowerPoint (.pptx) Helper**:
  ```bash
  python ".\.agents\skills\document-processor\scripts\pptx_helper.py" <action> [options]
  ```
  [See PowerPoint Guide](./references/pptx_guide.md)

- **Excel (.xlsx) Helper**:
  ```bash
  python ".\.agents\skills\document-processor\scripts\xlsx_helper.py" <action> [options]
  ```
  [See Excel Guide](./references/xlsx_guide.md)

- **PDF (.pdf) Helper**:
  ```bash
  python ".\.agents\skills\document-processor\scripts\pdf_helper.py" <action> [options]
  ```
  [See PDF Guide](./references/pdf_guide.md)

- **HTML / Reveal.js to Landscape PDF Converter**:
  ```bash
  python ".\.agents\skills\document-processor\scripts\html_to_pdf.py" "<input.html>" "<output.pdf>" [--size 16:10|16:9|A4]
  ```

- **PDF to PowerPoint (.pptx) Converter**:
  ```bash
  python ".\.agents\skills\document-processor\scripts\pdf_to_pptx.py" "<input.pdf>" "<output.pptx>" [--dpi 220]
  ```

---

## Capabilities & Workflows

### 1. Quiz to Quizizz Excel Workflow
Whenever generating or updating teaching materials containing quizzes:
1. Write/update the markdown quiz file `session-XX-quiz.md` (e.g. 10 questions with 3 choices `[x]` and explanations).
2. Run `quiz_to_xlsx.ps1` to produce the companion `session-XX-quiz.xlsx` matching `QuizizzSampleSpreadsheetUpdated_v2.xlsx`.
3. The generated file can be imported directly into Quizizz without manual formatting.

### 2. Reading & Inspecting Documents
Always use `doc_reader.py` to inspect unknown or large binary files:
- Supports UTF-8, Thai language glyphs, and complex table structures.
- For spreadsheets, displays sheet lists and data tables.
- For presentations, displays slide titles, body bullet points, and speaker notes.
- For PDFs, extracts text and tables page-by-page.

### 3. Creating New Documents
- **Word (.docx)**: Use `python-docx` to construct professional documents with headings, styled tables, header/footer, callout boxes, and custom margins.
- **PowerPoint (.pptx)**: Use `python-pptx` to generate 16:9 widescreen presentations with modern color palettes, clean typographic hierarchy, content cards, and structured bullet points.
- **Excel (.xlsx)**: Use `openpyxl` / `pandas` / `quiz_to_xlsx.ps1` to generate workbooks with styled header rows, auto-adjusted column widths, currency/number formatting, formulas, and Quizizz import sheets.
- **PDF (.pdf)**: Generate via HTML/CSS (WeasyPrint/browser print), ReportLab, or convert from DOCX.

### 4. Editing Existing Files
- Load the document object in Python or OpenXML.
- Query targeted paragraphs, slides, sheets, or tables.
- Update text while preserving existing formatting and styles.
- Save to the target path or overwrite cleanly.

---

## Detailed References
- [Quizizz Excel Converter Guide](./references/quiz_to_xlsx_guide.md)
- [Word (.docx) Manual & Recipes](./references/docx_guide.md)
- [PowerPoint (.pptx) Manual & Recipes](./references/pptx_guide.md)
- [Excel (.xlsx) Manual & Recipes](./references/xlsx_guide.md)
- [PDF (.pdf) Manual & Recipes](./references/pdf_guide.md)
