# Quizizz Excel (.xlsx) Converter Guide

คู่มือและข้อกำหนดสำหรับการสร้างไฟล์แบบทดสอบ Quizizz Spreadsheet (`.xlsx`) จาก Markdown Quiz สำหรับทุก Session การสอน

---

## 1. วัตถุประสงค์
เพื่อให้แบบทดสอบ (Quiz) ที่สร้างในรูปแบบ Markdown (`session-XX-quiz.md`) สามารถแปลงเป็นไฟล์ Excel (`session-XX-quiz.xlsx`) ตาม Template `QuizizzSampleSpreadsheetUpdated_v2.xlsx` ได้อย่างอัตโนมัติ 100% พร้อมนำไปกด **Import from Spreadsheet** บนแพลตฟอร์ม **Quizizz** ทันที

---

## 2. โครงสร้างและกฎการ Map Field (Quizizz Schema)

| คอลัมน์ | Header Name | กฎและเงื่อนไขข้อมูล |
| :---: | :--- | :--- |
| **A** | `Question Text` | ข้อความคำถาม (ดึงจาก Markdown บรรทัด `**คำถาม:** ...`) |
| **B** | `Question Type` | ค่าตายตัว: **`Multiple Choice`** |
| **C** | `Option 1` | ข้อความตัวเลือกที่ 1 (Choice A) |
| **D** | `Option 2` | ข้อความตัวเลือกที่ 2 (Choice B) |
| **E** | `Option 3` | ข้อความตัวเลือกที่ 3 (Choice C) |
| **F** | `Correct Answer` | หมายเลขของตัวเลือกที่ถูกต้อง (`1`, `2`, `3`, หรือ `4`) ตรวจจับจาก `[x]` |
| **G** | `Time in seconds` | ค่าเวลาต่อข้อ: กำหนดเป็น **`60`** วินาที |
| **H** | `Image Link` | เว้นว่างไว้ |
| **I** | `Answer explanation` | คำอธิบายเฉลยและเหตุผลประกอบ (ดึงจาก `**เฉลย:** ...`) |

---

## 3. รูปแบบ Markdown Quiz มาตรฐาน (`session-XX-quiz.md`)

```markdown
### ข้อที่ 1:
**คำถาม:** ในวงจร Data Science 5 ขั้นตอน ขั้นตอนที่ 1 'ASK' มีความสำคัญอย่างไร?
- [ ] A) เป็นขั้นตอนที่ใช้ AI เขียนโค้ดซับซ้อนที่สุด
- [x] B) ถ้าตั้งคำถามผิด ข้อมูลและการวิเคราะห์ที่ตามมาก็จะได้คำตอบที่ผิด
- [ ] C) เจ้าของธุรกิจไม่ต้องทำ ให้โปรแกรมเมอร์ทำแทนได้
**เฉลย:** B) "ถ้าตั้งคำถามผิด ข้อมูลก็ให้คำตอบที่ผิด" การตั้งคำถามที่ตรงกับปัญหาธุรกิจจริงเป็นจุดเริ่มต้นที่สำคัญที่สุด
```

---

## 4. คำสั่ง CLI ในการแปลงไฟล์อัตโนมัติ

เปิดรันคำสั่ง PowerShell จาก Workspace Root:

```powershell
# แปลงไฟล์ Quiz ของ Session 02 (บันทึกเป็น .xlsx ในโฟลเดอร์เดียวกัน)
powershell -ExecutionPolicy Bypass -File ".\.agents\skills\document-processor\scripts\quiz_to_xlsx.ps1" -InputMarkdown ".\session\session-02\session-02-quiz.md"

# หรือระบุปลายทาง Output เอง
powershell -ExecutionPolicy Bypass -File ".\.agents\skills\document-processor\scripts\quiz_to_xlsx.ps1" -InputMarkdown ".\session\session-03\session-03-quiz.md" -OutputXlsx ".\session\session-03\session-03-quiz.xlsx"
```

> [!IMPORTANT]
> **ข้อบังคับลำดับการทำงาน:** ต้องทำการตรวจสอบและแก้ไขเนื้อหาในไฟล์ `session-XX-quiz.md` ให้ตรงกับ Presentation ล่าสุดและบันทึกลงดิสก์ให้เรียบร้อยก่อนเสมอ ห้ามรันสคริปต์แปลงไฟล์ `.xlsx` โดยที่ยังไม่ได้แก้ไขไฟล์ `.md` ในรอบนั้นเด็ดขาด เพื่อป้องกันการบันทึกทับด้วยข้อสอบเก่า

---

## 5. การเปิดไฟล์ Template อย่างปลอดภัย (Technical Note)
- ตัวสคริปต์ `quiz_to_xlsx.ps1` ใช้ `[System.IO.FileShare]::ReadWrite` ในการอ่าน Template เพื่อป้องกันปัญหา File Lock กรณีที่ผู้ใช้กำลังเปิดไฟล์ Excel ทิ้งไว้อยู่
- ระบบจัดเก็บ Zip Entry ด้วย Forward Slash (`/`) ตามมาตรฐาน OpenXML (ECMA-376) ทำให้เปิดได้สมบูรณ์ทั้งใน MS Excel, LibreOffice และระบบ Cloud Importer ของ Quizizz
