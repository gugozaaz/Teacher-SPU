# Courseware Upgrade Design: Session 12 (End-to-End Pipeline & AI Governance)

**Date:** 2026-10-24  
**Target:** `session/session-12/session-12-presentation.html`  
**Course:** Fundamentals of Data Science (พื้นฐานวิทยาการข้อมูล)  
**Target Audience:** Entrepreneurship Students (No coding / IT / advanced math background)  

---

## 1. Pedagogical Flow Architecture (4-Step Learning Structure)
Every concept in Session 12 strictly follows the 4-step progressive learning structure:
`[1. ทฤษฎีและหลักการคิด] ➔ [2. สูตรคำนวณและตรรกะแบบง่าย] ➔ [3. ตัวอย่างการใช้กับชุดข้อมูลจริง FinQuick Lending 10 ร้านค้า] ➔ [4. Prompt สั่ง AI คำนวณ/วิเคราะห์แทน]`

### Four Thematic Cycles:
1. **Cycle 1: The End-to-End Flywheel & Business Mindset (Slides 4–6)**
   - Theory: The Dual Engine (Value Engine vs Governance Shield).
   - Case Study: FinQuick Lending (Digital microfinance for Shopee/TikTok/Lazada sellers; PII leak risk, AI bias, black box).
   - Core Framework: The Data Flywheel (Feedback loop: Data ➔ Insight ➔ Product Action ➔ Better Data).
2. **Cycle 2: Privacy, PDPA & Data Masking (Slides 7–11)**
   - Theory: Data Privacy & PDPA Compliance (5M THB administrative fines, 1-year prison term).
   - The Cardinal Sin: Never dump raw PII (Name, 13-digit ID, Phone) into public LLMs.
   - Formula & Logic: Spreadsheet Masking formulas (`=LEFT(...) & "-XXXX-" & RIGHT(...)`).
   - Real Data Table: 10 applicant stores before and after Masking.
   - AI Master Prompt: Gemini DPO PII & Anonymization Audit.
3. **Cycle 3: Credit Scoring Math & AI Bias Audit (Slides 12–16)**
   - Theory: AI Bias & Historical Discrimination.
   - Financial Formulas: DSR % ($\text{Monthly Debt} / \text{Monthly Revenue} \le 30\%$) & Credit Limit Cap ($\text{Revenue} \times \text{Factor}$).
   - Logic: 100-pt Alternative Credit Risk Scoring (Consistency 30, Review 30, Return Rate 20, Sales 20; Grades A/B/C).
   - Real Data Results: 10 Stores scoring & Bias Parity Check (100% approval parity for female store owners based on 96-99% positive reviews).
   - AI Master Prompt: Gemini CRO Credit Scoring & Bias Audit.
4. **Cycle 4: Explainable AI, 1-Page BLUF & Final Project Launchpad (Slides 17–28)**
   - Theory: Grounding to prevent AI Hallucination + Explainable AI (XAI) Right to Explanation.
   - Real Deliverable: Transparent Decision Letters (APP-01 approval vs APP-04 60-day constructive delay).
   - Blueprint: 1-Page Executive BLUF (490k THB loan approval, 70k THB interest, 0% bias).
   - AI Master Prompt: Gemini XAI Decision Letter & 1-Page BLUF Generator.
   - Governance: 5-Point AI Governance Checklist.
   - Final Project: 4 Roles, 4 Deliverables, 5-Dimension Rubric (100 pts / 40% course weight), 3-Week Timeline, Brainstorming Master Prompt.
   - Wrap-up: 5 Golden Rules, Quizizz Arena, Workshop Brief.

---

## 2. Technical & Layout Specifications
- **Aspect Ratio:** 16:10 default (`1280x800`), toggled to 16:9 (`1280x720`) on key 'A'.
- **Slide Count:** Exactly 28 slides.
- **Continuous Slide Comments:** `<!-- SLIDE 1: ... -->` through `<!-- SLIDE 28: ... -->`.
- **Layout Test Result:** 28/28 Passed (100% PASS rate, 0 overflow) on both 16:10 and 16:9 Playwright automated audits.
- **Learner Subagent Review:** Official verdict `APPROVED: Ready for non-tech students` (10/10 across all 6 criteria).

---

## 3. Synchronized Quizizz Quiz
- Updated `session/session-12/session-12-quiz.md` with 10 questions covering Data Flywheel, AI Bias, DSR calculation, Alternative Credit Scoring, PDPA fines, Data Masking formulas, Grounding, XAI, and 1-Page BLUF.
- Successfully compiled into `session/session-12/session-12-quiz.xlsx` via `quiz_to_xlsx.ps1`.
