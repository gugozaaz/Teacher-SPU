# Design Document: Session 10 Courseware Upgrade & Learner Review Loop

- **Date:** 2026-10-24
- **Course:** Fundamentals of Data Science (พื้นฐานวิทยาการข้อมูล)
- **Target Audience:** Entrepreneurship Students (ไม่มีพื้นฐานไอที/การเขียนโค้ด/สถิติขั้นสูง)
- **Primary Topic:** Session 10 — Step 4 'ANALYZE' (Part 5): Customer Segmentation (RFM) & What-If Analysis

---

## 1. Intent & The Why

### Background & Problem
นักศึกษาคณะการสร้างเจ้าของธุรกิจต้องการใช้ข้อมูลเพื่อการตัดสินใจทางธุรกิจจริง แต่เนื้อหาสไลด์เดิมใน Session 10 มีลักษณะ:
1. การอธิบายสูตรและฟังก์ชัน Spreadsheet (`=IFS()`, Pivot Tables) ถูกจัดวางแยกไว้ท้ายคาบ ไม่ได้เชื่อมโยงกับทฤษฎีในขณะที่สอน
2. ขาด "Business Mental Model" เชิงภาพ (Visual Metaphors) เช่น ภาพถังแยกเกรดลูกค้า หรือคันโยกจำลองผลกำไร ทำให้ผู้เรียนที่ไม่มีพื้นฐาน Data เกิด Cognitive Overload
3. จำเป็นต้องมีกลไกตรวจสอบคุณภาพสองด้าน:
   - **ด้านการสอน (Pedagogical Clarity):** มี Subagent สวมบทบาทเป็น "นักศึกษาผู้ประกอบการมือใหม่" ตรวจสอบความเข้าใจง่าย ความต่อเนื่อง และความถูกต้องของข้อมูล
   - **ด้านการแสดงผล (Visual & Layout Integrity):** ทดสอบบนสัดส่วน 16:10 (1280x800) ให้ผ่านเกณฑ์ 100% ไม่มีเนื้อหาล้นกรอบหรือตัวอักษรหลุดจอ

---

## 2. Goals, Non-Goals & Anti-Goals

### Goals
1. **4-Step Progressive Learning Architecture:** ร้อยเรียงเนื้อหาเป็น 4 ขั้นตอนต่อเนื่อง:
   `[1. ทฤษฎีและหลักคิดธุรกิจ] ➔ [2. ตรรกะสูตรคำนวณแบบง่าย] ➔ [3. ตัวอย่างตารางข้อมูลจริง] ➔ [4. Prompt สั่ง AI คำนวณแทน]`
2. **Dual-Track Integrated Cycles:** ประยุกต์ใช้โครงสร้าง 4 ขั้นตอนกับ 2 วงจรหลัก:
   - **Cycle A:** Customer Segmentation (RFM Mastery, Personas & Visual Pivot Table)
   - **Cycle B:** What-If Analysis & Scenario Simulation (Pricing, Off-Peak, Churn Recovery)
3. **Real Data Grounding:** อ้างอิงและเชื่อมโยงชุดข้อมูลเดิมของวิชา:
   - `session-10-pulse-studio-rfm.csv` (ตัวอย่างหลัก 500 รายการ)
   - `session-6a-coffee-sales-crm.csv` (เชื่อมโยงที่มาของ Raw Transactions สู่ Customer Aggregation)
   - `session-08-coffee-sales-correlation.csv` (ใช้เป็นสะพานเชื่อมโยงความสัมพันธ์ Price vs Demand ในการสร้าง What-If Levers)
