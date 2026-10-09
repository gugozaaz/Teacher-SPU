---
trigger: always_on
---

# Teaching Materials & Presentation Guidelines

## 📌 กฎและมาตรฐานการสร้างเอกสารการสอน (Teaching Materials)

วิชานี้คือ **"พื้นฐานวิทยาการข้อมูล" (Fundamentals of Data Science)** สำหรับนักศึกษาคณะการสร้างเจ้าของธุรกิจ (Entrepreneurship) ที่ไม่มีพื้นฐานไอที/การเขียนโค้ด

### 📁 0. กฎการวางแผนเนื้อหาก่อนสร้าง Session ใหม่ (Mandatory Pre-Writing Pipeline)

⛔ **ก่อนเริ่มสร้างเอกสาร session ใหม่ (session-XX ที่ยังไม่เคยมี) ต้อง activate skill `session-content-planner` ก่อนเสมอ:**

1. อ่านคำแนะนำจาก `.agents/skills/session-content-planner/SKILL.md`
2. ทำ **Mandatory Research Pipeline** ครบ 4 ขั้นตอน:
   - **Step 1:** อ่านแผนการสอนหลัก `fundamentals-of-data-science-v6.md`
   - **Step 2:** อ่าน `session-XX-presentation.html` ของทุก session ก่อนหน้า — ดึง Key Concepts และ Anti-Duplication List
   - **Step 3:** สร้าง Content Brief ภายใน (ไม่ต้องบันทึกเป็นไฟล์แยก)
   - **Step 4:** ใช้ Content Brief เป็น input ในการเขียนเอกสารทุกชิ้น
3. เนื้อหาใหม่ **ต้อง** อ้างอิงหลักการ/concept จาก session ก่อนหน้า แต่ **ห้าม copy use case/กรณีศึกษาเดิมมาซ้ำ**

---

### 📁 1. โครงสร้างไฟล์ในแต่ละ Session (`session/session-XX/`)
1. **`session-XX-presentation.html`**: สไลด์ Reveal.js **อัตราส่วนเริ่มต้น 16:10 (Default: `width: 1280, height: 800`)** พร้อมรองรับการสลับ 16:9 (`width: 1280, height: 720`) ได้ ดีไซน์สวยงาม ทันสมัย ตัวหนังสืออ่านง่าย ไม่เล็กเกินไป มีคำอธิบายภาษาไทยและตัวอย่างธุรกิจไทยที่เข้าใจง่าย
2. **`session-XX-teaching-guide.md`**: แผนการสอน ตารางเวลา และ Slide Mapping
3. **`session-XX-workshop-worksheet.md` & `.html`**: ใบงานกิจกรรม Workshop ประจำคาบเรียน
4. **`session-XX-quiz.md`**: ข้อสอบ Quiz 10 ข้อ 3 ตัวเลือก (A, B, C) พร้อมเฉลยละเอียด
5. **`session-XX-quiz.xlsx`**: **ไฟล์ Excel สำหรับนำเข้า Quizizz (บังคับสร้างคู่กันเสมอ!)**

*(หมายเหตุ: ไฟล์ `session-XX-presentation.pdf` จะไม่ถูกสร้างพร้อมกับชุดเอกสารนี้ แต่จะสร้างแยกต่างหากเมื่อเนื้อหาสไลด์สมบูรณ์และผ่านกระบวนการทดสอบ Layout PDF สัดส่วน 16:10 แล้ว)*

---

