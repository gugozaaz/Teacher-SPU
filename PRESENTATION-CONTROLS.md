# มาตรฐานและคู่มือระบบควบคุมสไลด์นำเสนอ (Presentation Controls & Navigation Standard)
## หลักสูตร: พื้นฐานวิทยาการข้อมูล (Fundamentals of Data Science)

เอกสารส่วนกลางฉบับนี้กำหนดมาตรฐานการแสดงผล โครงสร้าง UI/UX และระบบควบคุมการนำทางสไลด์ Reveal.js สำหรับทุกคาบเรียน (`session/session-XX/session-XX-presentation.html`) เพื่อความสอดคล้อง เป็นมืออาชีพ และสะดวกสูงสุดในการจัดกิจกรรมการเรียนการสอน

---

## 🎯 1. มาตรฐานการแสดงผลและส่วนติดต่อผู้ใช้ (UI/UX Standards)

1. **อัตราส่วนและความละเอียดหน้าจอ (Resolution & Aspect Ratio):**
   * **อัตราส่วนเริ่มต้น (Default):** **16:10** (`width: 1280, height: 800`, `margin: 0.04`) ให้ขนาดตัวอักษรภาษาไทย หัวข้อ และการ์ดข้อมูลมีขนาดใหญ่อ่านง่าย สบายตา
   * **อัตราส่วนสลับใช้งาน:** **16:9** (`width: 1280, height: 720`) สำหรับจอภาพหรือโปรเจกเตอร์ Wide 16:9 มาตรฐาน
2. **ไม่ใช้แถบข้อความด้านล่าง (`.deck-footer`):**
   * ห้ามมีแถบด้านล่างค้างอยู่บนหน้าจอ เพื่อป้องกันการบดบังเนื้อหาสไลด์ กล่อง Callout ตาราง หรือเนื้อหาการสอนส่วนล่าง
3. **ซ่อนปุ่มลูกศรนำทาง (`controls: false`):**
   * ปิดการแสดงผลปุ่มลูกศรควบคุมที่มุมขวาล่างของ Reveal.js เพื่อให้หน้าจอคลีน สะอาดตา ไร้สิ่งรบกวน
4. **นำทางด้วย Keyboard & Mouse แทนปุ่มบนหน้าจอ:**
   * สไลด์ทุกชุดต้องควบคุมได้อย่างลื่นไหลผ่านเมาส์และคีย์บอร์ด
5. **ระบบแจ้งเตือนสถานะชั่วคราว (HUD Toast Notification):**
   * เมื่อมีการสลับขนาดหน้าจอ ต้องมีกล่องข้อความลอย (Floating Toast) แจ้งเตือนสถานะขนาดหน้าจอชั่วคราว 1.5 วินาที แล้วค่อย ๆ จางหายไปอัตโนมัติ (Fade out) โดยไม่ค้างบังหน้าจอ

---

## ⌨️ 2. ตารางคำสั่งควบคุมสไลด์ส่วนกลาง (Standard Navigation Cheatsheet)

### การเลื่อนเปลี่ยนหน้าสไลด์ (Slide Navigation)
| การกระทำ | คำสั่งผ่าน Keyboard | คำสั่งผ่าน Mouse | หมายเหตุ |
|:---|:---:|:---:|:---|
| **สไลด์ถัดไป (Next Slide)** | `ลูกศรขวา (→)` หรือ `Space` | **Mouse Scroll Down** (หมุนลูกกลิ้งลง) | เลื่อนไปข้างหน้าทีละ 1 สไลด์ |
| **สไลด์ก่อนหน้า (Previous Slide)** | `ลูกศรซ้าย (←)` | **Mouse Scroll Up** (หมุนลูกกลิ้งขึ้น) | ถอยกลับทีละ 1 สไลด์ |

---

### การควบคุมโหมดการแสดงผล (Display & Presentation Modes)
| การกระทำ | ปุ่มลัด (Shortcut Key) | ผลลัพธ์และฟังก์ชันการทำงาน |
|:---|:---:|:---|
| **สลับอัตราส่วนหน้าจอ** | **`A`** (หรือ `a`) | สลับระหว่าง **16:10** (`1280×800`) และ **16:9** (`1280×720`) พร้อม HUD Toast |
| **เปิด / ปิดโหมดเต็มจอ** | **`F`** | เข้าสู่โหมด Fullscreen เพื่อการนำเสนอบนจอโปรเจกเตอร์หรือทีวี |
| **ภาพรวมสไลด์ทั้งหมด** | **`O`** หรือ **`Esc`** | แสดงภาพสไลด์ทั้งหมดแบบกระเบื้อง (Tile Overview) เพื่อข้ามหัวข้อ |
| **พักหน้าจอชั่วคราว** | **`B`** หรือ **`.`** | พักหน้าจอเป็นสีดำสนิท (Blackout) เพื่อดึงความสนใจนักเรียนกลับมาที่ผู้สอน |
| **หน้าต่างบันทึกผู้สอน** | **`S`** | เปิดหน้าต่าง Speaker Notes แสดงโน้ตและเวลาจับการบรรยาย |
| **เปิด/ปิด Slide Audit Overlay** | **`T`** | เปิด/ปิดหน้าต่างตรวจสอบความสูงสไลด์และการล้นของเนื้อหา (Debug) |

