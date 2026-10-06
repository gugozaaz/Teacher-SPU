# Teacher Workspace Guidelines for AI Assistant

## 🎯 มาตรฐานการสร้างเอกสารและสื่อการสอน (Teaching Materials Standard)

วิชานี้คือ **"พื้นฐานวิทยาการข้อมูล" (Fundamentals of Data Science)** สำหรับนักศึกษาคณะการสร้างเจ้าของธุรกิจ (Entrepreneurship) ที่ไม่มีพื้นฐานไอที/การเขียนโค้ด

### 📁 ชุดเอกสารที่ต้องมีในแต่ละคาบเรียน (`session/session-XX/`)
1. **`session-XX-presentation.html`**: สไลด์ Reveal.js **อัตราส่วนเริ่มต้น 16:10 (Default: `width: 1280, height: 800`)** พร้อมรองรับการสลับ 16:9 (`width: 1280, height: 720`) ได้ ดีไซน์สวยงาม ทันสมัย ตัวหนังสืออ่านง่าย ไม่เล็กเกินไป มีคำอธิบายภาษาไทยและตัวอย่างธุรกิจไทยที่เข้าใจง่าย
2. **`session-XX-teaching-guide.md`**: แผนการสอน ตารางเวลา และ Slide Mapping
3. **`session-XX-workshop-worksheet.md` & `.html`**: ใบงานกิจกรรม Workshop ประจำคาบเรียน
4. **`session-XX-quiz.md`**: ข้อสอบ Quiz 10 ข้อ 3 ตัวเลือก (A, B, C) พร้อมเฉลยละเอียด
5. **`session-XX-quiz.xlsx`**: **ไฟล์ Excel สำหรับนำเข้า Quizizz (บังคับสร้างคู่กันเสมอ!)**

*(หมายเหตุ: ไฟล์ `session-XX-presentation.pdf` จะไม่ถูกสร้างพร้อมกับชุดเอกสารนี้ แต่จะสร้างแยกต่างหากเมื่อเนื้อหาสไลด์สมบูรณ์และผ่านกระบวนการทดสอบ Layout PDF สัดส่วน 16:10 แล้ว)*

---

### 📚 กฎการอ้างอิงแผนการสอนและเนื้อหาก่อนหน้า (Curriculum-Aware Content Generation Rule)

⛔ **เมื่อได้รับคำสั่งให้สร้างเอกสาร session ใหม่ (session-XX ที่ยังไม่เคยมี) ต้องทำขั้นตอนต่อไปนี้ก่อนเริ่มเขียนเนื้อหาเสมอ:**

> **Activate Skill:** `session-content-planner` — อ่านคำแนะนำเต็มได้ที่ `.agents/skills/session-content-planner/SKILL.md`

#### ขั้นตอนบังคับ (Mandatory Pre-Writing Pipeline):

1. **อ่านแผนการสอนหลัก (Syllabus Reference):**
   - เปิดอ่านไฟล์ `fundamentals-of-data-science-v6.md` ที่ root ของ workspace
   - ค้นหาหัวข้อ, เนื้อหาหลัก, Module, และกิจกรรม Quiz/Workshop ที่กำหนดไว้สำหรับ session ที่จะสร้าง
   - ระบุตำแหน่งของ session ในวงจร Data Science 5 ขั้นตอน (ASK → COLLECT → PREPARE → ANALYZE → ACT)

2. **อ่านสไลด์การสอนครั้งก่อนหน้าทั้งหมด (Prior Sessions Scan):**
   - อ่านไฟล์ `session-XX-presentation.html` ของ **ทุก session ที่มีอยู่แล้ว** ก่อนหน้า session ที่จะสร้าง
   - ดึง **Key Concepts** (หลักการ/นิยาม/คำศัพท์สำคัญ) ที่เคยสอนไปแล้ว
   - จดรายการ **use case/กรณีศึกษา** ที่เคยใช้แล้วเป็น Anti-Duplication List

3. **สร้างเนื้อหาที่เชื่อมโยงข้ามคาบ (Cross-Session Knowledge Linking):**
   - เนื้อหาใหม่ **ต้อง** มีสไลด์ Recap สั้น ๆ (1-2 สไลด์) เชื่อมจากครั้งก่อน
   - ต้องอ้างอิงหลักการ/concept จาก session ก่อนหน้าในจุดที่เหมาะสม
   - Workshop ต้องต่อยอดจากทักษะ/ความรู้ที่เคยฝึกไปแล้ว
   - ⚠️ **ห้าม copy use case/กรณีศึกษาจาก session ก่อนหน้ามาใช้ซ้ำเด็ดขาด** — ใช้ได้เฉพาะหลักการ/concept เท่านั้น

