# Courseware Upgrade Design: Session 11 (Data Storytelling & Executive Pitching)

**Date:** 2026-10-24  
**Target:** `session/session-11/session-11-presentation.html`  
**Course:** Fundamentals of Data Science (พื้นฐานวิทยาการข้อมูล)  
**Target Audience:** Entrepreneurship Students (No coding / IT / advanced math background)  

---

## 1. Pedagogical Flow Architecture (4-Step Learning Structure)
Every concept in Session 11 strictly follows the 4-step progressive learning structure:
`[1. ทฤษฎีและหลักการคิด] ➔ [2. สูตรคำนวณและตรรกะแบบง่าย] ➔ [3. ตัวอย่างการใช้กับชุดข้อมูลจริง AuraSkin Lab] ➔ [4. Prompt สั่ง AI คำนวณ/วิเคราะห์แทน]`

### Four Thematic Cycles:
1. **Cycle 1: The Narrative Core & The Stakes (Slides 4–7)**
   - Theory: The Last Mile Problem & Data Dump vs Data Storytelling.
   - Case Study: AuraSkin Lab (9.24M THB revenue, 4,200 orders, 1M THB Facebook conflict).
   - Core Framework: The C-I-A Framework (Context ➔ Insight ➔ Action).
   - Formula: ROAS ($\text{Revenue} / \text{Ad Spend}$) and Break-even ROAS ($1 / \text{Gross Margin}$).
2. **Cycle 2: Business & Marketing Math (Slides 8–12)**
   - Formula: CAC ($\text{Ad Spend} / \text{New Customers}$).
   - Real Data Table: 3 Marketing Channels (TikTok ROAS 4.8x, CAC 160 ฿ vs FB ROAS 1.2x, CAC 540 ฿).
   - Formula: Hero SKU & Repeat Purchase Rate in 60 days + Profit Contribution %.
   - Real Data Table: 4 SKUs (Centella Serum 72% profit share, 42% repeat rate).
   - AI Master Prompt: Gemini ROAS, CAC, Break-even & Hero SKU Audit.
3. **Cycle 3: What-If Simulation & Actionable Proposal (Slides 13–15)**
   - Logic & Formula: What-If Scenarios (Dumping 1M in FB loses -460k THB vs Shifting 400k to TikTok gains +656k THB net profit / +35% profit growth).
   - Real Data Plan: 90-Day Action Plan (Phase 1 Stop Bleeding ➔ Phase 2 50 Micro-KOLs ➔ Phase 3 Shopee Repeat Retargeting).
   - AI Master Prompt: Gemini What-If Sensitivity & The Ask Generator.
4. **Cycle 4: Slide Design Rules & Executive Pitching (Slides 16–28)**
   - Design Rules: One Slide One Message, Action Titles (5-Second Rule), Signal-to-Noise Ratio, Strategic Color Contrast.
   - Anti-Traps: The 4 Deadly Presentation Traps & Fixes + Before/After Transformation.
   - Executive Pitching: BLUF Principle (Bottom-Line Up Front), 3-Minute Elevator Pitch Formula (180 seconds).
   - Blueprint: 7-Slide Master Deck Template & AuraSkin 7-Slide Showcase.
   - AI Co-Pilot: 3-Minute BLUF Script Generator & Tough Q&A Investor Stress-Test.
   - Quality Gates: 5-Point Pitch Readiness Checklist, Summary, Quizizz Arena, Workshop Brief.

---

## 2. Technical & Layout Specifications
- **Aspect Ratio:** 16:10 default (`1280x800`), toggled to 16:9 (`1280x720`) on key 'A'.
- **Slide Count:** Exactly 28 slides.
- **Continuous Slide Comments:** `<!-- SLIDE 1: ... -->` through `<!-- SLIDE 28: ... -->`.
- **Layout Test Result:** 28/28 Passed (100% PASS rate, 0 overflow) on both 16:10 and 16:9 Playwright automated audits.
- **Learner Subagent Review:** Official verdict `APPROVED: Ready for non-tech students` (10/10).

---

## 3. Synchronized Quizizz Quiz
- Updated `session/session-11/session-11-quiz.md` with 10 questions covering Break-even ROAS, CAC, Hero SKU repeat rate, What-If simulation, BLUF, and 7-Slide Master Deck.
- Successfully compiled into `session/session-11/session-11-quiz.xlsx` via `quiz_to_xlsx.ps1`.