### 💾 กฎการสำรองไฟล์สไลด์ก่อนแก้ไข (Presentation Pre-Edit Backup Rule)
⛔ **กฎเหล็กก่อนเริ่มแก้ไขสไลด์ (Mandatory Pre-Edit Backup):**
ทุกครั้งที่มีการแก้ไข ดัดแปลง หรือปรับปรุงเนื้อหาในไฟล์ **`session-XX-presentation.html`** (รวมถึงไฟล์สไลด์ย่อย เช่น `session-XXa-presentation.html`) **ต้องทำการสร้างไฟล์ Backup ของไฟล์เดิมไว้ก่อนเสมอ** ก่อนที่จะลงมือแก้ไขไฟล์ต้นฉบับ:
- **รูปแบบการตั้งชื่อไฟล์:** `session-XX-presentation-Backup-YYYYMMDD-HHMM.html` (โดย `YYYYMMDD-HHMM` คือ ปี ค.ศ. เดือน วัน - ชั่วโมง นาที ณ เวลาที่ทำการแก้ไข เช่น `session-08-presentation-Backup-20261009-1745.html`)
- **ตำแหน่งจัดเก็บ:** บันทึกไว้ในโฟลเดอร์เดียวกันกับไฟล์สไลด์นั้น ๆ (`session/session-XX/`)
- **ข้อห้ามเด็ดขาด:** ห้ามเริ่มเขียนหรือแก้ไขทับไฟล์ต้นฉบับโดยเด็ดขาดจนกว่าจะสร้างไฟล์ Backup สำเร็จเรียบร้อยแล้ว

---

### 🔄 2. กฎการซิงค์เนื้อหาระหว่างเอกสาร (Content Synchronization Rule)
เมื่อมีการแก้ไขหรือปรับปรุงเนื้อหาในสไลด์การสอน **`session-XX-presentation.html`** ให้ทำการตรวจสอบและ**อัปเดตเอกสารอื่นที่เกี่ยวข้องในคาบเรียนนั้นให้สอดคล้องกับเนื้อหาใหม่อยู่เสมอ** ตามลำดับขั้นตอน (Strict Pipeline):
-1. **Pre-Edit Slide Backup:** ตรวจสอบและสร้างไฟล์ Backup ของ `session-XX-presentation.html` ในรูปแบบ `session-XX-presentation-Backup-YYYYMMDD-HHMM.html` ก่อนเริ่มแก้ไขไฟล์จริงทุกครั้ง
0. **`session-XX-presentation.html` (Slide Comment & Numbering Maintenance):**
   - หลังปรับปรุง เพิ่ม ลบ หรือสลับสไลด์เสร็จสิ้น **ต้องทำการ re-check และอัปเดต HTML Comment กำกับหัวสไลด์ทุกหน้า (`<!-- SLIDE X: [SLIDE_NAME] -->`) ให้ถูกต้องเสมอ**
   - **จัดเรียงลำดับหมายเลขสไลด์ (Slide Numbering):** ตรวจสอบว่าหมายเลขสไลด์เรียงลำดับต่อเนื่องถูกต้องตั้งแต่ `SLIDE 1` จนถึงหน้าสุดท้าย (ไม่มีเลขข้าม ซ้ำ หรือเรียงผิด)
   - **ตั้งชื่อระบุสไลด์ (Slide Semantic Identifier):** ตั้งชื่อกำกับสไลด์ให้ตรงกับหัวข้อ/เนื้อหาจริงของสไลด์หน้านั้นอย่างชัดเจน สื่อความหมาย เข้าใจง่าย เช่น `<!-- SLIDE 7: VISUAL COMPARISON: MESSY VS TIDY -->`, `<!-- SLIDE 8: TRAP 1: MULTIPLE VALUES IN ONE CELL -->` เพื่อเป็นจุดอ้างอิง (Reference Point) ที่เข้าใจตรงกันเมื่อต้องการระบุสไลด์เพื่อแก้ไขในอนาคต