4. **Autonomous Learner Review Loop:** ใช้ Subagent เป็นตัวแทนผู้เรียน ตรวจทานความชัดเจน ภาษา และความถูกต้อง ก่อนส่งมอบ
5. **Rigorous Layout Testing:** ผ่านการทดสอบบน `test-presentation.html` สัดส่วน 16:10 (1280x800) PASS 100% ปราศจาก Scrollbar และ Overflow
6. **Strict Workspace Compliance:**
   - ทำการสำรองไฟล์ `session-10-presentation-Backup-YYYYMMDD-HHMM.html` ก่อนแก้ไข
   - รักษาหมายเลขสไลด์และคอมเมนต์ `<!-- SLIDE X: [NAME] -->` ต่อเนื่องครบ 28 สไลด์
   - อัปเดต `session-10-quiz.md` (10 ข้อ) ให้ครอบคลุมเนื้อหาใหม่ และแปลงเป็น `session-10-quiz.xlsx`
   - Git Commit & Push เมื่อเสร็จสมบูรณ์
7. **Roadmap to Subsequent Sessions:** กำหนดพิมพ์เขียวนี้เพื่อนำไปประยุกต์ใช้ต่อกับ Session 11, 12, 13, 14 ตามลำดับ

### Non-Goals
- ไม่สร้างหรืออัปเดตไฟล์ `session-10-teaching-guide.md`, `session-10-workshop-worksheet.md`, `session-10-workshop-worksheet.html` (เป็นไปตามกฎ Strict Content Update Exemptions ใน `AGENTS.md`)
- ไม่สร้างไฟล์ PDF อัตโนมัติ (จะสร้างเมื่อมีคำสั่ง Explicit Command เท่านั้น)
- ไม่นำสูตรคณิตศาสตร์ขั้นสูงหรือโค้ดโปรแกรมมิ่ง (Python/SQL/R) เข้ามาในสไลด์

### Anti-Goals
- ไม่สร้างสไลด์ที่มีแต่ตัวหนังสือแน่น (Wall of Text)
- ไม่อธิบายสูตร Spreadsheet แบบลอยๆ โดยไม่ระบุความหมายทางธุรกิจ
- ไม่ปล่อยให้ความสูงของเนื้อหาสไลด์เกิน 800px ในสัดส่วน 16:10

---

## 3. Approaches Considered

### Approach 1: Dual-Track Integrated Flow (CHOSEN)
- จัดเนื้อหาเป็น 2 วงจรสมบูรณ์:
  - **Cycle A (RFM):** Theory ➔ Formula/Logic ➔ Pulse Studio CSV ➔ Gemini Prompt & Segmentation Matrix
  - **Cycle B (What-If):** Theory ➔ Formula/Logic ➔ 3 Real Business Cases ➔ Gemini Prompt & Simulation Stress-Test
- **เหตุผลที่เลือก:** แก้ปัญหา Cognitive Overload ผู้เรียนเห็นภาพการต่อยอดจากทฤษฎีสู่สูตร และเห็นพลังของ AI ทันทีในแต่ละหัวข้อ

### Approach 2: Linear 4-Block Macro Flow (REJECTED)
- แบ่งทั้งคาบเป็น 4 ช่วง: รวมทฤษฎีทั้งหมด ➔ รวมสูตรทั้งหมด ➔ รวมข้อมูลจริง ➔ รวม AI Prompt
- **ข้อเสีย:** ผู้เรียนไม่มีพื้นฐานจะสะดุดหนักในช่วงรวมสูตร และลืมบริบททางธุรกิจเมื่อถึงช่วง AI Prompting

### Approach 3: Micro-Stepped Storytelling (REJECTED)
- แตกย่อยเป็น 40+ สไลด์ สไลด์ละประเด็นเล็กมาก
- **ข้อเสีย:** เนื้อหากระจัดกระจาย ไม่กระชับ และเกินเวลาการสอน 3 ชั่วโมง

---

## 4. Detailed Slide Blueprint (Session 10: 28 Slides Total)

