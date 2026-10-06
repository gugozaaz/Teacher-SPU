# Thai Language & Unicode Guidelines for Antigravity Documents

## 🇹🇭 การรองรับภาษาไทยในชุดเอกสาร (Thai Language Support)

ระบบเอกสารนี้ได้รับการปรับแต่งเพื่อรองรับ **Unicode (UTF-8)** และโครงสร้างตัวอักษรภาษาไทยอย่างสมบูรณ์แบบ (พยัญชนะ สระบน/ล่าง วรรณยุกต์ ไม้ไต่คู้ สระอำ สระจม/ลอย):

---

### 1. ฟอนต์ภาษาไทยที่แนะนำสำหรับ Windows
เพื่อให้การแสดงผลสระและวรรณยุกต์ถูกต้อง สวยงาม และไม่ลอย:

| โปรแกรม | ฟอนต์แนะนำ | หมายเหตุ |
| :--- | :--- | :--- |
| **PowerPoint (.pptx)** | `Leelawadee UI`, `Segoe UI`, `Tahoma` | อ่านง่าย คมชัดบนหน้าจอ 16:9 |
| **Word (.docx)** | `TH Sarabun New`, `Sarabun`, `Cordia New`, `Angsana New`, `Leelawadee UI` | มาตรฐานเอกสารทางการและรายงาน |
| **Excel (.xlsx)** | `Segoe UI`, `Leelawadee UI`, `Tahoma` | ตารางตัวเลขและข้อความตรงช่อง |
| **PDF (.pdf)** | `tahoma.ttf`, `leelawad.ttf`, `sarabun.ttf` | ฝังฟอนต์ TrueType เพื่อป้องกันฟอนต์เพี้ยน |

---

### 2. ตัวอย่างการกำหนดฟอนต์ภาษาไทยใน Python

#### Word (`python-docx`):
```python
from docx import Document
from docx.shared import Pt

doc = Document()
p = doc.add_paragraph()
run = p.add_run("ข้อความภาษาไทยที่มีสระและวรรณยุกต์ครบถ้วน")
run.font.name = "TH Sarabun New"  # หรือ "Leelawadee UI"
run.font.size = Pt(16)
```

#### PowerPoint (`python-pptx`):
```python
from pptx import Presentation
from pptx.util import Pt

prs = Presentation()
slide = prs.slides.add_slide(prs.slide_layouts[6])
tb = slide.shapes.add_textbox(0, 0, 10, 2)
p = tb.text_frame.paragraphs[0]
p.text = "หัวข้อการนำเสนอภาษาไทย"
p.font.name = "Leelawadee UI"
p.font.size = Pt(32)
```

#### การประมวลผลภาษาไทยขั้นสูง (`pythainlp`):
```python
from pythainlp import word_tokenize, thai_strftime
from datetime import datetime

# ตัดคำภาษาไทย
words = word_tokenize("ระบบจัดการเอกสารอัตโนมัติ", engine="newmm")
print(words)  # ['ระบบ', 'จัดการ', 'เอกสาร', 'อัตโนมัติ']

# แปลงวันที่แบบไทย
thai_date = thai_strftime(datetime.now(), "%d %B %BE")
print(thai_date)  # เช่น '25 สิงหาคม 2569'
```
