# Design Spec: Session 13 Courseware Upgrade (Final Project Coaching & Dry Run Clinic)

## 1. Overview & Context
- **Target Audience:** Entrepreneurship students with no background in IT, coding, or advanced mathematics.
- **Session Topic:** Session 13: Final Project Coaching & Dry Run Clinic (คลินิกตรวจสุขภาพโปรเจกต์ 5 สถานี ปิด 4 กับดักมรณะ ซ้อมใหญ่ 15 นาที และแลกเปลี่ยน Peer Feedback).
- **Core Pedagogical Framework:**
  `[1. ทฤษฎีและหลักการคิด] ➔ [2. สูตรคำนวณและตรรกะแบบง่าย] ➔ [3. ตัวอย่างการใช้กับชุดข้อมูลจริง GreenFresh] ➔ [4. Prompt สั่ง AI คำนวณ/วิเคราะห์แทน]`

## 2. Business Case Study: "GreenFresh Subscription"
- **Business Model:** Organic vegetable & meal-kit monthly delivery startup (1,990 THB/month/subscriber).
- **Baseline Pain Point:** 1,200 active subscribers, but 336 users churned in Month 3 (28% Churn Rate).
- **Data Discovery:** 64% canceled not because of price, but due to "spoilage before cooking" (ผักเน่าคาตู้เย็นกินไม่ทัน).
- **Strategic Solution:** Smart Swap flex menu, Mini Kit box, recipe cards, and proactive WhatsApp/SMS reminder.
- **Pilot Outcome:** Churn reduced to 12% among pilot group, recovering 192 users over 6 months.

## 3. Core Formulas & Arithmetic
1. **Monthly Churn Rate (%):**
   $$\text{Churn Rate (\%)} = \frac{\text{Lost Users}}{\text{Starting Users}} \times 100 = \frac{336}{1200} \times 100 = 28.0\%$$
2. **Customer Lifespan (Months):**
   $$\text{Customer Lifespan} = \frac{1}{\text{Monthly Churn Rate}} = \frac{1}{0.28} \approx 3.57\text{ months}$$
   $$\text{Target Lifespan} = \frac{1}{0.12} \approx 8.33\text{ months (extended by } +4.76\text{ months)}$$
3. **Customer Lifetime Value (LTV):**
   $$\text{LTV} = 1,990\text{ THB} \times \text{Lifespan} \quad (7,104\text{ THB} \rightarrow 16,577\text{ THB, } +9,473\text{ THB gain)}$$
4. **Revenue Recovered (6 Months):**
   $$\text{Recovered Revenue} = 192 \text{ users} \times 1,990\text{ THB} \times 6\text{ months} = 2,292,480\text{ THB}$$
5. **Net Financial Payoff & ROI (%):**
   $$\text{Net Payoff} = 2,292,480 - 450,000 (\text{Smart Swap System Cost}) = +1,842,480\text{ THB}$$
   $$\text{Expected ROI (\%)} = \frac{1,842,480}{450,000} \times 100 = 409.4\% \quad (\text{Payback Period: } 1.2\text{ months})$$

## 4. Architectural Enhancements
- **5-Station Diagnostics:** Station 1 (ASK), Station 2 (PREPARE & PRIVACY), Station 3 (ANALYZE), Station 4 (ACT & STORYTELLING), Station 5 (PITCHING & STAGE).
- **4 Fatal Traps:** Vague ASK, Privacy Breach, Blind AI Hallucination, Zombie Chart Deck.
- **Master Deck Blueprint:** 6-slide executive structure following BLUF (Hook -> Data Diagnosis -> Solution -> Pilot -> Payoff & ROI -> Roadmap).
- **Stage Roles:** 4 C-Suite roles (CEO/Opener, CDO/Data Master, COO/AI Lead, CFO/Closer) with seamless handover cues.
- **Stanford d.school Peer Feedback Protocol:** "I Like / I Wish / What If" structure.
- **Master Rubric Deep-Dive:** 5 dimensions (20% each = 100%, 40% course weight).
- **AI Master Prompts:** 4 ready-to-copy prompts in Gemini for ASK refinement, spreadsheet audit, Churn & Payoff simulation, and tough judge stress-testing.

## 5. Verification & Testing
- Pre-edit backup created (`session-13-presentation-Backup-20261024-1915.html`).
- Playwright layout test at 1280x800 and 1280x720: 28/28 slides PASS (100%).
- Learner Reviewer subagent review: 10.0 / 10.0 (`APPROVED: Ready for non-tech students`).
- Quiz updated: `session-13-quiz.md` and compiled `session-13-quiz.xlsx`.
