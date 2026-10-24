# Implementation Plan: Session 13 Courseware Upgrade

## 1. Goal
Upgrade Session 13 presentation, quiz, and related resources according to the 4-step progressive framework, ensuring zero jargon barrier for non-tech entrepreneurship students, 100% layout pass rate, autonomous subagent certification, and automated quiz synchronization.

## 2. Tasks & Progress
- [x] **Task 1: Pre-Edit Slide Backup**
  - Created `session/session-13/session-13-presentation-Backup-20261024-1915.html`
- [x] **Task 2: Slide Architecture & Modular Generation**
  - Modular scripts created in `scratch/`: `s13_prepare.py`, `s13_part1.py` (Slides 1-6), `s13_part2.py` (Slides 7-11), `s13_part3.py` (Slides 12-16), `s13_part4.py` (Slides 17-28), and `s13_assemble.py`.
  - Assembled `session/session-13/session-13-presentation.html` with 28 slides and formula styling.
- [x] **Task 3: Slide Header Comment Audit**
  - Verified 28 continuous semantic comments from `<!-- SLIDE 1: TITLE SLIDE -->` to `<!-- SLIDE 28: BEST DATA VENTURE AWARD & FINAL SENDOFF -->`.
- [x] **Task 4: Automated Playwright Layout Testing**
  - Executed `s13_layout_test.py`:
    - 16:10 (`1280x800`): 28/28 slides PASS (100.0%)
    - 16:9 (`1280x720`): 28/28 slides PASS (100.0%)
- [x] **Task 5: Autonomous Learner Reviewer Subagent**
  - Subagent `e3a17255-3de1-4f20-95c0-a1f9eb95d840` evaluated 5 criteria: 10.0 / 10.0.
  - Official certification: `APPROVED: Ready for non-tech students`.
- [x] **Task 6: Quiz Synchronization Pipeline**
  - Updated `session/session-13/session-13-quiz.md` with 10 questions reflecting new formulas (Churn Rate, Lifespan, Payoff, ROI) and exact slide header references.
  - Compiled `session/session-13/session-13-quiz.xlsx` via `quiz_to_xlsx.ps1`.
- [x] **Task 7: Documentation & Git Commit / Push**
  - Documented Design Spec and Implementation Plan in `docs/superpowers/`.
  - Stage, commit, and push to remote `origin main`.
