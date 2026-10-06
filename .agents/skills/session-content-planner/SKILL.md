---
name: session-content-planner
description: >-
  Mandatory research & content planning pipeline for creating new teaching session materials.
  Activate BEFORE writing any new session documents (presentation, teaching guide, workshop, quiz).
  Ensures new content aligns with the course syllabus and builds upon knowledge from all prior sessions
  without duplicating use cases.
---

# Session Content Planner — คู่มือวางแผนเนื้อหาการสอนครั้งใหม่

Skill นี้กำหนด **ขั้นตอนบังคับ (Mandatory Pipeline)** ที่ต้องทำ **ก่อนเริ่มเขียนเอกสารการสอนในทุก session ใหม่** เพื่อให้เนื้อหามีความต่อเนื่อง สอดคล้องกับแผนการสอน และอ้างอิงหลักการจากครั้งก่อนหน้าอย่างเป็นระบบ

---

## ⛔ เงื่อนไขการ Activate (Trigger Condition)

Skill นี้ **ต้อง activate ทุกครั้ง** เมื่อได้รับคำสั่งให้:
- สร้างเอกสาร session ใหม่ (session-XX ที่ยังไม่เคยมี)
- สร้าง presentation, teaching guide, workshop, หรือ quiz ของ session ใหม่

> **ห้ามข้ามขั้นตอนใน Skill นี้เด็ดขาด** — ต้องทำครบทุก Step ก่อนเริ่มเขียนเนื้อหา

---

## 📋 Mandatory Research Pipeline (4 ขั้นตอน)

### Step 1: อ่านแผนการสอนหลัก (Syllabus Reference)

**ไฟล์อ้างอิง:** `fundamentals-of-data-science-v6.md` (อยู่ที่ root ของ workspace)

ขั้นตอน:
1. เปิดอ่านไฟล์ `fundamentals-of-data-science-v6.md`
2. ค้นหาข้อมูลของ **session ที่จะสร้าง** (ครั้งที่ XX) จากตาราง "แผนการสอนรายครั้ง":
   - **หัวข้อ** ของ session
   - **Module** ที่ session นี้อยู่
   - **เนื้อหาหลัก** ที่ต้องครอบคลุม
   - **Quiz Game / ปฏิบัติ** ที่กำหนดไว้
3. ระบุ **ตำแหน่งในวงจร Data Science 5 ขั้นตอน** (ASK → COLLECT → PREPARE → ANALYZE → ACT) ว่า session นี้อยู่ที่ขั้นใด
4. ตรวจสอบ **ความเชื่อมโยงกับ session ก่อนหน้าและ session ถัดไป** ตาม syllabus เพื่อวางเนื้อหาให้ต่อเนื่อง

**ผลลัพธ์ Step 1:**
- หัวข้อหลักของ session ใหม่
- ขั้นตอน Data Science ที่เกี่ยวข้อง
- เนื้อหาหลักตาม syllabus
- กิจกรรม Quiz/Workshop ที่กำหนดไว้

---

### Step 2: อ่านสไลด์การสอนครั้งก่อนหน้าทั้งหมด (Prior Sessions Scan)

**ไฟล์อ้างอิง:** `session/session-XX/session-XX-presentation.html` ของทุก session ที่สร้างเสร็จแล้ว

ขั้นตอน:
1. ค้นหาทุกโฟลเดอร์ `session/session-XX/` ที่มีอยู่แล้ว (ไม่รวม session ที่จะสร้างใหม่)
2. **อ่านไฟล์ `session-XX-presentation.html` ของทุก session ก่อนหน้า** ทีละไฟล์
3. จากแต่ละ presentation ให้ดึงข้อมูลต่อไปนี้:

#### 3.1 Key Concepts (หลักการ/นิยาม/คำศัพท์สำคัญ)
สิ่งที่ต้องดึง:
- นิยามและคำจำกัดความสำคัญ (เช่น Data Science 5 ขั้นตอน, 4 ระดับการวิเคราะห์, Tidy Data, Correlation ≠ Causation)
- กรอบแนวคิด/โมเดล (เช่น ASK Framework, Hypothesis Thinking, PDPA)
- คำศัพท์เทคนิคที่สอนไปแล้ว (เช่น Structured/Unstructured Data, Primary/Secondary Data)
- สูตร/เครื่องมือที่แนะนำไปแล้ว (เช่น Google Sheets functions, Gemini Prompt patterns)