1. **`session-XX-teaching-guide.md`**: ปรับแผนการสอน, โครงสร้างเนื้อหา, วัตถุประสงค์, และ Slide Mapping ให้ตรงกับลำดับและเนื้อหาสไลด์ล่าสุด
2. **`session-XX-workshop-worksheet.md`**: ปรับโจทย์กิจกรรม Workshop, กรณีศึกษา และแนวทางวิเคราะห์ให้เชื่อมโยงกับเนื้อหาใหม่
3. **`session-XX-workshop-worksheet.html`**: อัปเดตไฟล์ HTML ของใบงานกิจกรรมให้ตรงกับ Markdown เพื่อพร้อมใช้งาน
4. **Quiz Synchronization Pipeline (ต้องทำ 4.1 ให้เสร็จและบันทึกก่อนทำ 4.2 เสมอ ห้ามข้ามขั้นตอน!):**
   - **4.1 `session-XX-quiz.md` (ขั้นตอนบังคับแก้ไขเนื้อหาข้อสอบ - Mandatory & Non-conditional Edit):**
     - ⛔ **กฎเหล็กเด็ดขาด (No Skip Rule):** ทุกครั้งที่มีการแก้ไข เพิ่ม ลบ หรือปรับปรุงเนื้อหาในสไลด์ `session-XX-presentation.html` **AI มีหน้าที่ต้องเปิดแก้ไขและบันทึกไฟล์ `session-XX-quiz.md` เสมอ ห้ามตัดสินใจข้าม ห้ามคิดเอาเองว่าข้อสอบเดิมดีอยู่แล้ว และห้ามอ้างว่า "เนื้อหาเดิมครอบคลุมแล้ว" โดยเด็ดขาด!**
     - **Slide-to-Quiz Coverage Audit (การตรวจสอบความครอบคลุมของเนื้อหาใหม่):**
       1. ตรวจสอบสไลด์ที่เพิ่มใหม่, สไลด์ที่ถูกแยกออกมา (เช่น แยกกับดักเดี่ยว, แยก Wide/Long), หรือกรณีศึกษาที่ปรับปรุงตาราง
       2. **ต้องปรับปรุงคำถามและตัวเลือกใน 10 ข้อ** ให้มีข้อสอบที่เจาะลึกเนื้อหา/สไลด์ที่เพิ่มใหม่หรือแยกใหม่อย่างน้อย 2-3 ข้อเสมอ (เช่น หากสไลด์แยกกับดักที่ 5 "No Unique ID" ออกมาเดี่ยวๆ หรือเพิ่มเรื่อง "Checkbox Trap" ในแบบฟอร์ม ต้องมีคำถามที่วัดความรู้เรื่องนั้นโดยเฉพาะ)
       3. อัปเดตคำอธิบายเฉลยให้อ้างอิงกฎเหล็ก ชื่อสไลด์ และบริบทธุรกิจตรงกับสไลด์เวอร์ชันล่าสุด
     - **การบันทึกไฟล์:** ต้องเรียกใช้เครื่องมือเขียนหรือแก้ไขไฟล์ (`replace_file_content` หรือ `write_to_file`) กับ `session-XX-quiz.md` ให้สำเร็จก่อนเสมอ
   - **4.2 `session-XX-quiz.xlsx` (แปลงไฟล์เป็นขั้นตอนปิดท้าย):**
     - **หลังจากบันทึกไฟล์ `.md` สำเร็จแล้วเท่านั้น** จึงรันคำสั่งสคริปต์แปลงไฟล์เป็น `.xlsx`
     - ⛔ **Hard Guardrail (ข้อห้ามเด็ดขาด):** **ห้ามรันสคริปต์แปลง `.xlsx` โดยที่ไม่มีการเรียกใช้ Tool แก้ไขและบันทึกไฟล์ `.md` ในรอบนั้นเด็ดขาด** (การรันสคริปต์ทับไฟล์เดิมโดยไม่อัปเดต `.md` จะถือว่าการซิงค์เนื้อหาล้มเหลว)
5. **Automated GitHub Commit & Push (ขั้นตอนปิดท้ายงานทุกครั้ง):**
   - ดำเนินการ Stage, Commit และ Push ขึ้น GitHub เสมอหลังการซิงค์เอกสารและการแก้ไขในรอบนั้นเสร็จสิ้นตามข้อกำหนด

---