### Opening & Framework (Slides 1 - 3)
- **Slide 1:** Title Slide (ตามมาตรฐาน Session 3 สัดส่วน 16:10, Badges, Header 2.2em, อาจารย์ผู้สอน)
- **Slide 2:** Recap & 5-Step Data Science Life Cycle (Highlight ขั้นที่ 4: ANALYZE, เชื่อมโยง Session 8-9 สู่ Session 10)
- **Slide 3:** Session Roadmap (4 เสาหลัก: 1. ปัญหา Mass Marketing 2. RFM Mastery 3. What-If Simulation 4. AI Strategic Co-Pilot)

### Part 1: The Entrepreneur's Dilemma & Pareto Principle (Slides 4 - 6)
- **Slide 4:** The Core Question: ทำไม Mass Marketing ถึงใช้ไม่ได้ผลกับธุรกิจยุคใหม่?
- **Slide 5:** กฎ Pareto 80/20 ในมุมมองเจ้าของธุรกิจ (ลูกค้า 20% สร้างกำไร 80%)
- **Slide 6:** Case Study: Pulse Fitness & Pilates Studio (บริบทธุรกิจ สตูดิโอออกกำลังกายระดับพรีเมียม)

### Part 2 (Cycle A): Customer Segmentation via RFM (Slides 7 - 15)
- **Slide 7 [Theory & Data Bridge]:** ถอดรหัสลูกค้าจากบันทึกการขาย (เชื่อมโยง Raw Transactions จาก Session 6A สู่พฤติกรรมลูกค้า)
- **Slide 8 [Theory]:** มิติการแบ่งกลุ่มลูกค้า: Demographic vs Behavioral vs Value-based
- **Slide 9 [Formula & Logic]:** แกน R-F-M (Recency, Frequency, Monetary) และตรรกะการให้คะแนน (Scoring Logic แบบเข้าใจง่าย)
- **Slide 10 [Formula & Spreadsheet]:** การแปลงคะแนนเป็นระดับเกรด (Mental Model: ถังแยกเกรดลูกค้า และตรรกะ `=IFS()`)
- **Slide 11 [Spreadsheet Lab - Pivot Table]:** Pivot Table Visual 3 สเต็ป (ลาก-วาง สรุปยอดลูกค้า 500 คนเป็น 4 Tiers โดยไม่ต้องเขียนสูตร — ตรงตามเกณฑ์ Workshop 5 คะแนน)
- **Slide 12 [Real Dataset & Personas]:** ตารางลูกค้าจริงจาก `session-10-pulse-studio-rfm.csv` และ 4 Customer Personas (2x2 Value-Engagement Matrix)
- **Slide 13 [Data Deep-Dive]:** เจาะลึก Persona 1 & 2: VIP Champions & Loyal Regulars
- **Slide 14 [Data Deep-Dive]:** เจาะลึก Persona 3 & 4: Trial Drop-in & Sleeping Churn Risk
- **Slide 15 [AI Prompt Automation]:** Gemini Prompt: S-E-G-M-E-N-T Template ให้ AI วิเคราะห์ Segment และเขียนข้อความสื่อสารเฉพาะกลุ่มทันที

### Part 3 (Cycle B): What-If Analysis & Scenario Simulation (Slides 16 - 23)
- **Slide 16 [Theory & Bridge]:** What-If Analysis คืออะไร? (Mental Model: ห้องแล็บทดลองธุรกิจก่อนลงเงินจริง พร้อมสะพานเชื่อมโยงความสัมพันธ์ Price vs Demand จาก Session 08)
- **Slide 17 [Formula & Logic]:** กายวิภาคของโมเดลจำลอง (Decision Levers: Price, Volume, Cost, Retention)
- **Slide 18 [Spreadsheet Formula]:** สมการรายได้และตรรกะการคำนวณ Sensitivity บน Spreadsheet
- **Slide 19 [Real Dataset - Case 1]:** จำลองกรณีที่ 1: ขึ้นราคาคอร์ส VIP 20% (ผลกระทบต่อ Volume และ Net Revenue บนข้อมูลจริง)
- **Slide 20 [Real Dataset - Case 2]:** จำลองกรณีที่ 2: เปิดคลาส Off-Peak ลดราคา 40% (Utilization vs Margins)
- **Slide 21 [Real Dataset - Case 3]:** จำลองกรณีที่ 3: แคมเปญปลุกชีพ Sleeping Members (Win-back ROI)
- **Slide 22 [AI Prompt Automation]:** Gemini What-If Simulator: Prompt สั่ง AI จำลองฉากทัศน์ Best/Worst Case
- **Slide 23 [AI Sanity Check]:** Human-in-the-Loop: 3 กฎเหล็กตรวจสอบผลลัพธ์จำลองของ AI ก่อนตัดสินใจ

