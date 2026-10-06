# Word (.docx) Reference Guide

## Essential Python Snippets

### 1. Reading full document text and headings
```python
from docx import Document

doc = Document("sample.docx")
for p in doc.paragraphs:
    if p.text.strip():
        print(f"[{p.style.name}] {p.text}")
```

### 2. Reading all tables
```python
from docx import Document

doc = Document("sample.docx")
for table in doc.tables:
    for row in table.rows:
        row_data = [cell.text.strip() for cell in row.cells]
        print(" | ".join(row_data))
```

### 3. Generating a document with custom styling
```python
from docx import Document
from docx.shared import Inches, Pt, RGBColor

doc = Document()
heading = doc.add_heading("Project Report", level=1)
p = doc.add_paragraph("This is a paragraph with ")
bold_run = p.add_run("bold text")
bold_run.font.bold = True
bold_run.font.color.rgb = RGBColor(0x0F, 0x52, 0xBA)

doc.save("output.docx")
```

### 4. Thai Language Support
Ensure fonts supporting Thai glyphs (e.g. `TH Sarabun New`, `Sarabun`, `Tahoma`, `Arial Unicode MS`, `Cordia New`, `Segoe UI`) are used when formatting runs:
```python
run.font.name = 'Sarabun'
```