#### 3.2 Recap-worthy Items (สิ่งที่ควรทบทวนใน session ใหม่)
- Concept ที่เป็น prerequisite ของเนื้อหาใหม่
- ทักษะที่นักศึกษาต้องใช้ต่อเนื่อง
- ความเข้าใจที่ต้องตอกย้ำก่อนเรียนเนื้อหาใหม่

#### 3.3 Use Cases ที่เคยใช้แล้ว (Anti-Duplication List)
- จดรายการ **กรณีศึกษา/ตัวอย่างธุรกิจ** ที่เคยใช้ในแต่ละ session (เช่น ร้านกาแฟ Arabica Craft, ร้านชาไข่มุกบางแสน)
- **ห้ามนำ use case เหล่านี้มาใช้ซ้ำ** ใน session ใหม่
- ใช้ได้เฉพาะ **หลักการ/concept** ที่ได้จาก use case เหล่านั้น

**ผลลัพธ์ Step 2:**
- รายการ Key Concepts จากทุก session ก่อนหน้า
- รายการ Recap-worthy items
- รายการ Use Cases ที่ห้ามซ้ำ (Anti-Duplication List)

---

### Step 3: สร้าง Session Content Brief

รวบรวมผลลัพธ์จาก Step 1 และ Step 2 เป็น **Content Brief** สำหรับ session ใหม่ (เก็บไว้เป็น context ภายใน ไม่ต้องบันทึกเป็นไฟล์แยก):

```
═══════════════════════════════════════════════════
📋 SESSION CONTENT BRIEF — Session XX
═══════════════════════════════════════════════════

📌 จาก Syllabus:
- หัวข้อ: [หัวข้อจาก syllabus]
- Module: [Module X]
- ขั้นตอน Data Science: [ขั้นที่ X 'XXX']
- เนื้อหาหลัก: [รายการจาก syllabus]
- Quiz/Workshop: [กิจกรรมที่กำหนดไว้]

🔗 Knowledge Bridge (เชื่อมจาก session ก่อนหน้า):
- [Session 01] → อ้างอิง: [concept/หลักการที่ต้อง recap]
- [Session 02] → อ้างอิง: [concept/หลักการที่ต้อง recap]
- ...
- ทักษะ prerequisite: [ทักษะที่ต้องมีก่อนเรียนเนื้อหาใหม่]

⚠️ Anti-Duplication List (use case ที่ห้ามซ้ำ):
- [Session 01]: [use case 1], [use case 2], ...
- [Session 02]: [use case 1], [use case 2], ...
- ...

💡 แนวทางการเชื่อมโยง:
- Recap slide: [สิ่งที่ต้องทบทวนในสไลด์เปิดเรื่อง]
- Callback ระหว่างเนื้อหา: [จุดที่ควรอ้างอิงกลับ]
- Workshop linkage: [วิธีเชื่อม Workshop กับความรู้เดิม]
═══════════════════════════════════════════════════
```

---

### Step 4: ส่งต่อ Content Brief ให้กระบวนการสร้างเอกสาร

เมื่อ Content Brief พร้อมแล้ว ให้นำไปใช้เป็น **input หลัก** ในการเขียนเอกสารทุกชิ้น:

| เอกสาร | วิธีใช้ Content Brief |
|:---|:---|
| `session-XX-presentation.html` | **บังคับโครงสร้าง 3 สไลด์เปิดเรื่อง:**<br>• **Slide 1 (Title):** ดีไซน์สไตล์เดียวกับ Session 3 (พื้นหลัง radial-gradient, ป้าย badge 2 ป้าย, หัวข้อใหญ่ 2 บรรทัด, ชื่อวิชาสี secondary, ป้ายผู้สอนทรง Pill)<br>• **Slide 2 (Recap & Connection):** เชื่อมโยงวงจร Data Science 5 ขั้นตอน (ASK → COLLECT → PREPARE → ANALYZE → ACT) เสมอ ก่อนเข้าสู่เนื้อหาบทเรียน (แถบ `step-container` แสดง 5 ขั้นตอนพร้อม Highlight ขั้นประจำคาบ, การ์ดเปรียบเทียบคาบที่แล้ว vs คาบนี้, และกล่องเน้นย้ำ GIGO)<br>• **Slide 3 (Session Roadmap):** แผนที่การเรียนรู้สรุปหัวข้อสำคัญประจำคาบ ก่อนเข้าสู่เนื้อหาหลักใน Slide 4 |
| `session-XX-teaching-guide.md` | ระบุ Knowledge Bridge และ Recap items ในส่วนวัตถุประสงค์และ Timeline (ตรงกับ Slide Mapping 1–3) |
| `session-XX-workshop-worksheet.md/.html` | โจทย์ Workshop ต้องเชื่อมกับทักษะ/ความรู้จาก session ก่อนหน้า |
| `session-XX-quiz.md` | ข้อสอบอาจมี 1-2 ข้อที่ทดสอบการเชื่อมโยงความรู้ข้ามคาบ |