### 🖥️ 3. ข้อกำหนดการสร้างสไลด์นำเสนอ (Presentation Specification)
- **อัตราส่วนเริ่มต้น (Default):** **16:10** (`width: 1280, height: 800`, `margin: 0.04`) ให้ขนาดตัวอักษรอ่านง่าย สบายตา ชัดเจน
- **อัตราส่วนสลับใช้งาน:** **16:9** (`width: 1280, height: 720`)
- **มาตรฐานการระบุ Comment กำกับสไลด์ (Slide Header Comment & Numbering Standard):**
  - ทุก `<section>` ของแต่ละสไลด์ **ต้องมี HTML Comment กำกับไว้บรรทัดบนสุดเสมอ** ในรูปแบบ:
    `<!-- SLIDE X: [SLIDE_NAME_OR_TOPIC] -->`
    (เช่น `<!-- SLIDE 7: VISUAL COMPARISON: MESSY VS TIDY -->`, `<!-- SLIDE 8: TRAP 1: MULTIPLE VALUES IN ONE CELL -->`)
  - **ลำดับหมายเลข (Continuous Numbering):** ต้องเรียงลำดับ 1, 2, 3... ต่อเนื่องตั้งแต่สไลด์แรกจนถึงสไลด์สุดท้าย ห้ามมีเลขซ้ำ ตกหล่น หรือข้ามเลขเด็ดขาด
  - **การตั้งชื่อเรียก (Semantic Identifier):** ต้องตั้งชื่อที่กระชับ สื่อถึงหัวข้อและประเด็นสำคัญของสไลด์หน้านั้นอย่างแม่นยำ เพื่อใช้เป็น Anchor อ้างอิงที่ตรงกันระหว่างผู้ใช้และ AI