---

## 💡 3. เหตุผลทางเทคนิคในการเลือกปุ่ม `A` สำหรับสลับ Aspect Ratio

* **ปลอดภัย 100% ต่อระบบปฏิบัติการ Windows:** ไม่ใช้ปุ่มร่วมกับ `Win` หรือ `Alt` จึงไม่มีผลข้างเคียงต่อระบบปฏิบัติการ
* **ไม่ขัดแย้งกับ Google Chrome / Edge:** เบราว์เซอร์ไม่มีคำสั่งที่ผูกกับตัวอักษรเดี่ยว `A` (มีแต่ `Ctrl + A` สำหรับ Select All) และโค้ดได้เพิ่มการป้องกันกรณีโฟกัสอยู่ในช่องกรอกข้อความ (`INPUT`, `TEXTAREA`)
* **ไม่ทับซ้อนกับปุ่มมาตรฐานของ Reveal.js:** ปุ่มดั้งเดิมคือ `F`, `S`, `O`, `B`, `?` ซึ่งปุ่ม `A` ยังว่างอยู่
* **จดจำง่ายและตรงตัว:** `A` ย่อมาจาก **A**spect Ratio สะดวกในการกดยกสลับด้วยมือซ้ายของผู้สอนได้ทันที

---

## ⚙️ 4. โค้ดต้นแบบสำหรับการสร้าง Session ใหม่ (Implementation Template)

เมื่อสร้างหรือปรับปรุงสไลด์ Reveal.js ในโฟลเดอร์ `session/session-XX/session-XX-presentation.html` ให้วางโครงสร้าง JavaScript มาตรฐานดังนี้:

```javascript
// 1. Reveal.js Configuration
const deck = new Reveal({
    width: 1280,
    height: 800,
    margin: 0.04,
    minScale: 0.1,
    maxScale: 3.0,
    controls: false,      // ซ่อนปุ่มลูกศรนำทาง
    progress: true,       // เส้นความคืบหน้าบางเฉียบด้านล่าง
    center: false,
    hash: true,
    transition: 'slide',
    transitionSpeed: 'default',
    mouseWheel: true,     // เลื่อนสไลด์ด้วย Mouse Wheel (Scroll Up = Prev, Scroll Down = Next)
    plugins: [RevealNotes, RevealHighlight]
});

deck.initialize().then(() => {
    window.deck = deck;
    window.Reveal = deck;

    // 2. Keyboard Event Listeners
    window.addEventListener('keydown', (e) => {
        if (['INPUT', 'TEXTAREA'].includes(e.target.tagName)) return;

        // ปุ่ม A / a: สลับ Aspect Ratio 16:10 <-> 16:9
        if (e.key === 'a' || e.key === 'A') {
            toggleAspectRatio();
        }

        // ปุ่ม T / t: เปิด Overlay ตรวจสอบ Slide Height
        if (e.key === 't' || e.key === 'T') {
            const overlay = document.getElementById('test-report-overlay');
            if (overlay) {
                overlay.style.display = overlay.style.display === 'block' ? 'none' : 'block';
                if (overlay.style.display === 'block' && typeof window.runSlideHeightAudit === 'function') {
                    window.runSlideHeightAudit();
                }
            }
        }
    });
});

// 3. HUD Toast แจ้งสถานะขนาดหน้าจอชั่วคราว
function showRatioToast(msg) {
    let toast = document.getElementById('aspect-ratio-toast');
    if (!toast) {
        toast = document.createElement('div');
        toast.id = 'aspect-ratio-toast';
        toast.style.cssText = `
            position: fixed;
            bottom: 24px;
            right: 24px;
            background: rgba(15, 23, 42, 0.90);
            backdrop-filter: blur(8px);
            color: #ffffff;
            padding: 8px 18px;
            border-radius: 9999px;
            font-family: 'Outfit', 'Noto Sans Thai', sans-serif;
            font-size: 0.85rem;
            font-weight: 600;
            letter-spacing: 0.02em;
            box-shadow: 0 4px 14px rgba(0, 0, 0, 0.2);
            border: 1px solid rgba(255, 255, 255, 0.15);
            z-index: 99999;
            pointer-events: none;
            transition: opacity 0.3s ease, transform 0.3s ease;
            transform: translateY(0);
            opacity: 0;
        `;
        document.body.appendChild(toast);
    }
    toast.innerHTML = `<i class="fa-solid fa-display" style="margin-right: 8px; color: #818cf8;"></i> ${msg}`;
    toast.style.opacity = '1';
    toast.style.transform = 'translateY(0)';
    clearTimeout(window._ratioToastTimer);
    window._ratioToastTimer = setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateY(6px)';
    }, 1500);
}

// 4. ฟังก์ชันสลับอัตราส่วนหน้าจอ
function toggleAspectRatio() {
    if (deck.getConfig().height === 800) {
        deck.configure({ width: 1280, height: 720 });
        showRatioToast('สลับอัตราส่วนหน้าจอ: 16:9 (1280 × 720)');
    } else {
        deck.configure({ width: 1280, height: 800 });
        showRatioToast('สลับอัตราส่วนหน้าจอ: 16:10 (1280 × 800)');
    }
}
window.toggleAspectRatio = toggleAspectRatio;
```
