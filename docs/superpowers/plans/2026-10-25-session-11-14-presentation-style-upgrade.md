# Session 11-14 Presentation Style & Layout Upgrade Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** ปรับปรุง Style การจัดวาง, Typography & Font, และโครงสร้าง Slide 1-2 ในเอกสารการสอน `session-11-presentation.html`, `session-12-presentation.html`, `session-13-presentation.html`, และ `session-14-presentation.html` ให้ได้มาตรฐานเดียวกับ `session-09-presentation.html` และข้อกำหนดของวิชา

**Architecture:** ปรับปรุงระดับ CSS & HTML ในทั้ง 4 ไฟล์: (1) กฎ Typography (Google Fonts 'Noto Sans Thai', 'Outfit', 'Fira Code' พร้อมขนาด rem/line-height/letter-spacing), (2) โครงสร้างสไลด์ที่ 1 (Title Slide: 2-line title, 2 header badges with FontAwesome, instructor pill with university affiliation, vertical centering), (3) โครงสร้างสไลด์ที่ 2 (Recap & Connection: 5-step `step-container` + `step-card` highlight, `grid-2` comparison card with icons, callout box), (4) ปรับปรุง Slide Header (เปลี่ยนจาก `.slide-title-group`/`.slide-title` ที่ไม่มี CSS เป็น `.title-group` + `<h2>` + `.subtitle` และ `.badge-step` อยู่ฝั่งขวา) ทุกสไลด์

**Tech Stack:** HTML5, CSS3 (Vanilla CSS variables), Reveal.js 5.1.0, FontAwesome 6.5.1, Google Fonts