---

### 🔄 กฎการซิงค์เนื้อหาระหว่างเอกสาร (Content Synchronization Rule)
เมื่อมีการแก้ไขหรือปรับปรุงเนื้อหาในสไลด์การสอน **`session-XX-presentation.html`** ให้ทำการตรวจสอบและ**อัปเดตเอกสารอื่นที่เกี่ยวข้องในคาบเรียนนั้นให้สอดคล้องกับเนื้อหาใหม่อยู่เสมอ** ตามลำดับขั้นตอน (Strict Pipeline):
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

---

### 🖥️ มาตรฐานการสร้างสไลด์นำเสนอ (Presentation Specification)
- **อัตราส่วนหน้าจอ (Aspect Ratio & Resolution):**
  - **อัตราส่วนเริ่มต้น (Default):** **16:10** (`width: 1280, height: 800`, `margin: 0.04`) ให้ขนาดตัวอักษรอ่านง่าย สบายตา ชัดเจน
  - **อัตราส่วนสลับใช้งาน:** **16:9** (`width: 1280, height: 720`)
- **มาตรฐานการระบุ Comment กำกับสไลด์ (Slide Header Comment & Numbering Standard):**
  - ทุก `<section>` ของแต่ละสไลด์ **ต้องมี HTML Comment กำกับไว้บรรทัดบนสุดเสมอ** ในรูปแบบ:
    `<!-- SLIDE X: [SLIDE_NAME_OR_TOPIC] -->`
    (เช่น `<!-- SLIDE 7: VISUAL COMPARISON: MESSY VS TIDY -->`, `<!-- SLIDE 8: TRAP 1: MULTIPLE VALUES IN ONE CELL -->`)
  - **ลำดับหมายเลข (Continuous Numbering):** ต้องเรียงลำดับ 1, 2, 3... ต่อเนื่องตั้งแต่สไลด์แรกจนถึงสไลด์สุดท้าย ห้ามมีเลขซ้ำ ตกหล่น หรือข้ามเลขเด็ดขาด
  - **การตั้งชื่อเรียก (Semantic Identifier):** ต้องตั้งชื่อที่กระชับ สื่อถึงหัวข้อและประเด็นสำคัญของสไลด์หน้านั้นอย่างแม่นยำ เพื่อใช้เป็น Anchor อ้างอิงที่ตรงกันระหว่างผู้ใช้และ AI
