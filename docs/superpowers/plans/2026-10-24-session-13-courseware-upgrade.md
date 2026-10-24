# Implementation Plan: Session 13 Courseware Upgrade (Unlimited Expansion & Thai CSV)

## 1. Goal
Upgrade Session 13 presentation, dataset, and quiz according to the 4-step progressive framework, expanding to 34 slides with breathing room for non-tech entrepreneurship students, providing a dedicated Thai CSV dataset, 100% layout pass rate, autonomous subagent certification (10/10), and automated quiz synchronization.

## 2. Tasks & Progress
- [x] **Task 1: Pre-Edit Slide Backup**
  - Created `session/session-13/session-13-presentation-Backup-20261024-2110.html`
- [x] **Task 2: Thai CSV Dataset Generation**
  - Generated `session/session-13/session-13-greenfresh-subscription-churn-thai.csv` (16 customer rows, 10 columns in UTF-8 with BOM for Excel compatibility) covering subscription churn reasons, Smart Swap pilot, LTV, and NPS.
- [x] **Task 3: Slide Architecture & Unlimited Expansion (34 Slides)**
  - Expanded deck from 28 to 34 slides matching Session 10 design system, CSS variables, fonts, aspect ratio toggle (Key A), and test runner (Key T).
  - Continuous comments `<!-- SLIDE 1: TITLE SLIDE -->` through `<!-- SLIDE 34: COMMENCEMENT & COURSE LEGACY -->`.
  - Step-by-step arithmetic: 1,200 accounts, 28% to 12% churn (-192 churn/mo), $1,036,800 gross profit recovered, Net profit +518,400 ฿ (ROI 100%).
- [x] **Task 4: Automated Playwright Layout Testing**
  - Executed `s13_layout_test.py`:
    - 16:10 (`1280x800`): 34/34 slides PASS (100.0%)
    - 16:9 (`1280x720`): 34/34 slides PASS (100.0%)
- [x] **Task 5: Autonomous Learner Reviewer Subagent**
  - Subagent `5613de48-bfe2-4e5d-ba99-3620f7f7a757` evaluated 5 criteria: 10.0 / 10.0.
  - Official certification: `VERDICT: APPROVED: Ready for non-tech students`.
- [x] **Task 6: Quiz Synchronization Pipeline**
  - Updated `session/session-13/session-13-quiz.md` with 10 questions reflecting the 34 slides and Thai CSV dataset.
  - Compiled `session/session-13/session-13-quiz.xlsx` via `quiz_to_xlsx.ps1`.
- [x] **Task 7: Documentation & Git Commit / Push**
  - Stage, commit, and push to remote `origin main`.
