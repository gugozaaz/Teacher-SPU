# PDF (.pdf) Reference Guide

## Essential Python Snippets

### 1. Extracting text and structured tables with PDFPlumber
```python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    for idx, page in enumerate(pdf.pages, start=1):
        print(f"--- Page {idx} ---")
        text = page.extract_text()
        print(text)
        
        tables = page.extract_tables()
        for table in tables:
            for row in table:
                print(" | ".join([str(c or '') for c in row]))
```

### 2. High-speed text & metadata extraction with PyMuPDF (fitz)
```python
import fitz

doc = fitz.open("document.pdf")
print("Total Pages:", len(doc))
print("Metadata:", doc.metadata)

for page in doc:
    print(page.get_text())
```

### 3. Rendering PDF pages to Images
```python
import fitz

doc = fitz.open("document.pdf")
for i, page in enumerate(doc):
    pix = page.get_pixmap(dpi=150)
    pix.save(f"page_{i+1}.png")
```

### 4. Merging and Splitting PDFs with PyPDF
```python
import pypdf

# Merge
merger = pypdf.PdfMerger()
merger.append("file1.pdf")
merger.append("file2.pdf")
merger.write("combined.pdf")
merger.close()
```