---

## 🔑 หลักการ Cross-Session Knowledge Linking

### ✅ สิ่งที่ต้องทำ (DO)
1. **อ้างอิงหลักการ/concept** จาก session ก่อน เช่น "จากที่เราเรียน 5 ขั้นตอน Data Science ในครั้งที่ 1..."
2. **ใช้ Callback phrases** เช่น "จำได้ไหมว่าในครั้งที่ 2 เราพูดถึง Hypothesis Thinking..."
3. **สร้างสไลด์ Recap สั้น ๆ** (1-2 สไลด์) ตอนเปิดเรื่องเพื่อเชื่อมจากครั้งก่อน
4. **ใช้ภาษาที่สะท้อนความต่อเนื่อง** เช่น "ต่อจากครั้งที่แล้ว วันนี้เราจะก้าวไปขั้นถัดไป..."
5. **Workshop ต้องต่อยอด** — ถ้าครั้งก่อนทำ Data Map ครั้งนี้อาจใช้ข้อมูลจาก Data Map นั้นมาทำ Data Cleaning

### ❌ สิ่งที่ห้ามทำ (DON'T)
1. **ห้าม copy use case/กรณีศึกษาเดิม** — ห้ามเอาร้านกาแฟชื่อเดียวกัน ตัวเลขเดียวกันมาใช้ซ้ำ
2. **ห้ามทำเนื้อหาแบบ standalone** — ทุก session ต้องมีส่วนที่เชื่อมกลับไปยังความรู้เดิม
3. **ห้ามทบทวนมากเกินไป** — Recap ควรกระชับ (1-2 สไลด์, ไม่เกิน 5 นาที) ไม่ใช่สอนซ้ำ
4. **ห้ามใช้ศัพท์ใหม่โดยไม่เชื่อมกับศัพท์เดิม** — ถ้ามีคำศัพท์ใหม่ ควรเชื่อมกับคำศัพท์ที่เคยเรียนไปแล้ว

---

## 📊 ตัวอย่างการเชื่อมโยง (Examples)

### ตัวอย่าง 1: Session 04 (Tidy Data & Google Forms)
- **Recap จาก Session 03:** "ครั้งที่แล้วเราเรียนเรื่องประเภทข้อมูล (Structured vs Unstructured) และแหล่งข้อมูลธุรกิจ — วันนี้เราจะมาเรียนรู้วิธีจัดเก็บข้อมูลเหล่านั้นให้เป็นระบบ"
- **Knowledge Bridge:** concept ข้อมูล Structured → นำไปสู่ Tidy Data (โครงสร้างที่ถูกต้อง)
- **Workshop linkage:** ใช้ Data Map จากครั้งที่ 3 มาเป็น input ในการออกแบบ Google Forms

### ตัวอย่าง 2: Session 06 (Prompt Engineering with Gemini)
- **Recap จาก Session 01-05:** "ตลอด 5 ครั้งที่ผ่านมา เราครบ 3 ขั้นตอนแรก (ASK, COLLECT, PREPARE) แล้ว — วันนี้เราเข้าสู่ขั้นที่ 4 'ANALYZE' ด้วย AI"
- **Knowledge Bridge:** สมมติฐานจาก ASK (Session 02) + ข้อมูลที่ Clean แล้วจาก PREPARE (Session 05) → นำมาให้ Gemini วิเคราะห์
- **Workshop linkage:** อัปโหลดข้อมูลที่ทำความสะอาดจาก Session 05 ให้ Gemini วิเคราะห์

---

## ⚡ Quick Checklist ก่อนเริ่มเขียนเอกสาร Session ใหม่

- [ ] อ่าน `fundamentals-of-data-science-v6.md` แล้ว
- [ ] อ่าน presentation ของทุก session ก่อนหน้าแล้ว
- [ ] ดึง Key Concepts จากทุก session ก่อนหน้าแล้ว
- [ ] สร้าง Anti-Duplication List (use case ที่ห้ามซ้ำ) แล้ว
- [ ] วาง Knowledge Bridge (จุดเชื่อมจากครั้งก่อน → ครั้งใหม่) แล้ว
- [ ] มี Content Brief ครบถ้วนพร้อมเริ่มเขียนแล้ว