**Spec:** [AGENTS.md](file:///d:/GoogleDrive/VibeCoding/teacher/AGENTS.md) และ [PRESENTATION-CONTROLS.md](file:///d:/GoogleDrive/VibeCoding/teacher/PRESENTATION-CONTROLS.md)

## Global Constraints
- ทุกครั้งก่อนแก้ไขสไลด์ ต้องสร้างไฟล์ Backup ในรูปแบบ `session-XX-presentation-Backup-YYYYMMDD-HHMM.html` ในโฟลเดอร์เดียวกันเสมอ
- สไลด์ใช้อัตราส่วนเริ่มต้น 16:10 (`1280x800`) สลับ 16:9 (`1280x720`) ได้ด้วยปุ่ม `A` พร้อม HUD Toast
- ห้ามมี `.deck-footer` และซ่อน `controls: false`
- Slide Comment ทุกหน้าต้องเรียงหมายเลขต่อเนื่อง `<!-- SLIDE X: [SLIDE_NAME] -->` โดยไม่มีเลขข้ามหรือตกหล่น
- หลังแก้ไขเสร็จสิ้น ต้องซิงค์ควิซ (1.1 md, 1.2 xlsx) และ Git commit & push ขึ้น main เสมอ

## Review Focus
1. **Slide 1 Visual Layout:** ต้องอยู่กึ่งกลางแนวตั้ง ไม่ติดขอบบน ไม่มีเส้นคั่นผิดตำแหน่ง และมีป้ายผู้สอนทรง Pill ขอบมนสวยงาม
2. **Slide 2 Visual Layout:** กล่อง 5 ขั้นตอน ASK->COLLECT->PREPARE->ANALYZE->ACT ต้องแสดงครบ 5 ขั้น และทำ Highlight ขั้นที่ถูกต้อง
3. **Slide Header Typography:** ทุกสไลด์ตั้งแต่ Slide 2 เป็นต้นไป หัวข้อต้องแสดงผลด้วย Font 'Noto Sans Thai'/'Outfit' น้ำหนัก 800 ขนาด 1.40rem พร้อมไอคอนและป้าย Badge ทางขวาอย่างถูกต้อง
4. **No Overflow:** เนื้อหาในแต่ละสไลด์ต้องไม่ล้นกรอบความสูง 800px ในโหมด 16:10
5. **Backup & Git Integrity:** มีไฟล์ Backup ครบทุก session และ commit & push สำเร็จ

---

### Task 1: Backup Files for Sessions 11, 12, 13, and 14

**Files:**
- Create: `session/session-11/session-11-presentation-Backup-20261025-1855.html`
- Create: `session/session-12/session-12-presentation-Backup-20261025-1855.html`
- Create: `session/session-13/session-13-presentation-Backup-20261025-1855.html`
- Create: `session/session-14/session-14-presentation-Backup-20261025-1855.html`

- [ ] **Step 1: Create backup copies of all 4 presentation files**
- [ ] **Step 2: Verify all 4 backup files exist and match file size**

---

### Task 2: Refactor Session 11 Presentation (`session-11-presentation.html`)

**Files:**
- Modify: `session/session-11/session-11-presentation.html`

- [ ] **Step 1: Update CSS in `<style>` to match Session 09 standard**
  - Section padding: `20px 36px 22px 36px !important`
  - `.reveal h2`: `font-size: 1.40rem; line-height: 1.25; letter-spacing: -0.015em;`
  - `.reveal p`: `font-size: 0.94rem; line-height: 1.45;`
  - Robust `.slide-header` styles: `.title-group`/`.slide-title-group` with `order: 1`, `h2`/`.slide-title` styling, `.subtitle`/`.slide-subtitle` styling, and `.badge-step`/`.slide-badge` with `order: 2`
- [ ] **Step 2: Refactor Slide 1 (Title Slide)**
  - Use Session 09 structure with centered container: `<div style="text-align: center; margin: auto 0; padding: 20px 10px;">`
  - Badges: `ภาคเรียนที่ 1/2569` and `ครั้งที่ 11 / 14` with FontAwesome icons
  - Title: 2-line `<h1>` (2.25em, weight 900)
  - Subtitle: `Fundamentals of Data Science (พื้นฐานวิทยาการข้อมูล)`
  - Instructor pill: Pill shape with FontAwesome icon `fa-user-tie` and affiliation "มหาวิทยาลัยศรีปทุม"
- [ ] **Step 3: Refactor Slide 2 (Recap & Connection - Bridge to ACT)**
  - Standard `.slide-header` with `<h2><i class="fas fa-route"></i> วงจร Data Science: ก้าวข้ามสู่ขั้นสุดท้าย 'ACT'</h2>` and `.badge-step`
  - Standard `.step-container` with 5 `.step-card` elements, highlighting `Step 5 ACT (ปัจจุบัน)`
  - Standard `.grid-2` comparison cards with icons: คาบที่แล้ว (Session 10) vs คาบนี้ (Session 11)
  - Standard callout box for golden rule
- [ ] **Step 4: Standardize Slide Headers & Comments throughout Slides 3 to 36**
  - Ensure all slide headers use `<h2>` with FontAwesome icons and `.badge-step` on the right
  - Verify continuous comment numbering `<!-- SLIDE X: [SLIDE_NAME] -->` 1 to 36
- [ ] **Step 5: Verify in browser that Slide 1, Slide 2, and slide typography render correctly**

---

### Task 3: Refactor Session 12 Presentation (`session-12-presentation.html`)

**Files:**
- Modify: `session/session-12/session-12-presentation.html`

- [ ] **Step 1: Update CSS in `<style>` to match Session 09 standard**
  - Section padding: `20px 36px 22px 36px !important`
  - `.reveal h2`: `font-size: 1.40rem; line-height: 1.25; letter-spacing: -0.015em;`
  - `.reveal p`: `font-size: 0.94rem; line-height: 1.45;`
  - Robust `.slide-header` styling for title, subtitle, and badge
- [ ] **Step 2: Refactor Slide 1 (Title Slide)**
  - Use Session 09 structure with centered container
  - Badges: `ภาคเรียนที่ 1/2569` and `ครั้งที่ 12 / 14` with FontAwesome icons
  - Title: 2-line `<h1>` (2.25em, weight 900)
  - Subtitle: `Fundamentals of Data Science (พื้นฐานวิทยาการข้อมูล)`
  - Instructor pill: Pill shape with FontAwesome icon `fa-user-tie` and affiliation "มหาวิทยาลัยศรีปทุม"
- [ ] **Step 3: Refactor Slide 2 (Recap & Connection - Full Pipeline & Governance)**
  - Standard `.slide-header` with `<h2><i class="fas fa-route"></i> วงจร Data Science: บูรณาการ 5 ขั้นตอนอย่างไร้รอยต่อ</h2>` and `.badge-step`
  - Standard `.step-container` with 5 `.step-card` elements, highlighting `Step 5 ACT (ปัจจุบัน)`
  - Standard `.grid-2` comparison cards with icons: คาบ 1-11 vs คาบนี้ (Session 12)
  - Standard callout box for golden rule
- [ ] **Step 4: Standardize Slide Headers & Comments throughout Slides 3 to 34**
  - Ensure all slide headers use `<h2>` with FontAwesome icons and `.badge-step` on the right
  - Verify continuous comment numbering `<!-- SLIDE X: [SLIDE_NAME] -->` 1 to 34
- [ ] **Step 5: Verify in browser that Slide 1, Slide 2, and slide typography render correctly**

---

### Task 4: Refactor Session 13 Presentation (`session-13-presentation.html`)

**Files:**
- Modify: `session/session-13/session-13-presentation.html`

- [ ] **Step 1: Update CSS in `<style>` to match Session 09 standard**
  - Section padding: `20px 36px 22px 36px !important`
  - `.reveal h2`: `font-size: 1.40rem; line-height: 1.25; letter-spacing: -0.015em;`
  - `.reveal p`: `font-size: 0.94rem; line-height: 1.45;`
  - Robust `.slide-header` styling for title, subtitle, and badge
- [ ] **Step 2: Refactor Slide 1 (Title Slide)**
  - Use Session 09 structure with centered container
  - Badges: `ภาคเรียนที่ 1/2569` and `ครั้งที่ 13 / 14` with FontAwesome icons
  - Title: 2-line `<h1>` (2.25em, weight 900)
  - Subtitle: `Fundamentals of Data Science (พื้นฐานวิทยาการข้อมูล)`
  - Instructor pill: Pill shape with FontAwesome icon `fa-user-tie` and affiliation "มหาวิทยาลัยศรีปทุม"
- [ ] **Step 3: Refactor Slide 2 (Recap & Connection - Dry Run Clinic)**
  - Standard `.slide-header` with `<h2><i class="fas fa-route"></i> วงจร Data Science: โค้งสุดท้ายสู่เวทีพิทช์จริง</h2>` and `.badge-step`
  - Standard `.step-container` with 5 `.step-card` elements, highlighting `Step 5 ACT (ปัจจุบัน)`
  - Standard `.grid-2` comparison cards with icons: สัปดาห์ที่ 1–12 vs สัปดาห์นี้ (Session 13)
  - Standard callout box for golden rule
- [ ] **Step 4: Standardize Slide Headers & Comments throughout Slides 3 to 34**
  - Ensure all slide headers use `<h2>` with FontAwesome icons and `.badge-step` on the right
  - Verify continuous comment numbering `<!-- SLIDE X: [SLIDE_NAME] -->` 1 to 34
- [ ] **Step 5: Verify in browser that Slide 1, Slide 2, and slide typography render correctly**

---

### Task 5: Refactor Session 14 Presentation (`session-14-presentation.html`)

**Files:**
- Modify: `session/session-14/session-14-presentation.html`

- [ ] **Step 1: Update CSS in `<style>` to match Session 09 standard**
  - Section padding: `20px 36px 22px 36px !important`
  - `.reveal h2`: `font-size: 1.40rem; line-height: 1.25; letter-spacing: -0.015em;`
  - `.reveal p`: `font-size: 0.94rem; line-height: 1.45;`
  - Robust `.slide-header` styling for title, subtitle, and badge
- [ ] **Step 2: Refactor Slide 1 (Title Slide)**
  - Use Session 09 structure with centered container
  - Badges: `ภาคเรียนที่ 1/2569` and `ครั้งที่ 14 / 14` with FontAwesome icons
  - Title: 2-line `<h1>` (2.25em, weight 900)
  - Subtitle: `Fundamentals of Data Science (พื้นฐานวิทยาการข้อมูล)`
  - Instructor pill: Pill shape with FontAwesome icon `fa-user-tie` and affiliation "มหาวิทยาลัยศรีปทุม"
- [ ] **Step 3: Refactor Slide 2 (Recap & Connection - The Grand Finale)**
  - Standard `.slide-header` with `<h2><i class="fas fa-route"></i> มหากาพย์ 14 สัปดาห์: จากศูนย์สู่ผู้ประกอบการที่ขับเคลื่อนด้วยข้อมูล</h2>` and `.badge-step`
  - Standard `.step-container` with 5 `.step-card` elements, highlighting `Step 5 ACT (TODAY!)`
  - Standard `.grid-2` comparison cards with icons: วันแรก (Week 1) vs วันนี้ (Week 14)
  - Standard callout box for golden rule
- [ ] **Step 4: Standardize Slide Headers & Comments throughout Slides 3 to 34**
  - Ensure all slide headers use `<h2>` with FontAwesome icons and `.badge-step` on the right
  - Verify continuous comment numbering `<!-- SLIDE X: [SLIDE_NAME] -->` 1 to 34
- [ ] **Step 5: Verify in browser that Slide 1, Slide 2, and slide typography render correctly**

---

### Task 6: Quiz Synchronization & Automated Git Commit/Push

**Files:**
- Touch/Update: `session/session-11/session-11-quiz.md` & `.xlsx`
- Touch/Update: `session/session-12/session-12-quiz.md` & `.xlsx`
- Touch/Update: `session/session-13/session-13-quiz.md` & `.xlsx`
- Touch/Update: `session/session-14/session-14-quiz.md` & `.xlsx`

- [ ] **Step 1: Audit & synchronize quizzes with latest slide headers/terms**
- [ ] **Step 2: Convert quizzes to `.xlsx` using `quiz_to_xlsx.ps1`**
- [ ] **Step 3: Check `git status` and stage all changed files**
- [ ] **Step 4: Commit with descriptive message and push to GitHub remote**