### Part 4: Integration, Decision Matrix & Workshop (Slides 24 - 28)
- **Slide 24:** Executive Action Matrix: กลยุทธ์แบบ Tailored Strategy สำหรับลูกค้าทั้ง 4 กลุ่ม
- **Slide 25:** 5 กฎทองของการวิเคราะห์ลูกค้าและการจำลองสถานการณ์สำหรับผู้ประกอบการ
- **Slide 26:** Quizizz Arena: สรุปความพร้อมและเตรียมตัวทดสอบ
- **Slide 27:** Workshop Brief: ภารกิจ "Pulse Studio Strategy Master" & บทบาทในทีม (สอดคล้องกับ Role 1-4)
- **Slide 28:** Workshop Rubric & Deliverables: เกณฑ์การให้คะแนน 20 คะแนนเต็ม (รวม Pivot Table 5 คะแนน)

*(โครงสร้างสมบูรณ์ 28 สไลด์ เรียงลำดับต่อเนื่อง 1 ถึง 28)*

---

## 5. Learner Reviewer Agent Specification

### Persona & System Prompt
- **Role:** Non-Technical Entrepreneurship Student Reviewer
- **Mindset:** 
  - "ฉันเป็นเจ้าของธุรกิจมือใหม่ ไม่เคยเขียนโค้ด เกลียดสูตรคณิตศาสตร์ยาวๆ"
  - "ฉันต้องการเข้าใจทันทีว่าทำไมต้องทำสิ่งนี้ และเอาไปเพิ่มกำไรให้ธุรกิจได้อย่างไร"
- **Inspection Checklist:**
  1. *Jargon & Clarity:* มีคำศัพท์เทคนิคที่ไม่ได้อธิบายล่วงหน้าหรือไม่?
  2. *Mental Models:* ภาพประกอบ แผนผัง และการเปรียบเทียบ เข้าใจง่ายเห็นภาพทันทีหรือไม่?
  3. *Formula Intuitiveness:* สูตรอธิบายเป็นภาษามนุษย์เข้าใจง่ายหรือไม่? เชื่อมกับตาราง CSV จริงไหม?
  4. *AI Prompt Usability:* Prompt ที่ให้ไป สามารถ Copy-Paste แล้วนำไปใช้งานได้จริงหรือไม่?
  5. *Layout & Readability:* มีข้อความอัดแน่นเกินไป หรือสไลด์หน้าใดที่รู้สึกเหนื่อยล้าในการอ่านหรือไม่?

---

## 6. Implementation & Verification Workflow

```
[Phase 1: Pre-Edit Backup]
    │
    ▼
[Phase 2: Presentation Deck Drafting & Refactoring] (session-10-presentation.html)
    │
    ▼
[Phase 3: Automated Layout & Responsive Verification] (test-presentation.html on 1280x800)
    │
    ▼
[Phase 4: Learner Agent Review Subagent Execution]
    │
    ├──> Needs Refinement ──> Refine Slides ──> Re-test Layout
    │
    └──> APPROVED (100% Student-Friendly)
            │
            ▼
[Phase 5: Quiz & Sync Pipeline] (session-10-quiz.md ──> session-10-quiz.xlsx)
            │
            ▼
[Phase 6: Git Stage, Commit & Push]
```
