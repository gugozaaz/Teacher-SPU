# Session 10 Courseware Upgrade & Learner Review Loop Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Upgrade `session-10-presentation.html` into a highly visual, 28-slide progressive learning deck for non-technical entrepreneurship students, verified by an autonomous Learner Reviewer subagent and 16:10 layout tests, followed by synchronized quiz generation and Git push.

**Architecture:** A 4-step progressive learning architecture `[Theory & Concept ➔ Formula & Logic ➔ Real Data ➔ AI Prompt]` implemented across two core cycles (Cycle A: RFM Segmentation & Pivot Tables, Cycle B: What-If Simulation & Levers). Quality is assured via an automated 16:10 headless layout test runner and an autonomous non-tech entrepreneur Learner Subagent loop.

**Tech Stack:** Reveal.js 5.1, HTML5/CSS3 (Noto Sans Thai, Outfit, FontAwesome 6.5), PowerShell 7+, Node.js/Headless Chrome, Git.

**Spec:** [docs/superpowers/specs/2026-10-24-session-10-courseware-upgrade-design.md](file:///d:/GoogleDrive/VibeCoding/teacher/docs/superpowers/specs/2026-10-24-session-10-courseware-upgrade-design.md)

## Global Constraints
- Target aspect ratio: 16:10 (`width: 1280, height: 800`, `margin: 0.04`), with responsive switch to 16:9 (`1280x720`).
- Presentation must pass 16:10 layout test with 100% PASS rate and 0px vertical overflow (content height <= 800px).
- HTML comment standard: `<!-- SLIDE X: [SLIDE_NAME] -->` with continuous 1-based numbering (Slide 1 to 28).
- Mandatory pre-edit backup: Create `session-10-presentation-Backup-YYYYMMDD-HHMM.html` before modifying presentation.
- Synchronize quiz: Must update `session-10-quiz.md` (10 questions covering new 28-slide content) before compiling to `session-10-quiz.xlsx`.
- Non-goals: Do NOT touch or generate `session-10-teaching-guide.md`, `session-10-workshop-worksheet.*`, or PDF.
- Final step: Git stage all, commit with descriptive message, and push to `origin main`.

## Review Focus
1. **Vertical Overflow in 16:10 (1280x800):** If content exceeds 800px height, scrollbars appear in Reveal.js slides.
2. **Formula Intimidations:** Mathematical formulas or `=IFS()` syntax appearing without clear visual metaphors.
3. **Data Discrepancy:** Inconsistencies between Pulse Studio CSV (`session-10-pulse-studio-rfm.csv`) numbers and slide tables.
4. **Broken Presentation Controls:** Loss of keyboard controls, aspect ratio switch HUD toast, or Reveal.js initialization errors.
5. **Quiz-Slide Desynchronization:** Quiz questions referencing obsolete slide topics or missing questions for newly added Pivot Table / What-If cases.

---

### Task 1: Mandatory Pre-Edit Slide Backup

**Files:**
- Create: `session/session-10/session-10-presentation-Backup-20261024-1745.html`
- Read: `session/session-10/session-10-presentation.html`

**Interfaces:**
- Consumes: Current `session-10-presentation.html`
- Produces: Timestamped backup copy preserving existing work

- [ ] **Step 1: Check current timestamp and format backup filename**
  Ensure filename matches `session-10-presentation-Backup-YYYYMMDD-HHMM.html`.
- [ ] **Step 2: Copy `session-10-presentation.html` to backup path**
  Execute file copy via PowerShell or read/write tool.
- [ ] **Step 3: Verify backup file exists and matches size**
  Run `Get-Item session/session-10/session-10-presentation-Backup-*.html` and verify identical size.

---

### Task 2: Presentation Deck Refactoring (28 Slides)

**Files:**
- Modify: `session/session-10/session-10-presentation.html`
- Reference: `session/session-10/session-10-pulse-studio-rfm.csv`
- Reference: `session/session-6a/session-6a-coffee-sales-crm.csv`
- Reference: `session/session-08/session-08-coffee-sales-correlation.csv`

**Interfaces:**
- Consumes: 28-slide blueprint from Spec Section 4
- Produces: Upgraded 28-slide HTML presentation with continuous numbering and visual models

- [ ] **Step 1: Update Opening & Framework Slides (Slides 1 - 3)**
  - Slide 1: Title slide with badge 1/2569, ครั้งที่ 10 / 14, standard pill author badge.
  - Slide 2: Recap & 5-Step Data Science Life Cycle (highlighting Step 4: ANALYZE).
  - Slide 3: Roadmap (4 pillars: Mass Marketing vs Segmentation, RFM & Pivot Tables, What-If Simulation Levers, AI Strategy Co-Pilot).
- [ ] **Step 2: Refactor Part 1: The Entrepreneur's Dilemma (Slides 4 - 6)**
  - Slide 4: Why Mass Marketing fails (comparison card: Blanket Blast vs Precision Targeting).
  - Slide 5: Pareto 80/20 in Business (visual distribution diagram showing top 20% delivering 80% revenue).
  - Slide 6: Case Study: Pulse Fitness & Pilates Studio (business profile, boutique fitness context).
- [ ] **Step 3: Implement Cycle A: RFM Segmentation & Pivot Tables (Slides 7 - 15)**
  - Slide 7: From Raw Transactions (Session 6A Coffee CRM) to Customer RFM profile.
  - Slide 8: 3 Dimensions of Segmentation (Demographic vs Behavioral vs Value-based).
  - Slide 9: RFM Framework (Recency: วันที่ซื้อล่าสุด, Frequency: ความถี่, Monetary: ยอดเงินรวม).
  - Slide 10: Scoring Logic & Tier Buckets (Grading mental model + spreadsheet logic `=IFS()`).
  - Slide 11: Spreadsheet Lab: Pivot Table 3-Step Drag-and-Drop (Rows: Tier, Values: Count & Sum Revenue — aligning with Workshop Role 2).
  - Slide 12: Real Dataset & 4 Personas 2x2 Matrix (Champions, Regulars, Drop-ins, Sleeping).
  - Slide 13: Deep-Dive Personas 1 & 2: VIP Champions & Loyal Regulars (profiles & retention playbook).
  - Slide 14: Deep-Dive Personas 3 & 4: Trial Drop-in & Sleeping Churn Risk (profiles & re-engagement).
  - Slide 15: Gemini Prompt: S-E-G-M-E-N-T Template for automated customer tiering and personalized messaging.
- [ ] **Step 4: Implement Cycle B: What-If Analysis & Levers (Slides 16 - 23)**
  - Slide 16: What-If Analysis Concept & Session 08 Correlation Bridge (Price vs Volume elasticity).
  - Slide 17: Anatomy of a What-If Model (4 Levers: Price, Volume, Variable Cost, Churn Rate).
  - Slide 18: Spreadsheet Sensitivity Logic & Formula (`New Revenue = Price * (1 + %change) * Volume * (1 + %change)`).
  - Slide 19: Case 1: Raising VIP Class Prices by 20% (+20% Price, -5% Churn = +14% Net Revenue).
  - Slide 20: Case 2: Off-Peak Midday Class at 40% Discount (Capacity utilization boost).
  - Slide 21: Case 3: Sleeping Member Win-Back Campaign (SMS promo ROI).
  - Slide 22: Gemini What-If Simulator Prompt (Stress-testing best, base, worst scenarios).
  - Slide 23: Human-in-the-Loop: 3 Sanity Checks on AI What-If output.
- [ ] **Step 5: Implement Part 4: Executive Synthesis & Workshop (Slides 24 - 28)**
  - Slide 24: Executive Action Matrix (Tailored action playbook across 4 segments).
  - Slide 25: 5 Golden Rules of Customer Analytics for Entrepreneurs.
  - Slide 26: Quizizz Arena Challenge briefing.
  - Slide 27: Workshop Mission: "Pulse Studio Strategy Master" & Team Roles (Roles 1-4).
  - Slide 28: Workshop Rubric & Deliverables (20 points total, explicitly including 5 pts for Pivot Table).
- [ ] **Step 6: Verify slide comments and continuous numbering**
  Verify `<!-- SLIDE 1: ... -->` through `<!-- SLIDE 28: ... -->` exist without gaps or duplicates.

---

### Task 3: Layout & Responsive Verification on 16:10 (1280x800)

**Files:**
- Read/Test: `session/session-10/session-10-presentation.html`
- Test Runner: `session/session-10/test-presentation.html`

**Interfaces:**
- Consumes: Refactored `session-10-presentation.html`
- Produces: Layout verification test report with pass/fail metrics for all 28 slides

- [ ] **Step 1: Check `test-presentation.html` iframe configuration**
  Ensure test runner points to `session-10-presentation.html` and targets 1280x800.
- [ ] **Step 2: Run automated headless browser test on 1280x800**
  Execute headless Chrome or test script to measure `scrollHeight` vs `clientHeight` for all 28 slides.
- [ ] **Step 3: Confirm 100% PASS rate (0 overflows, content height <= 800px)**
  Inspect any slide with height > 800px or negative margin and adjust font size/padding until PASS.

---

### Task 4: Learner Reviewer Subagent Execution & Feedback Loop

**Files:**
- Read: `session/session-10/session-10-presentation.html`
- Subagent Role: "Non-Technical Entrepreneurship Student Reviewer"

**Interfaces:**
- Consumes: Verified 28-slide presentation deck
- Produces: Detailed feedback report on clarity, pedagogical flow, formula intimidation, and data consistency

- [ ] **Step 1: Dispatch Learner Subagent with Student Persona prompt**
  Prompt subagent to evaluate:
  1. *Jargon & Clarity:* Any unexplained data terms?
  2. *4-Step Flow:* Does each cycle cleanly follow Theory ➔ Formula ➔ Real Data ➔ AI Prompt?
  3. *Formula Intuitiveness:* Are formulas explained with relatable business logic?
  4. *Pivot Table Utility:* Is Slide 11 clear and easy for a beginner to follow?
  5. *Data Accuracy:* Do numbers in Pulse Studio cases match expected math?
- [ ] **Step 2: Collect Subagent findings and categorize feedback**
  Identify any slides where the student persona feels confused or overwhelmed.
- [ ] **Step 3: Apply slide refinements (if any issues raised)**
  Modify targeted slides to simplify language, add diagrams, or refine copy.
- [ ] **Step 4: Re-evaluate until Learner Subagent awards approval**
  Confirm subagent gives full sign-off ("APPROVED: Ready for non-tech students").

---

### Task 5: Quiz Synchronization Pipeline (`session-10-quiz.md` & `.xlsx`)

**Files:**
- Modify: `session/session-10/session-10-quiz.md`
- Output: `session/session-10/session-10-quiz.xlsx`
- Script: `.agents/skills/document-processor/scripts/quiz_to_xlsx.ps1`

**Interfaces:**
- Consumes: Final 28-slide presentation deck
- Produces: Synchronized 10-question Quizizz markdown and Excel sheet

- [ ] **Step 1: Audit quiz questions against upgraded 28-slide deck**
  Ensure 10 questions cover:
  - Pareto 80/20 & Mass Marketing limitation
  - RFM dimensions (Recency, Frequency, Monetary)
  - Scoring and `=IFS()` grading
  - Pivot Table for customer summary
  - 4 Customer Personas (Champions, Regulars, Drop-in, Sleeping)
  - What-If Analysis definition & 4 Levers
  - Session 08 Price vs Volume correlation connection
  - Sensitivity formula & net revenue calculation
  - Gemini AI Prompting for Segmentation / Simulation
  - Human-in-the-Loop validation
- [ ] **Step 2: Edit and save `session-10-quiz.md`**
  Write complete 10-question quiz with 3 options (A, B, C), correct answers, and thorough Thai explanations referencing slide names.
- [ ] **Step 3: Convert `session-10-quiz.md` to `session-10-quiz.xlsx`**
  Run:
  ```powershell
  powershell -ExecutionPolicy Bypass -File ".\.agents\skills\document-processor\scripts\quiz_to_xlsx.ps1" -InputMarkdown ".\session\session-10\session-10-quiz.md"
  ```
- [ ] **Step 4: Verify generated `.xlsx` file exists and is valid**
  Ensure `session-10-quiz.xlsx` is created and non-empty.

---

### Task 6: Automated Git Commit & Push

**Files:**
- Modified/Created files in `session/session-10/` and `docs/superpowers/`

**Interfaces:**
- Consumes: All completed and verified deliverables
- Produces: Clean Git commit pushed to `origin main`

- [ ] **Step 1: Check git status**
  Run `git status` to verify all changed files.
- [ ] **Step 2: Stage all changes**
  Run `git add -A`.
- [ ] **Step 3: Commit with descriptive message**
  Run `git commit -m "feat(session-10): upgrade courseware to 4-step progressive 28-slide deck with learner review"`.
- [ ] **Step 4: Push to origin main**
  Run `git push origin main`.
- [ ] **Step 5: Report completion and commit hash to user**
  Summarize results and prepare for sequential execution of Session 11.