- **ระบบควบคุมและสลับอัตราส่วน (Controls & Navigation):** ควบคุมผ่าน Keyboard และ Mouse (ปุ่ม `A` สลับ 16:10 / 16:9 พร้อม HUD Toast, ลูกศรซ้าย/ขวา หรือ Mouse Scroll Up/Down สำหรับเปลี่ยนหน้า, `controls: false`)
- 📖 **คู่มือมาตรฐานและโค้ดต้นแบบส่วนกลาง:** [PRESENTATION-CONTROLS.md](file:///d:/GoogleDrive/VibeCoding/teacher/PRESENTATION-CONTROLS.md)
- **โครงสร้างสไลด์เริ่มต้นบังคับ (Mandatory Opening Slides Standard):**
  - **Slide 1 (Title Slide):** ต้องใช้ Style และ Layout มาตรฐานเดียวกับ Session 3 เสมอ (พื้นหลัง `data-background-gradient="radial-gradient(circle at 50% 50%, #e0e7ff 0%, #f8fafc 100%)"`, Badges 2 ป้าย, `<h1>` 2.2em-2.4em, ชื่อวิชาสี secondary, กล่องข้อมูลผู้สอนทรง Pill)
  - **Slide 2 (Recap & Connection):** **ต้องมีสไลด์เชื่อมโยงวงจร Data Science 5 ขั้นตอน (ASK → COLLECT → PREPARE → ANALYZE → ACT) เสมอ ก่อนเข้าสู่เนื้อหาบทเรียนใหม่** (แถบ `step-container` แสดง 5 ขั้นตอนพร้อม Highlight ขั้นประจำคาบ, การ์ด `grid-2` คาบที่แล้ว vs คาบนี้, และกล่องเตือนใจ GIGO)
  - **Slide 3 (Session Roadmap / Agenda):** สรุป 4 เสาหลักของคาบเรียน ก่อนเข้าสู่เนื้อหาหลักใน Slide 4

---

### 📄 4. กระบวนการสร้างไฟล์นำเสนอ PDF (PDF Export Execution)
การสร้างไฟล์ PDF จะทำเมื่อเนื้อหาสไลด์สมบูรณ์ตรงตามความต้องการแล้ว โดยจะต้องผ่านการทดสอบ Layout ด้วย `test-presentation.html` (16:10 Widescreen Layout Test: 1280x800) จนผ่านเกณฑ์ **PASS 100%** ก่อนเสมอ จากนั้นแปลงและบันทึกไฟล์ไว้ที่โฟลเดอร์ `d:\GoogleDrive\VibeCoding\teacher\presentation\` ด้วยคำสั่ง:

```powershell
powershell -ExecutionPolicy Bypass -File ".\.agents\skills\document-processor\scripts\html_to_pdf.ps1" -InputHtml ".\session\session-XX\session-XX-presentation.html" -OutputPdf "d:\GoogleDrive\VibeCoding\teacher\presentation\session-XX-presentation.pdf" -Size "16:10"
```

---

### ⚡ 5. ข้อกำหนดการสร้างไฟล์ Quizizz Excel (`session-XX-quiz.xlsx`)
1. **ข้อบังคับลำดับการทำงาน (Strict Dependency):**
   - **ต้องทำการเขียนหรืออัปเดตไฟล์ `session-XX-quiz.md` ให้เสร็จสมบูรณ์และบันทึกไฟล์ก่อนเสมอ**
   - **ห้าม** สั่งรันสคริปต์แปลง `.xlsx` หากยังไม่มีการอัปเดตเนื้อหาในไฟล์ `.md` ให้สอดคล้องกับ Presentation ล่าสุด
2. **คำสั่งแปลงไฟล์อัตโนมัติ (รันหลังจากบันทึก `.md` เรียบร้อยแล้วเท่านั้น):**

```powershell
powershell -ExecutionPolicy Bypass -File ".\.agents\skills\document-processor\scripts\quiz_to_xlsx.ps1" -InputMarkdown ".\session\session-XX\session-XX-quiz.md"
```

#### กฎการ Map Field Quizizz Template (`QuizizzSampleSpreadsheetUpdated_v2.xlsx`):
* `Question Text` = คำถาม
* `Question Type` = `'Multiple Choice'`
* `Option 1` = ตัวเลือก A
* `Option 2` = ตัวเลือก B
* `Option 3` = ตัวเลือก C
* `Correct Answer` = เลขคำตอบที่ถูกต้อง (`1`, `2`, หรือ `3`)
* `Time in seconds` = `60`
* `Image Link` = ว่าง
* `Answer explanation` = คำอธิบายเฉลย

---

### 🚀 6. ข้อกำหนดการ Commit และ Push ขึ้น GitHub อัตโนมัติ (Automated GitHub Commit & Push Rule)

⛔ **กฎเหล็กบังคับหลังการแก้ไขไฟล์ทุกครั้ง (Mandatory Post-Edit Action):**
ทุกครั้งที่ AI Assistant ดำเนินการสร้าง แก้ไข ปรับปรุง หรือลบไฟล์ใดๆ ในโปรเจกต์นี้ผ่าน Antigravity IDE (ไม่ว่าจะเป็นสไลด์, แผนการสอน, ใบงาน, ควิซ, สคริปต์, โค้ด หรือเอกสารข้อกำหนด) เมื่อการทำงานในแต่ละรอบหรือแต่ละคำขอเสร็จสิ้นเรียบร้อยแล้ว **ต้องทำการ Commit และ Push ขึ้น GitHub เสมอ** โดยปฏิบัติตามขั้นตอนต่อไปนี้อย่างเคร่งครัด:

1. **ตรวจสอบสถานะไฟล์ที่มีการเปลี่ยนแปลง (Check Status):** `git status`
2. **Stage ไฟล์ทั้งหมดที่มีการเปลี่ยนแปลง (Stage Changes):** `git add -A`
3. **Commit พร้อมระบุข้อความที่สื่อความหมายชัดเจน (Descriptive Commit Message):**
   ```powershell
   git commit -m "<type>(<scope>): <message>"
   ```
4. **Push ขึ้น GitHub Remote ทันที (Push to Remote):**
   ```powershell
   git push origin main
   ```
5. **รายงานผลให้ผู้ใช้ทราบ (Report to User):**
   - ทุกครั้งที่เสร็จสิ้นภารกิจ ต้องระบุผลการ Commit (เช่น Commit Message หรือ Short Hash) และสถานะการ Push ขึ้น GitHub ในคำตอบปิดท้ายเสมอ