- **ระบบควบคุมและสลับอัตราส่วน (Controls & Navigation):**
  - ซ่อนปุ่มลูกศรนำทาง (`controls: false`) และไม่มีแถบด้านล่าง (`deck-footer`) บังเนื้อหา
  - ควบคุมการเปลี่ยนสไลด์ด้วย Keyboard (`←` ถอยหลัง, `→` ไปข้างหน้า) หรือ Mouse Wheel (Scroll Up ถอยหลัง, Scroll Down ไปข้างหน้า, `mouseWheel: true`)
  - สลับขนาดหน้าจอด้วยปุ่ม **`A`** (Aspect Ratio) พร้อม HUD Toast แจ้งเตือนสถานะขนาดหน้าจอชั่วคราว 1.5 วินาที
  - 📖 **คู่มือมาตรฐานและโค้ดต้นแบบส่วนกลาง:** [PRESENTATION-CONTROLS.md](file:///d:/GoogleDrive/VibeCoding/teacher/PRESENTATION-CONTROLS.md)
- **โครงสร้างสไลด์เริ่มต้นบังคับ (Mandatory Opening Slides Standard):**
  - **Slide 1 (Title Slide):** ต้องใช้ Style และ Layout มาตรฐานเดียวกับ Session 3 เสมอ:
    - พื้นหลัง Gradient ละมุน: `data-background-gradient="radial-gradient(circle at 50% 50%, #e0e7ff 0%, #f8fafc 100%)"`
    - ป้าย Badge ด้านบน 2 ป้าย: ภาคเรียน (เช่น `badge-primary` ภาคเรียนที่ 1/2569) และครั้งที่สอน (เช่น `badge-accent` ครั้งที่ XX / 14)
    - หัวข้อใหญ่ `<h1>` (ขนาด 2.2em - 2.4em, weight 900) 2 บรรทัด ระบุชื่อขั้นตอนและหัวข้อหลัก
    - ชื่อวิชา: `Fundamentals of Data Science (พื้นฐานวิทยาการข้อมูล)` สี `var(--secondary)`
    - ป้ายกล่องผู้สอน Pill Shape ขอบมนพื้นขาว มีเงา แสดงไอคอนและชื่ออาจารย์ผู้สอน
  - **Slide 2 (Recap & Connection):** **ต้องมีสไลด์เชื่อมโยงวงจร Data Science 5 ขั้นตอน (ASK → COLLECT → PREPARE → ANALYZE → ACT) เสมอ ก่อนเข้าสู่เนื้อหาบทเรียนใหม่:**
    - กล่องผังขั้นตอน `step-container` แสดงทั้ง 5 ขั้นตอน (1. ASK → 2. COLLECT → 3. PREPARE → 4. ANALYZE → 5. ACT) โดยทำ Highlight กล่องขั้นตอนประจำคาบเรียนปัจจุบัน (`border: 2px solid var(--primary); transform: scale(1.04); background: #eef2ff;`)
    - การ์ดคู่เปรียบเทียบ `grid-2`: "คาบที่แล้ว (Session XX-1)" vs "คาบนี้ (Session XX)" เพื่อทบทวนและปูทางอย่างราบรื่น
    - กล่องเตือนใจหรือกฎเหล็ก (เช่น กฎ GIGO หรือ Key Takeaway)
  - **Slide 3 (Session Roadmap / Agenda):** แสดงแผนที่การเรียนรู้ 4 เสาหลักของคาบเรียน ก่อนเข้าสู่เนื้อหาหลักใน Slide 4

---

### 📄 กระบวนการสร้างไฟล์นำเสนอ PDF (session-XX-presentation.pdf Generation Process)
การสร้างไฟล์ PDF จะทำเมื่อเนื้อหาสไลด์สมบูรณ์ตรงตามความต้องการแล้ว โดยจะต้องผ่านการทดสอบ Layout และขนาดสัดส่วนหน้าจอตามขั้นตอนดังนี้:
1. **สร้างไฟล์ `test-presentation.html`**: สร้างไฟล์นี้ไว้ในโฟลเดอร์คาบเรียน (`session/session-XX/test-presentation.html`) เพื่อใช้เป็น Automated Layout Test Runner
2. **รันการทดสอบขนาด PDF สัดส่วน 16:10 (16:10 Widescreen Layout Test):**
   - รันเพื่อทดสอบความพอดีของเนื้อหากับ**สัดส่วน 16:10 (`1280x800`) เพื่อให้ Element และการตัดคำทุกอย่างตรงกับหน้าเว็บเบราว์เซอร์ 100%**
   - ตรวจสอบว่าความสูงของเนื้อหาในแต่ละสไลด์ (Content Height) พอดีกับกรอบ 16:10 (800px) และไม่ล้นหน้าจอ (ต้องผ่านเกณฑ์ **PASS 100%**)
3. **ตรวจสอบการจัดเรียงตัวอักษรและองค์ประกอบ (Typography & Visual Inspection):**
   - ตรวจสอบการตัดคำภาษาไทย, หัวข้อ, เนื้อหาย่อย, การจัดวางการ์ด และตาราง
   - ตรวจสอบว่าไม่มีข้อความเบี้ยว ซ้อนทับ หลุดกรอบ หรือขนาดผิดสัดส่วนในมุมมอง 16:10
4. **การวนรอบปรับปรุงแก้ไข (Feedback & Refinement Loop):**
   - หากพบสไลด์ที่ไม่ผ่าน (FAIL), เนื้อหาล้น หรือมีข้อความเบี้ยวไม่สวยงาม **ต้องกลับไปปรับปรุงแก้ไขไฟล์ `session-XX-presentation.html` ให้เรียบร้อย** แล้วรันการทดสอบใหม่อีกครั้งจนกว่าจะถูกต้องสมบูรณ์ 100%
5. **การแปลงเป็นไฟล์ PDF (PDF Export Execution):**
   - เมื่อผ่านการทดสอบด้วย `test-presentation.html` ครบ 100% แล้ว ให้ทำการแปลงไฟล์เป็น PDF และบันทึกไว้ที่โฟลเดอร์ `d:\GoogleDrive\VibeCoding\teacher\presentation\` (ไม่เก็บรวมกับโฟลเดอร์ `session`) ด้วยคำสั่ง:
   ```powershell
   powershell -ExecutionPolicy Bypass -File ".\.agents\skills\document-processor\scripts\html_to_pdf.ps1" -InputHtml ".\session\session-XX\session-XX-presentation.html" -OutputPdf "d:\GoogleDrive\VibeCoding\teacher\presentation\session-XX-presentation.pdf" -Size "16:10"
   ```

---

### ⚡ กฎการแปลง Quiz Markdown เป็น Quizizz Excel (.xlsx)
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
