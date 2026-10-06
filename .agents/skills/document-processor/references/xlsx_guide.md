# Excel (.xlsx) Reference Guide

## Essential Python Snippets

### 1. Reading Excel with Pandas / OpenPyXL
```python
import pandas as pd

# Read specific sheet
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")
print(df.head())

# Read all sheets into dictionary
all_sheets = pd.read_excel("data.xlsx", sheet_name=None)
for sheet_name, df_sheet in all_sheets.items():
    print(f"Sheet {sheet_name}: {len(df_sheet)} rows")
```

### 2. Creating styled Excel Workbook with OpenPyXL
```python
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Financial Summary"

# Header
ws.append(["Category", "Q1", "Q2", "Q3", "Q4", "Total"])
header_fill = PatternFill(start_color="1E293B", end_color="1E293B", fill_type="solid")
header_font = Font(name="Segoe UI", size=11, bold=True, color="FFFFFF")

for col in range(1, 7):
    c = ws.cell(row=1, column=col)
    c.fill = header_fill
    c.font = header_font
    c.alignment = Alignment(horizontal="center")

# Add data & formulas
ws.append(["Revenue", 120000, 145000, 160000, 210000, "=SUM(B2:E2)"])
ws.append(["Expenses", 85000, 92000, 95000, 110000, "=SUM(B3:E3)"])

wb.save("financial_summary.xlsx")
```
