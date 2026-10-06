import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

OUTPUT_DIR = r"d:\GoogleDrive\VibeCoding\teacher\session\session-05"

def get_base_styles():
    font_header = Font(name="Noto Sans Thai", size=10, bold=True, color="FFFFFF")
    font_data = Font(name="Noto Sans Thai", size=10, color="0F172A")
    font_bold = Font(name="Noto Sans Thai", size=10, bold=True, color="0F172A")
    font_muted = Font(name="Noto Sans Thai", size=9, italic=True, color="64748B")
    
    fill_header = PatternFill(start_color="3730A3", end_color="3730A3", fill_type="solid") # Indigo 800
    fill_bad = PatternFill(start_color="FFE4E6", end_color="FFE4E6", fill_type="solid") # Rose 100
    fill_bad_cell = PatternFill(start_color="FECDD3", end_color="FECDD3", fill_type="solid") # Rose 200
    fill_warning = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid") # Amber 100
    fill_fix = PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid") # Emerald 100
    
    thin_border = Border(
        left=Side(style='thin', color='CBD5E1'),
        right=Side(style='thin', color='CBD5E1'),
        top=Side(style='thin', color='CBD5E1'),
        bottom=Side(style='thin', color='CBD5E1')
    )
    
    return {
        "font_header": font_header,
        "font_data": font_data,
        "font_bold": font_bold,
        "font_muted": font_muted,
        "fill_header": fill_header,
        "fill_bad": fill_bad,
        "fill_bad_cell": fill_bad_cell,
        "fill_warning": fill_warning,
        "fill_fix": fill_fix,
        "thin_border": thin_border
    }

def create_explanation_sheet(wb, title, subtitle, trap_no, trap_name, description, why_bad, how_to_fix, tools_used):
    ws = wb.create_sheet(title="คำอธิบายข้อผิดพลาด")
    ws.views.sheetView[0].showGridLines = True
    
    title_font = Font(name="Noto Sans Thai", size=13, bold=True, color="1E1B4B")
    subtitle_font = Font(name="Noto Sans Thai", size=10, italic=True, color="4338CA")
    bold_font = Font(name="Noto Sans Thai", size=10, bold=True, color="0F172A")
    normal_font = Font(name="Noto Sans Thai", size=10, color="334155")
    
    fill_header = PatternFill(start_color="EEF2FF", end_color="EEF2FF", fill_type="solid")
    fill_bad = PatternFill(start_color="FFE4E6", end_color="FFE4E6", fill_type="solid")
    fill_fix = PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid")
    fill_trap = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid")
    
    ws["B2"] = title
    ws["B2"].font = title_font
    ws["B3"] = subtitle
    ws["B3"].font = subtitle_font
    
    ws["B5"] = "กับดักข้อมูลสกปรก (Dirty Data Trap):"
    ws["B5"].font = bold_font
    ws["B5"].fill = fill_trap
    ws["C5"] = f"{trap_no}: {trap_name}"
    ws["C5"].font = bold_font
    
    ws["B6"] = "ลักษณะข้อมูลที่ไม่ถูกต้องในตารางนี้:"
    ws["B6"].font = bold_font
    ws["C6"] = description
    ws["C6"].font = normal_font
    
    ws["B8"] = "ทำไมจึงเป็นปัญหาต่อธุรกิจ? (Pain Points & GIGO):"
    ws["B8"].font = bold_font
    ws["B8"].fill = fill_bad
    
    row = 9
    for point in why_bad:
        ws.cell(row=row, column=2, value="❌").alignment = Alignment(horizontal="center")
        ws.cell(row=row, column=3, value=point).font = normal_font
        row += 1
        
    row += 1
    ws.cell(row=row, column=2, value="วิธีแก้ไขตามมาตรฐาน Session 5 (Best Practices):").font = bold_font
    ws.cell(row=row, column=2).fill = fill_fix
    row += 1
    for fix in how_to_fix:
        ws.cell(row=row, column=2, value="✔️").alignment = Alignment(horizontal="center")
        ws.cell(row=row, column=3, value=fix).font = normal_font
        row += 1
        
    row += 1
    ws.cell(row=row, column=2, value="เครื่องมือ & สูตร Google Sheets ที่ใช้:").font = bold_font
    ws.cell(row=row, column=2).fill = fill_header
    ws.cell(row=row, column=3, value=tools_used).font = bold_font
    
    ws.column_dimensions['A'].width = 4
    ws.column_dimensions['B'].width = 38
    ws.column_dimensions['C'].width = 95

def auto_fit_columns(ws, max_cols=12):
    for col in range(1, max_cols + 1):
        col_letter = get_column_letter(col)
        max_len = 0
        for row in range(1, ws.max_row + 1):
            val = ws.cell(row=row, column=col).value
            if val is not None:
                val_str = str(val)
                # approximate Thai char length
                thai_len = len(val_str)
                if thai_len > max_len:
                    max_len = thai_len
        ws.column_dimensions[col_letter].width = max(max_len + 4, 12)

# ==============================================================================
# 1. TRAP 1: DUPLICATE RECORDS (bad_data_01_duplicate_records.xlsx)
# ==============================================================================
def generate_trap_01():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "orders_duplicate_trap"
    styles = get_base_styles()
    
    headers = ["Order_ID", "Order_Date", "Customer_Name", "Product_Name", "Color", "Size", "Quantity", "Unit_Price", "Total_Amount", "Channel", "Note_Trap_Audit"]
    
    rows = [
        ["ORD-1001", "2026-03-01", "คุณสมศรี ใจดี", "เสื้อยืด Oversize", "ขาว", "M", 1, 350, 350, "TikTok Shop", "ปกติ"],
        ["ORD-1002", "2026-03-01", "คุณวิชัย เกียรติสกุล", "กางเกงยีนส์ขากระบอก", "ยีนส์เข้ม", "L", 2, 890, 1780, "Shopee", "ซ้ำแถวแรก (ออเดอร์เบิ้ลจากการกดซ้ำ)"],
        ["ORD-1002", "2026-03-01", "คุณวิชัย เกียรติสกุล", "กางเกงยีนส์ขากระบอก", "ยีนส์เข้ม", "L", 2, 890, 1780, "Shopee", "ซ้ำแถวที่สอง (Duplicate Row 100%)"],
        ["ORD-1003", "2026-03-01", "คุณกานดา รัตนกุล", "เสื้อครอปไหมพรม", "ชมพู", "S", 1, 290, 290, "LINE OA", "ปกติ"],
        ["ORD-1004", "2026-03-02", "คุณพงษ์ศักดิ์ ชัยชนะ", "กระเป๋าผ้าแคนวาส", "ดำ", "Free", 1, 199, 199, "หน้าร้าน", "ปกติ"],
        ["ORD-1005", "2026-03-02", "คุณดาริน แซ่ตั้ง", "เดรสชีฟองลายดอก", "ฟ้า", "M", 1, 490, 490, "TikTok Shop", "ซ้ำแถวแรก (ส่งไฟล์ซ้อน)"],
        ["ORD-1005", "2026-03-02", "คุณดาริน แซ่ตั้ง", "เดรสชีฟองลายดอก", "ฟ้า", "M", 1, 490, 490, "TikTok Shop", "ซ้ำแถวที่สอง (Duplicate Row)"],
        ["ORD-1006", "2026-03-02", "คุณธีรพงษ์ สุขเกษม", "เสื้อโปโลคลาสสิก", "กรมท่า", "XL", 2, 450, 900, "Shopee", "ปกติ"],
        ["ORD-1007", "2026-03-03", "คุณมณีรัตน์ วงศ์วิวัฒน์", "เสื้อยืด Oversize", "ดำ", "L", 1, 350, 350, "TikTok Shop", "ปกติ"],
        ["ORD-1008", "2026-03-03", "คุณณัฐพล ทองสุข", "กางเกงสแล็คทำงาน", "ดำ", "32", 1, 690, 690, "LINE OA", "ซ้ำแถวแรก (เน็ตค้างขณะยืนยัน)"],
        ["ORD-1008", "2026-03-03", "คุณณัฐพล ทองสุข", "กางเกงสแล็คทำงาน", "ดำ", "32", 1, 690, 690, "LINE OA", "ซ้ำแถวที่สอง (Duplicate Row)"],
        ["ORD-1009", "2026-03-03", "คุณวราภรณ์ สดใส", "เสื้อเบลเซอร์ลำลอง", "เบจ", "M", 1, 890, 890, "หน้าร้าน", "ปกติ"],
        ["ORD-1010", "2026-03-04", "คุณพิเชษฐ์ บรรเจิด", "เสื้อฮู้ดดี้แขนยาว", "เทาเข้ม", "XXL", 1, 650, 650, "Shopee", "ปกติ"],
        ["ORD-1011", "2026-03-04", "คุณอารียา นิมิตกุล", "เสื้อยืด Oversize", "ขาว", "S", 3, 350, 1050, "TikTok Shop", "ปกติ"],
        ["ORD-1012", "2026-03-04", "คุณชาญวิทย์ วารี", "กางเกงยีนส์ขาสั้น", "ฟอกซีด", "34", 1, 490, 490, "LINE OA", "ซ้ำแถวแรก"],
        ["ORD-1012", "2026-03-04", "คุณชาญวิทย์ วารี", "กางเกงยีนส์ขาสั้น", "ฟอกซีด", "34", 1, 490, 490, "LINE OA", "ซ้ำแถวที่สอง (Duplicate Row)"],
        ["ORD-1013", "2026-03-05", "คุณจันทิมา ศรีสวัสดิ์", "เสื้อครอปไหมพรม", "ครีม", "Free", 2, 290, 580, "หน้าร้าน", "ปกติ"],
        ["ORD-1014", "2026-03-05", "คุณธนกร เลิศปัญญา", "เสื้อยืดคอกลม", "เขียวขี้ม้า", "L", 1, 290, 290, "TikTok Shop", "ปกติ"],
        ["ORD-1015", "2026-03-05", "คุณปิยะวรรณ เกตุแก้ว", "กระโปรงพลีทจีบรอบ", "ดำ", "Free", 1, 390, 390, "Shopee", "ซ้ำแถวแรก (ระบบดึงยอดเบิ้ล)"],
        ["ORD-1015", "2026-03-05", "คุณปิยะวรรณ เกตุแก้ว", "กระโปรงพลีทจีบรอบ", "ดำ", "Free", 1, 390, 390, "Shopee", "ซ้ำแถวที่สอง (Duplicate Row)"],
        ["ORD-1016", "2026-03-06", "คุณกิตติศักดิ์ ภักดี", "แจ็คเก็ตยีนส์ย้อนยุค", "ยีนส์ฟอก", "XL", 1, 990, 990, "LINE OA", "ปกติ"],
        ["ORD-1017", "2026-03-06", "คุณลลิตา รักษ์ดี", "เสื้อเชิ้ตโอเวอร์ไซส์", "ขาว", "L", 2, 420, 840, "TikTok Shop", "ปกติ"],
        ["ORD-1018", "2026-03-06", "คุณอนุพงศ์ มีโชค", "กางเกงขาสั้นชิโน", "กากี", "32", 1, 390, 390, "หน้าร้าน", "ซ้ำแถวแรก"],
        ["ORD-1018", "2026-03-06", "คุณอนุพงศ์ มีโชค", "กางเกงขาสั้นชิโน", "กากี", "32", 1, 390, 390, "หน้าร้าน", "ซ้ำแถวที่สอง (Duplicate Row)"],
        ["ORD-1019", "2026-03-07", "คุณศิริพร บุญยืน", "เสื้อยืด Oversize", "ชมพูพาสเทล", "M", 1, 350, 350, "TikTok Shop", "ปกติ"],
        ["ORD-1020", "2026-03-07", "คุณเกรียงไกร ชาญวิชิต", "เสื้อกล้ามสปอร์ต", "ดำ", "L", 2, 220, 440, "Shopee", "ปกติ"]
    ]
    
    # Write Headers
    for c_idx, h in enumerate(headers, 1):
        cell = ws.cell(row=1, column=c_idx, value=h)
        cell.font = styles["font_header"]
        cell.fill = styles["fill_header"]
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = styles["thin_border"]
    
    # Write Data
    for r_idx, row_data in enumerate(rows, 2):
        is_dup = "ซ้ำ" in row_data[10]
        for c_idx, val in enumerate(row_data, 1):
            cell = ws.cell(row=r_idx, column=c_idx, value=val)
            cell.font = styles["font_data"]
            cell.border = styles["thin_border"]
            if is_dup:
                cell.fill = styles["fill_bad"]
                if c_idx == 10:
                    cell.font = Font(name="Noto Sans Thai", size=9, bold=True, color="BE123C")
            if c_idx in [7, 8, 9]:
                cell.alignment = Alignment(horizontal="right")
                if c_idx in [8, 9]:
                    cell.number_format = "#,##0"
            elif c_idx in [1, 2, 6]:
                cell.alignment = Alignment(horizontal="center")
                
    auto_fit_columns(ws, len(headers))
    
    why_bad = [
        "ยอดขายรวมพองเกินจริง: มีแถวออเดอร์เบิ้ลถึง 6 แถว รวมมูลค่าเงินซ้ำซ้อนกว่า 4,500 บาท",
        "ตัดสต็อกสินค้าผิดพลาด: ระบบคำนวณว่าตัดสต็อกเสื้อยีนส์และเดรสไป 2 เท่า จนเกิดปัญหาสต็อกขาด",
        "กระทบต่อการยิงแอดและการขนส่ง: ส่งสินค้าหรือแจ้งเตือนสถานะซ้ำซ้อนให้ลูกค้ารายเดิม"
    ]
    how_to_fix = [
        "สำรองชีตดิบเป็น 'raw_data_backup' ก่อนเสมอ (ห้ามแก้ทับไฟล์เดิม)",
        "คลุมตารางแล้วใช้เมนู Data > Data cleanup > Remove duplicates",
        "ติ๊ก 'Data has header row' และเลือกคอลัมน์ Order_ID เพื่อตัดแถวที่คีย์เบิ้ลออก",
        "บันทึกประวัติการลบ 6 แถวลงใน Data Cleaning Log"
    ]
    create_explanation_sheet(wb, "กับดักที่ 1: ข้อมูลซ้ำซ้อน (Duplicate Records)", "ไฟล์ตัวอย่างชุดข้อมูลยอดขายที่มีออเดอร์บันทึกเบิ้ลจากการรวมข้อมูลหลายแพลตฟอร์ม", "Trap 1", "Duplicate Records", "มีแถวออเดอร์บันทึกซ้ำกันทุกตัวอักษรเนื่องจากลูกค้ากดสั่งเบิ้ล หรือรวมไฟล์ซ้ำซ้อน", why_bad, how_to_fix, "Data > Data cleanup > Remove duplicates หรือสูตร =UNIQUE()")
    
    wb.save(os.path.join(OUTPUT_DIR, "bad_data_01_duplicate_records.xlsx"))
    print("Generated: bad_data_01_duplicate_records.xlsx")

# ==============================================================================
# 2. TRAP 2: WHITESPACE & TYPOS (bad_data_02_hidden_whitespace_and_typos.xlsx)
# ==============================================================================
def generate_trap_02():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "menu_whitespace_trap"
    styles = get_base_styles()
    
    headers = ["Item_ID", "Date", "Menu_Name_Raw", "LEN_Audit", "Category", "Size", "Price", "Qty_Sold", "Revenue", "Note_Typo_Issue"]
    
    # HealthyBites Clean Food Store
    rows = [
        ["HB-01", "2026-03-01", "ข้าวยำอกไก่ย่าง", "=LEN(C2)", "อาหารคลีน", "M", 129, 15, "=G2*H2", "ปกติ (ความยาว 14 ตัว)"],
        ["HB-02", "2026-03-01", " ข้าวยำอกไก่ย่าง", "=LEN(C3)", "อาหารคลีน", "M", 129, 8, "=G3*H3", "มี Space ข้างหน้า (Pivot แยกแถว)"],
        ["HB-03", "2026-03-01", "ข้าวยำอกไก่ย่าง ", "=LEN(C4)", "อาหารคลีน", "m", 129, 12, "=G4*H4", "มี Space ข้างหลัง + ไซส์ตัวพิมพ์เล็ก 'm'"],
        ["HB-04", "2026-03-01", "ข้าวยำ   อกไก่ย่าง", "=LEN(C5)", "อาหารคลีน", "M", 129, 6, "=G5*H5", "Space ตรงกลาง 3 เคาะ"],
        ["HB-05", "2026-03-02", "สลัดแซลมอนย่าง", "=LEN(C6)", "สลัดเพื่อสุขภาพ", "L", 189, 10, "=G6*H6", "ปกติ"],
        ["HB-06", "2026-03-02", "  สลัดแซลมอนย่าง ", "=LEN(C7)", "สลัดเพื่อสุขภาพ", "l", 189, 4, "=G7*H7", "Space ทั้งหน้าและหลัง + ไซส์ 'l'"],
        ["HB-07", "2026-03-02", "สเต็กเต้าหู้เห็ดหอม", "=LEN(C8)", "มังสวิรัติ", "Standard", 119, 7, "=G8*H8", "ปกติ"],
        ["HB-08", "2026-03-02", "สเต๊กเต้าหู้เห็ดหอม", "=LEN(C9)", "มังสวิรัติ", "Standard", 119, 5, "=G9*H9", "สะกดผิด 'สเต๊ก' (ไม้ตรี vs ไม้โท)"],
        ["HB-09", "2026-03-03", "น้ำผลไม้สกัดเย็น", "=LEN(C10)", "เครื่องดื่ม", "Bottle", 85, 20, "=G10*H10", "ปกติ"],
        ["HB-10", "2026-03-03", "Cold-Pressed Juice", "=LEN(C11)", "Beverage", "bottle", 85, 14, "=G11*H11", "ใช้ภาษาอังกฤษปน ไม่ตรงมาตรฐานภาษาไทย"],
        ["HB-11", "2026-03-03", " น้ำผลไม้สกัดเย็น ", "=LEN(C12)", "เครื่องดื่ม", "Bottle", 85, 11, "=G12*H12", "ช่องว่างหน้าหลัง"],
        ["HB-12", "2026-03-04", "อกไก่นุ่มพริกไทยดำ", "=LEN(C13)", "อาหารคลีน", "S", 99, 18, "=G13*H13", "ปกติ"],
        ["HB-13", "2026-03-04", "อกไก่นุ่มพริกไทยดำ ", "=LEN(C14)", "อาหารคลีน", "s", 99, 9, "=G14*H14", "มีช่องว่างท้ายคำ + ไซส์ตัวเล็ก"],
        ["HB-14", "2026-03-04", " อกไก่นุ่ม พริกไทยดำ", "=LEN(C15)", "อาหารคลีน", "S", 99, 5, "=G15*H15", "Space ด้านหน้าและเคาะตรงกลาง"],
        ["HB-15", "2026-03-05", "ข้าวไรซ์เบอร์รี่ลาบปลาแซลมอน", "=LEN(C16)", "อาหารคลีน", "M", 159, 12, "=G16*H16", "ปกติ"],
        ["HB-16", "2026-03-05", "ข้าวไรซ์เบอรี่ลาบปลาแซลมอน", "=LEN(C17)", "อาหารคลีน", "m", 159, 7, "=G17*H17", "สะกดผิด 'ไรซ์เบอรี่' (ขาดไม้หันอากาศ รร)"],
        ["HB-17", "2026-03-05", "ซุปฟักทองญี่ปุ่น", "=LEN(C18)", "ซุป & ของทานเล่น", "Cup", 79, 16, "=G18*H18", "ปกติ"],
        ["HB-18", "2026-03-06", " ซุปฟักทองญี่ปุ่น", "=LEN(C19)", "ซุป & ของทานเล่น", "cup", 79, 8, "=G19*H19", "Space ข้างหน้า + cup ตัวพิมพ์เล็ก"],
        ["HB-19", "2026-03-06", "ยำทูน่าสมุนไพรสด", "=LEN(C20)", "สลัดเพื่อสุขภาพ", "M", 139, 14, "=G20*H20", "ปกติ"],
        ["HB-20", "2026-03-06", "ยำทูน่าสมุนไพรสด ", "=LEN(C21)", "สลัดเพื่อสุขภาพ", "M", 139, 6, "=G21*H21", "Space ท้ายคำ"],
        ["HB-21", "2026-03-07", "กรีกโยเกิร์ตผลไม้รวม", "=LEN(C22)", "ของหวานเพื่อสุขภาพ", "Bowl", 109, 15, "=G22*H22", "ปกติ"],
        ["HB-22", "2026-03-07", " กรีกโยเกิร์ตผลไม้รวม ", "=LEN(C23)", "ของหวานเพื่อสุขภาพ", "bowl", 109, 9, "=G23*H23", "Space หน้าหลัง + ไซส์ bowl"],
        ["HB-23", "2026-03-07", "แซนด์วิชไข่ต้มอะโวคาโด", "=LEN(C24)", "อาหารคลีน", "Set", 95, 11, "=G24*H24", "ปกติ"],
        ["HB-24", "2026-03-07", "แซนด์วิชไข่ต้มอโวคาโด", "=LEN(C25)", "อาหารคลีน", "set", 95, 7, "=G25*H25", "สะกดไม่เหมือนกัน 'อโวคาโด' vs 'อะโวคาโด'"],
        ["HB-25", "2026-03-07", "ข้าวยำอกไก่ย่าง", "=LEN(C26)", "อาหารคลีน", "XL", 149, 13, "=G26*H26", "ปกติ"]
    ]
    
    for c_idx, h in enumerate(headers, 1):
        cell = ws.cell(row=1, column=c_idx, value=h)
        cell.font = styles["font_header"]
        cell.fill = styles["fill_header"]
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = styles["thin_border"]
        
    for r_idx, row_data in enumerate(rows, 2):
        has_issue = row_data[9] != "ปกติ" and "ความยาว" not in row_data[9]
        for c_idx, val in enumerate(row_data, 1):
            cell = ws.cell(row=r_idx, column=c_idx, value=val)
            cell.font = styles["font_data"]
            cell.border = styles["thin_border"]
            if has_issue:
                if c_idx in [3, 4, 6, 10]:
                    cell.fill = styles["fill_bad"]
            if c_idx in [4, 7, 8, 9]:
                cell.alignment = Alignment(horizontal="right")
                if c_idx in [7, 9]:
                    cell.number_format = "#,##0"
            elif c_idx in [1, 2, 6]:
                cell.alignment = Alignment(horizontal="center")
                
    auto_fit_columns(ws, len(headers))
    
    why_bad = [
        "Pivot Table แยกแถวเมนูยอดฮิต: เมนู 'ข้าวยำอกไก่ย่าง' แตกออกเป็น 4 บรรทัด ทำให้ดูเหมือนขายไม่ดี",
        "VLOOKUP ค้นหาไม่เจอ: การดึงราคาสินค้าหรือรหัสสินค้าจะส่งผลลัพธ์เป็น #N/A เพราะช่องว่างล่องหน",
        "ตัวพิมพ์เล็ก/ใหญ่ (s vs S, m vs M): ระบบฐานข้อมูลมองเป็นคนละหมวดหมู่ สรุปยอดตามขนาดสินค้าไม่ได้"
    ]
    how_to_fix = [
        "ใช้คำสั่ง Data > Data cleanup > Trim whitespace เพื่อตัดช่องว่างหัว-ท้ายออกทั้งคอลัมน์",
        "ใช้สูตร =TRIM(C2) เพื่อตัดช่องว่างหน้าหลังและยุบช่องว่างตรงกลางที่เคาะเกินให้เหลือเคาะเดียว",
        "ใช้สูตร =UPPER(F2) หรือ =PROPER(F2) ปรับขนาดตัวพิมพ์ให้สม่ำเสมอเป็นมาตรฐานเดียวกัน",
        "ใช้ Edit > Find and replace (Ctrl+H) ติ๊ก 'Match entire cell contents' แก้คำสะกดผิดให้ตรงกับ Master Catalog"
    ]
    create_explanation_sheet(wb, "กับดักที่ 2: ช่องว่างล่องหน & คำสะกดเพี้ยน (Whitespace & Typos)", "ไฟล์ตัวอย่างเมนูอาหารคลีนที่ชื่อเมนูมีช่องว่างแอบแฝงและสะกดคนละแบบจน Pivot Table พัง", "Trap 2", "Whitespace & Inconsistent Text", "สายตามนุษย์มองว่าเหมือนกัน แต่คอมพิวเตอร์นับจำนวนตัวอักษร (LEN) ต่างกัน ทำให้รวมกลุ่มไม่ได้", why_bad, how_to_fix, "Data cleanup > Trim whitespace, =TRIM(), =UPPER(), =PROPER(), Ctrl+H (Match entire cell)")
    
    wb.save(os.path.join(OUTPUT_DIR, "bad_data_02_hidden_whitespace_and_typos.xlsx"))
    print("Generated: bad_data_02_hidden_whitespace_and_typos.xlsx")

# ==============================================================================
# 3. TRAP 3: MISSING VALUES & NULLS (bad_data_03_missing_values_and_nulls.xlsx)
# ==============================================================================
def generate_trap_03():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "gym_members_missing_trap"
    styles = get_base_styles()
    
    headers = ["Member_ID", "Full_Name", "Gender", "Age", "Phone_Number", "Package_Type", "Monthly_Fee", "Trainer_Assigned", "Join_Date", "Note_Missing_Trap"]
    
    # GymFit Express
    rows = [
        ["GF-101", "คุณสมชาย มุ่งมั่น", "ชาย", 28, "0812345678", "Annual Elite", 1500, "Coach Max", "2026-01-10", "ข้อมูลสมบูรณ์"],
        ["GF-102", "คุณพรทิพย์ สว่างจิต", "หญิง", 34, None, "Monthly Regular", 1200, "None", "2026-01-12", "เบอร์โทรว่างเปล่า (Blank)"],
        ["GF-103", "คุณวิทูร เจริญศรี", "ชาย", None, "0898765432", "Monthly Regular", 1200, "Coach Bank", "2026-01-15", "อายุว่างเปล่า (Missing Age)"],
        ["GF-104", "คุณเกสร บัวงาม", "หญิง", 25, "0861112233", "Student Pass", None, "None", "2026-01-18", "ค่าสมาชิกเว้นว่าง (Price Missing)"],
        ["GF-105", "คุณประเสริฐ ยิ่งยง", "ชาย", 42, "-", "Annual Elite", 1500, "Coach Max", "2026-01-20", "ใส่เครื่องหมายขีด '-' แทนเบอร์โทร"],
        ["GF-106", "คุณกัลยา พาเพลิน", "หญิง", 29, "0823334455", "Monthly Regular", 0, "Coach Bank", "2026-01-22", "ใส่เลข 0 มั่วซั่ว (ไม่ใช่โปรฟรี แต่ลืมคีย์เงิน)"],
        ["GF-107", "คุณอดิศร วงษ์ไทย", "ชาย", "NULL", "0856667788", "Personal Training", 2500, "Coach Max", "2026-01-25", "พิมพ์ตัวหนังสือ 'NULL' ในช่องอายุ"],
        ["GF-108", "คุณสิริกร มงคล", "หญิง", 31, "0879990011", "Annual Elite", 1500, "Coach Bow", "2026-01-28", "ข้อมูลสมบูรณ์"],
        ["GF-109", "คุณปิยะ ชนะพาล", "ชาย", 38, None, "Personal Training", 2500, "Coach Max", "2026-02-01", "เบอร์โทรว่าง"],
        ["GF-110", "คุณนงลักษณ์ ดีเลิศ", "หญิง", None, "0845556677", "Monthly Regular", 1200, "None", "2026-02-03", "อายุว่างเปล่า"],
        ["GF-111", "คุณธวัชชัย รุ่งโรจน์", "ชาย", 45, "0819998877", "Annual Elite", 1500, "Coach Bow", "2026-02-05", "ข้อมูลสมบูรณ์"],
        ["GF-112", "คุณพิมพา สุวรรณ", "หญิง", 22, "N/A", "Student Pass", 890, "None", "2026-02-08", "พิมพ์ 'N/A' ในช่องเบอร์โทร"],
        ["GF-113", "คุณอนุชา ช่างกล", "ชาย", 27, "0832223344", "Monthly Regular", None, "Coach Bank", "2026-02-10", "ค่าสมาชิกเว้นว่าง"],
        ["GF-114", "คุณลลนา งามยิ่ง", "หญิง", 36, "0894445566", "Personal Training", 2500, "Coach Max", "2026-02-12", "ข้อมูลสมบูรณ์"],
        ["GF-115", "คุณชัยพร สดสวย", "ชาย", 33, None, "Monthly Regular", 0, "None", "2026-02-15", "เบอร์โทรว่าง + ค่าบริการใส่ 0"],
        ["GF-116", "คุณมณฑา รุ่งเรือง", "หญิง", 40, "0867778899", "Annual Elite", 1500, "Coach Bow", "2026-02-18", "ข้อมูลสมบูรณ์"],
        ["GF-117", "คุณยุทธนา กาญจนา", "ชาย", None, "-", "Personal Training", 2500, "Coach Bank", "2026-02-20", "อายุว่าง + เบอร์โทรใส่ขีด"],
        ["GF-118", "คุณสุนิสา แก้วใส", "หญิง", 26, "0881119922", "Student Pass", 890, "None", "2026-02-22", "ข้อมูลสมบูรณ์"],
        ["GF-119", "คุณธีระ มหาลาภ", "ชาย", 50, "0824441133", "Annual Elite", 1500, "Coach Max", "2026-02-25", "ข้อมูลสมบูรณ์"],
        ["GF-120", "คุณนภา แจ่มจรัส", "หญิง", 24, None, "Monthly Regular", 1200, "Coach Bow", "2026-02-26", "เบอร์โทรว่าง"],
        ["GF-121", "คุณเอกพล ยิ่งยืน", "ชาย", 35, "0853332211", "Personal Training", None, "Coach Bank", "2026-02-27", "ค่าบริการเว้นว่าง"],
        ["GF-122", "คุณรสสุคนธ์ มีสุข", "หญิง", 29, "0876665544", "Monthly Regular", 1200, "None", "2026-02-28", "ข้อมูลสมบูรณ์"],
        ["GF-123", "คุณโกมินทร์ ปัญญา", "ชาย", "null", "0815554433", "Annual Elite", 1500, "Coach Max", "2026-03-01", "พิมพ์ 'null' ในช่องอายุ"],
        ["GF-124", "คุณวนิดา สมบูรณ์", "หญิง", 32, "0891114477", "Monthly Regular", 1200, "Coach Bow", "2026-03-02", "ข้อมูลสมบูรณ์"],
        ["GF-125", "คุณพิสุทธิ์ แดนไทย", "ชาย", 41, None, "Personal Training", 2500, "Coach Bank", "2026-03-03", "เบอร์โทรว่าง"]
    ]
    
    for c_idx, h in enumerate(headers, 1):
        cell = ws.cell(row=1, column=c_idx, value=h)
        cell.font = styles["font_header"]
        cell.fill = styles["fill_header"]
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = styles["thin_border"]
        
    for r_idx, row_data in enumerate(rows, 2):
        has_issue = row_data[9] != "ข้อมูลสมบูรณ์"
        for c_idx, val in enumerate(row_data, 1):
            cell = ws.cell(row=r_idx, column=c_idx, value=val)
            cell.font = styles["font_data"]
            cell.border = styles["thin_border"]
            
            # Check cell-level bad data
            if val is None or val == "" or str(val).strip() in ["-", "NULL", "null", "N/A"] or (c_idx == 7 and val == 0):
                cell.fill = styles["fill_bad_cell"]
            elif has_issue and c_idx == 10:
                cell.fill = styles["fill_warning"]
                cell.font = Font(name="Noto Sans Thai", size=9, bold=True, color="92400E")
                
            if c_idx in [4, 7]:
                cell.alignment = Alignment(horizontal="right")
                if c_idx == 7 and isinstance(val, (int, float)):
                    cell.number_format = "#,##0"
            elif c_idx in [1, 3, 5, 9]:
                cell.alignment = Alignment(horizontal="center")
                
    auto_fit_columns(ws, len(headers))
    
    why_bad = [
        "สูตรคำนวณค่าเฉลี่ยเพี้ยน: การใส่เลข 0 ในช่องค่าสมาชิก ทำให้ AVERAGE รายได้เฉลี่ยต่ำกว่าความเป็นจริงมหาศาล",
        "การใส่ขีด '-' หรือคำว่า 'NULL' ทำให้คอลัมน์ตัวเลขกลายเป็นข้อความ (Text) คำนวณทางสถิติต่อไม่ได้",
        "เบอร์โทรศัพท์เว้นว่าง: ระบบ CRM ไม่สามารถส่ง SMS แจ้งเตือนวันหมดอายุสมาชิก ทำให้สูญเสียลูกค้ารายเดือน"
    ]
    how_to_fix = [
        "ใช้ Format > Conditional formatting ตั้งกฎ 'Is empty' เพื่อส่องเซลล์ว่างให้เรืองแสงอัตโนมัติ",
        "ใช้สูตร =ISBLANK() และ =COUNTBLANK() สรุปจำนวนเซลล์ว่างในแต่ละคอลัมน์",
        "ใช้กลยุทธ์ Deletion: ลบแถวทิ้งเฉพาะกรณีที่ขาดข้อมูลสำคัญวิกฤตจนนำไปใช้ไม่ได้",
        "ใช้กลยุทธ์ Imputation: เติมราคามาตรฐานตามประเภท Package หรือใส่คำว่า 'ไม่ระบุ' สำหรับข้อความ",
        "ห้ามคีย์เลข 0 ลงในช่องว่างมั่วซั่วถ้าไม่ใช่ตัวเลข 0 จริงๆ!"
    ]
    create_explanation_sheet(wb, "กับดักที่ 3: ข้อมูลขาดหาย (Missing Values / Null Data)", "ไฟล์ตัวอย่างฐานข้อมูลสมาชิกฟิตเนสที่มีเซลล์ว่างและใส่เครื่องหมายกำกวมจนคำนวณไม่ได้", "Trap 3", "Missing Values & Nulls", "ช่องว่างเปล่า, ค่า NULL, เครื่องหมายขีด (-), และการพิมพ์เลข 0 แทนค่าว่าง ส่งผลให้สูตรเฉลี่ยพัง", why_bad, how_to_fix, "Conditional formatting (Is empty), =ISBLANK(), =COUNTBLANK(), Imputation")
    
    wb.save(os.path.join(OUTPUT_DIR, "bad_data_03_missing_values_and_nulls.xlsx"))
    print("Generated: bad_data_03_missing_values_and_nulls.xlsx")

# ==============================================================================
# 4. TRAP 4: FORMAT CHAOS (bad_data_04_date_and_number_format_chaos.xlsx)
# ==============================================================================
def generate_trap_04():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "format_chaos_trap"
    styles = get_base_styles()
    
    headers = ["Trans_ID", "Date_Chaos", "Customer", "Item_Code", "Price_Chaos", "Qty", "Total_Chaos", "Phone_Chaos", "Alignment_Status", "Note_Format_Error"]
    
    # Fashion & Retail Store Format Chaos
    rows = [
        ["TR-501", "2026-03-01", "คุณมนัส", "TS-01", 350, 1, 350, "0812345678", "Align Right (ตัวเลขจริง)", "ปกติ (ชิดขวา)"],
        ["TR-502", "02/03/2026", "คุณวาสนา", "JN-02", "฿ 890", 1, "฿ 890", "823456789", "Align Left (กลายเป็น Text)", "มีสัญลักษณ์ '฿' ปนทำให้ SUM ข้าม + เบอร์โทรศูนย์หน้าหาย"],
        ["TR-503", "03/05/2026", "คุณกิตติ", "TS-01", "350 บาท", 2, "700 บาท", "0834567890", "Align Left (มีคำว่า บาท)", "ใส่คำว่า 'บาท' ในเซลล์ สูตรคูณ/บวกพัง"],
        ["TR-504", "2569/03/02", "คุณนภาพร", "DR-03", 490, 1, 490, "0845678901", "Align Left (ปี พ.ศ.)", "ปี พ.ศ. ผสม ค.ศ. ระบบคิดว่าเป็นข้อความ"],
        ["TR-505", "20260303", "คุณสมเกียรติ", "CR-04", "290.-", 1, "290.-", "856789012", "Align Left (Text วันที่/ราคา)", "วันที่เขียนติดกัน 8 หลัก + ราคามี .-\""],
        ["TR-506", "2026-03-03", "คุณปรียา", "TS-01", 350, 2, 700, "0867890123", "Align Right", "ปกติ"],
        ["TR-507", "04-Mar-2026", "คุณธีรวัฒน์", "HD-05", " 650 ", 1, " 650 ", "0878901234", "Align Left (Space ในตัวเลข)", "ราคาเป็น Text เพราะเคาะวรรคแฝง"],
        ["TR-508", "2026/03/04", "คุณอารีย์", "JN-02", 890, 1, 890, "889012345", "Align Right (เบอร์โทรพัง)", "เบอร์โทรเป็นตัวเลขทำให้ 0 หน้าหาย"],
        ["TR-509", "05/03/2026", "คุณบุญส่ง", "BL-06", "1,250", 1, "1,250", "0890123456", "Align Left (Text มีลูกน้ำ)", "พิมพ์ลูกน้ำมือเองกลายเป็น Text"],
        ["TR-510", "2026-03-05", "คุณวิภา", "TS-01", 350, 1, 350, "0811122233", "Align Right", "ปกติ"],
        ["TR-511", "2026.03.05", "คุณธนิต", "CR-04", "290", 2, "580", "822233344", "Align Left (จุดในวันที่/Text)", "ใช้วันที่แบบมีจุด + ตัวเลขถูกจัดเป็น Text"],
        ["TR-512", "06/03/2026", "คุณสุดา", "DR-03", 490, 1, 490, "0833344455", "Align Right", "ปกติ"],
        ["TR-513", "2026-03-06", "คุณเจษฎา", "TS-01", "฿ 350", 3, "฿ 1,050", "0844455566", "Align Left", "มีสัญลักษณ์ ฿"],
        ["TR-514", "2569-03-06", "คุณดวงใจ", "JN-02", 890, 1, 890, "855566677", "Align Left (พ.ศ.)", "ปี พ.ศ. 2569 + เบอร์โทรขาด 0"],
        ["TR-515", "2026-03-07", "คุณอนุสรณ์", "HD-05", 650, 1, 650, "0866677788", "Align Right", "ปกติ"],
        ["TR-516", "07/03/2026", "คุณพัชรี", "BL-06", "1,250 บาท", 1, "1,250 บาท", "0877788899", "Align Left", "มีลูกน้ำและคำว่าบาทปน"],
        ["TR-517", "20260307", "คุณกมล", "TS-01", 350, 1, 350, "888899900", "Align Left", "วันที่ 8 หลัก + เบอร์ไม่มี 0"],
        ["TR-518", "2026-03-08", "คุณรุ่งนภา", "CR-04", 290, 2, 580, "0899900011", "Align Right", "ปกติ"],
        ["TR-519", "08/03/2026", "คุณวีระ", "DR-03", "490.-", 1, "490.-", "0812344321", "Align Left", "มีสัญลักษณ์ .-\""],
        ["TR-520", "2026-03-08", "คุณสุนีย์", "JN-02", 890, 1, 890, "823455432", "Align Right", "เบอร์โทร 0 หน้าหาย"],
        ["TR-521", "2026-03-09", "คุณเกรียง", "TS-01", 350, 1, 350, "0834566543", "Align Right", "ปกติ"],
        ["TR-522", "09/03/2026", "คุณกรรณิการ์", "HD-05", "฿ 650", 1, "฿ 650", "0845677654", "Align Left", "มี ฿ ชิดซ้าย"],
        ["TR-523", "2026.03.09", "คุณประดิษฐ์", "BL-06", 1250, 1, 1250, "856788765", "Align Right/Left ปน", "วันที่เพี้ยน + เบอร์โทรขาด 0"],
        ["TR-524", "2026-03-10", "คุณนฤมล", "CR-04", 290, 1, 290, "0867899876", "Align Right", "ปกติ"],
        ["TR-525", "10/03/2026", "คุณสุริยา", "JN-02", "890 บาท", 1, "890 บาท", "0878900987", "Align Left", "มีคำว่าบาทกลายเป็น Text"]
    ]
    
    for c_idx, h in enumerate(headers, 1):
        cell = ws.cell(row=1, column=c_idx, value=h)
        cell.font = styles["font_header"]
        cell.fill = styles["fill_header"]
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = styles["thin_border"]
        
    for r_idx, row_data in enumerate(rows, 2):
        is_align_left_issue = "Align Left" in row_data[8]
        for c_idx, val in enumerate(row_data, 1):
            cell = ws.cell(row=r_idx, column=c_idx, value=val)
            cell.font = styles["font_data"]
            cell.border = styles["thin_border"]
            
            if is_align_left_issue:
                if c_idx in [2, 5, 7, 8, 9]:
                    cell.fill = styles["fill_bad"]
            if c_idx in [5, 6, 7]:
                if isinstance(val, (int, float)):
                    cell.alignment = Alignment(horizontal="right")
                    cell.number_format = "#,##0"
                else:
                    cell.alignment = Alignment(horizontal="left") # visually show text error
            elif c_idx in [1, 2, 4, 8]:
                cell.alignment = Alignment(horizontal="center")
                
    auto_fit_columns(ws, len(headers))
    
    why_bad = [
        "กฎ Alignment ใน Sheets: ตัวเลขและวันที่จริงจะชิดขวา (Right) เสมอ แต่ตารางนี้ชิดซ้าย (Left) เพราะมีอักขระพิเศษ",
        "สูตร SUM ได้ผลลัพธ์เป็น 0: เมื่อเซลล์ราคาเป็น Text โปรแกรมจะข้ามการคำนวณ ทำให้ยอดขายหายไปจากรายงาน",
        "เบอร์โทรศัพท์สูญเสียเลข 0 นำหน้า: หากเก็บเป็น Number เลข 081 จะกลายเป็น 81 ส่ง SMS ติดต่อลูกค้าไม่ได้",
        "วันที่สลับ ว/ด/ป กับ ด/ว/ป: ไม่สามารถเรียงลำดับตามเวลา Timeline ได้ และสรุปยอดขายรายเดือนผิดพลาด"
    ]
    how_to_fix = [
        "ใช้เมนู Format > Number > Number (1,000.00) จัดการใส่ลูกน้ำแทนการพิมพ์มือ",
        "ใช้สูตร =VALUE(SUBSTITUTE(SUBSTITUTE(E2, '฿', ''), 'บาท', '')) แปลงข้อความกลับเป็นตัวเลขแท้จริง",
        "ตั้งฟอร์แมตเบอร์โทรศัพท์เป็น 'Plain text' เสมอเพื่อรักษาเลข 0 ข้างหน้า",
        "ใช้วันที่มาตรฐานสากล YYYY-MM-DD (ISO 8601) และปรับ Locale ใน File > Settings ให้ถูกต้อง"
    ]
    create_explanation_sheet(wb, "กับดักที่ 4: ความโกลาหลของวันที่และตัวเลข (Format Chaos)", "ไฟล์ตัวอย่างยอดขายที่ตัวเลขและวันที่กลายเป็นข้อความ (Text ชิดซ้าย) ทำให้สูตร SUM คำนวณไม่ติด", "Trap 4", "Format Chaos", "ตัวเลขมีสัญลักษณ์ ฿, ลูกน้ำ, หรือคำว่าบาทปะปน และวันที่บันทึกหลายฟอร์แมตปนกัน", why_bad, how_to_fix, "Format > Number, =VALUE(), =SUBSTITUTE(), Date formatting YYYY-MM-DD")
    
    wb.save(os.path.join(OUTPUT_DIR, "bad_data_04_date_and_number_format_chaos.xlsx"))
    print("Generated: bad_data_04_date_and_number_format_chaos.xlsx")

# ==============================================================================
# 5. TRAP 5: OUTLIERS & ANOMALIES (bad_data_05_outliers_and_anomalies.xlsx)
# ==============================================================================
def generate_trap_05():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "orders_outliers_trap"
    styles = get_base_styles()
    
    headers = ["Order_ID", "Date", "Customer_Name", "Product_Name", "Unit_Price", "Quantity", "Total_Amount", "Discount_Pct", "Note_Outlier_Audit"]
    
    rows = [
        ["ORD-701", "2026-03-01", "คุณวิศรุต", "เสื้อยืด Oversize", 350, 1, 350, "0%", "ปกติ"],
        ["ORD-702", "2026-03-01", "คุณนารี", "กางเกงยีนส์คาร์โก้", 890, 2, 1780, "5%", "ปกติ"],
        ["ORD-703", "2026-03-01", "คุณธนาคาร", "เดรสผ้าซาติน", 450, 999, 449550, "0%", "Outlier! คีย์จำนวนเบิ้ล 999 ชิ้น (ยอดพุ่ง 4 แสน)"],
        ["ORD-704", "2026-03-02", "คุณศิริ", "เสื้อครอปไหมพรม", 290, 1, 290, "0%", "ปกติ"],
        ["ORD-705", "2026-03-02", "คุณพงศธร", "กางเกงสแล็คทำงาน", -690, 1, -690, "0%", "Outlier! ราคาสินค้าติดลบ -690 บาท"],
        ["ORD-706", "2026-03-02", "คุณมาลินี", "เสื้อยืด Oversize", 350, 2, 700, "10%", "ปกติ"],
        ["ORD-707", "2026-03-03", "คุณจิรศักดิ์", "เสื้อฮู้ดดี้แขนยาว", 650, 1, 650, "0%", "ปกติ"],
        ["ORD-708", "2026-03-03", "คุณพรสวรรค์", "กระเป๋าผ้าแคนวาส", 199, 1, 199, "150%", "Outlier! ส่วนลดหลุดโลก 150% (เกิน 100%)"],
        ["ORD-709", "2026-03-03", "คุณทินกร", "กางเกงยีนส์ขากระบอก", 890, 1, 890, "0%", "ปกติ"],
        ["ORD-710", "2026-03-04", "คุณอรอนงค์", "เดรสผ้าซาติน", 450, 1, 450, "0%", "ปกติ"],
        ["ORD-711", "2026-03-04", "คุณเฉลิมชัย", "เสื้อเบลเซอร์ลำลอง", 890, 2, 1780, "5%", "ปกติ"],
        ["ORD-712", "2026-03-04", "คุณกัญญารัตน์", "เสื้อยืด Oversize", 350, 1, 350, "0%", "ปกติ"],
        ["ORD-713", "2026-03-05", "คุณมนตรี", "เสื้อโปโลคลาสสิก", 450, 5000, 2250000, "0%", "Outlier! คีย์ยอด 5,000 ตัว ยอดขายพุ่ง 2.2 ล้าน"],
        ["ORD-714", "2026-03-05", "คุณจารุณี", "เสื้อครอปไหมพรม", 290, 1, 290, "0%", "ปกติ"],
        ["ORD-715", "2026-03-05", "คุณอภิสิทธิ์", "กางเกงสแล็คทำงาน", 690, 1, 690, "0%", "ปกติ"],
        ["ORD-716", "2026-03-06", "คุณสุดารัตน์", "เสื้อยืด Oversize", 350, 2, 700, "0%", "ปกติ"],
        ["ORD-717", "2026-03-06", "คุณธเนศ", "กางเกงยีนส์คาร์โก้", 890, 1, 890, "5%", "ปกติ"],
        ["ORD-718", "2026-03-06", "คุณวรรณา", "เดรสผ้าซาติน", 450, 1, -450, "0%", "Outlier! ยอดรวมติดลบ -450 บาท"],
        ["ORD-719", "2026-03-07", "คุณสุรศักดิ์", "เสื้อฮู้ดดี้แขนยาว", 650, 2, 1300, "0%", "ปกติ"],
        ["ORD-720", "2026-03-07", "คุณปานทิพย์", "กระเป๋าผ้าแคนวาส", 199, 1, 199, "0%", "ปกติ"],
        ["ORD-721", "2026-03-07", "คุณเกรียงเดช", "เสื้อเบลเซอร์ลำลอง", 890, 1, 890, "10%", "ปกติ"],
        ["ORD-722", "2026-03-08", "คุณรพีพร", "เสื้อยืด Oversize", 350, 1, 350, "0%", "ปกติ"],
        ["ORD-723", "2026-03-08", "คุณโสภณ", "เสื้อโปโลคลาสสิก", 450, 1, 450, "0%", "ปกติ"],
        ["ORD-724", "2026-03-08", "คุณกานติมา", "กางเกงยีนส์ขากระบอก", 890, 2, 1780, "0%", "ปกติ"],
        ["ORD-725", "2026-03-08", "คุณพิพัฒน์", "เสื้อยืด Oversize", 350, 1, 350, "0%", "ปกติ"]
    ]
    
    for c_idx, h in enumerate(headers, 1):
        cell = ws.cell(row=1, column=c_idx, value=h)
        cell.font = styles["font_header"]
        cell.fill = styles["fill_header"]
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = styles["thin_border"]
        
    for r_idx, row_data in enumerate(rows, 2):
        is_outlier = "Outlier" in row_data[8]
        for c_idx, val in enumerate(row_data, 1):
            cell = ws.cell(row=r_idx, column=c_idx, value=val)
            cell.font = styles["font_data"]
            cell.border = styles["thin_border"]
            
            if is_outlier:
                cell.fill = styles["fill_bad"]
                if c_idx in [5, 6, 7, 8]:
                    cell.font = Font(name="Noto Sans Thai", size=10, bold=True, color="9F1239")
                    cell.fill = styles["fill_bad_cell"]
                    
            if c_idx in [5, 6, 7]:
                cell.alignment = Alignment(horizontal="right")
                if isinstance(val, (int, float)):
                    cell.number_format = "#,##0"
            elif c_idx in [1, 2, 8]:
                cell.alignment = Alignment(horizontal="center")
                
    # Add Summary Statistics rows at bottom
    last_row = len(rows) + 2
    ws.cell(row=last_row, column=6, value="ค่าเฉลี่ย (Mean):").font = styles["font_bold"]
    cell_mean = ws.cell(row=last_row, column=7, value=f"=AVERAGE(G2:G{last_row-1})")
    cell_mean.font = Font(name="Noto Sans Thai", size=11, bold=True, color="BE123C")
    cell_mean.fill = styles["fill_bad"]
    cell_mean.number_format = "#,##0.00"
    
    ws.cell(row=last_row+1, column=6, value="ค่ามัธยฐาน (Median):").font = styles["font_bold"]
    cell_med = ws.cell(row=last_row+1, column=7, value=f"=MEDIAN(G2:G{last_row-1})")
    cell_med.font = Font(name="Noto Sans Thai", size=11, bold=True, color="15803D")
    cell_med.fill = styles["fill_fix"]
    cell_med.number_format = "#,##0.00"
    
    ws.cell(row=last_row, column=9, value="⬅️ ยอดเฉลี่ยเพี้ยนทะลุ 100,000+ บาท เพราะมีบิลหลุดโลก!").font = styles["font_muted"]
    ws.cell(row=last_row+1, column=9, value="⬅️ มัธยฐาน 650 บาท สะท้อนยอดซื้อจริงของลูกค้าทั่วไป").font = styles["font_muted"]
    
    auto_fit_columns(ws, len(headers))
    
    why_bad = [
        "ค่าเฉลี่ย (Mean) พังทลาย: ออเดอร์ 5,000 ชิ้น และยอดติดลบ ดึงยอดเฉลี่ยจาก 600 บาท พุ่งกลายเป็นหลักแสน!",
        "วางแผนสต็อกผิดพลาด: ฝ่ายจัดซื้อเตรียมผ้าตัดเสื้อเป็นพันตัวจนเงินจม เพราะดูตัวเลข Mean ที่บิดเบือน",
        "AI วิเคราะห์หลอน: ป้อนข้อมูลนี้ให้ AI สรุปกลยุทธ์ AI จะแนะนำให้ขยายโรงงานผลิตเดรสเพราะเข้าใจผิดว่าเป็นลูกค้ารายย่อยซื้อเยอะ"
    ]
    how_to_fix = [
        "สแกนหาค่า Min และ Max ด้วยการ Sort คอลัมน์ตัวเลข จากน้อยไปมาก และมากไปน้อย",
        "เปิด Filter กรองดูค่าติดลบ (< 0) หรือค่าเกินจริง (> 10,000)",
        "ใช้ค่ามัธยฐาน (Median) แทนค่าเฉลี่ย (Mean) ในการดูพฤติกรรมลูกค้าทั่วไป",
        "ใช้ Data Validation ล็อกช่วงตัวเลข เช่น Qty ต้องอยู่ระหว่าง 1 ถึง 50 ชิ้น ป้องกันพนักงานคีย์เบิ้ล"
    ]
    create_explanation_sheet(wb, "กับดักที่ 5: ค่าผิดปกติหลุดโลก (Outliers & Anomalies)", "ไฟล์ตัวอย่างยอดขายที่มีตัวเลขสุดโต่ง ยอดติดลบ และจำนวน 999 ชิ้น จนดึงค่าเฉลี่ยเพี้ยน", "Trap 5", "Outliers & Anomalies", "ค่าสุดโต่งจากการพิมพ์ผิด แป้นพิมพ์ค้าง หรือระบบรวน ส่งผลกระทบอย่างรุนแรงต่อค่าเฉลี่ยเลขคณิต", why_bad, how_to_fix, "Sort Min/Max, Filter (< 0, > Limit), =MEDIAN(), Data Validation")
    
    wb.save(os.path.join(OUTPUT_DIR, "bad_data_05_outliers_and_anomalies.xlsx"))
    print("Generated: bad_data_05_outliers_and_anomalies.xlsx")

# ==============================================================================
# 6. ALL-IN-ONE COMPREHENSIVE (bad_data_all_traps_comprehensive.xlsx)
# ==============================================================================
def generate_comprehensive_file():
    wb = openpyxl.Workbook()
    styles = get_base_styles()
    
    # Sheet 1: Raw Data with all 5 traps
    ws_raw = wb.active
    ws_raw.title = "raw_data_with_all_traps"
    
    headers = ["Order_ID", "Date", "Customer_Name", "Product_Name", "Color", "Size", "Quantity", "Price", "Total_Amount", "Channel", "Traps_Identified"]
    
    raw_rows = [
        ["ORD-901", "2026-03-01", "คุณกานดา", "เสื้อยืด Oversize", "ขาว", "M", 1, 350, 350, "TikTok", "ปกติ"],
        ["ORD-902", "2026-03-01", "คุณวิชัย", "กางเกงยีนส์คาร์โก้", "ยีนส์เข้ม", "L", 2, 890, 1780, "Shopee", "Trap 1: แถวซ้ำ (Row 1)"],
        ["ORD-902", "2026-03-01", "คุณวิชัย", "กางเกงยีนส์คาร์โก้", "ยีนส์เข้ม", "L", 2, 890, 1780, "Shopee", "Trap 1: แถวซ้ำ (Row 2 - Exact Duplicate)"],
        ["ORD-903", "02/03/2026", "คุณเมย์", "เสื้อยืด Oversize", " White ", "m", 1, 350, 350, "TikTok", "Trap 2 & 4: ช่องว่างแฝง + White + ไซส์ m + วันที่ ว/ด/ป"],
        ["ORD-904", "2026-03-02", "คุณพงษ์", "เดรสผ้าซาติน", "ฟ้า", "M", 999, 450, 449550, "LINE OA", "Trap 5: Outlier สั่งซื้อ 999 ชิ้น"],
        ["ORD-905", "2026-03-02", "คุณแอน", "เสื้อครอปไหมพรม", "ชมพู", "s", 1, None, 0, "TikTok", "Trap 3: ช่องราคาว่าง (Missing Price)"],
        ["ORD-906", "2026-03-03", "คุณเอก", "เสื้อยืด Oversize", "  ขาว  ", "XL", 1, 350, 350, "หน้าร้าน", "Trap 2: ช่องว่างแฝงหน้าหลัง 2 เคาะ"],
        ["ORD-907", "2569/03/03", "คุณนุช", "กางเกงสแล็คทำงาน", "ดำ", "32", 1, "฿ 690", "฿ 690", "Shopee", "Trap 4: วันที่ปี พ.ศ. + ราคามีสัญลักษณ์ ฿ (Text)"],
        ["ORD-908", "2026-03-03", "คุณตั้ม", "เสื้อฮู้ดดี้แขนยาว", "เทา", "XL", 1, 650, 650, "TikTok", "ปกติ"],
        ["ORD-909", "2026-03-04", "คุณโบว์", "เสื้อยืด Oversize", "ขาว", "S", 2, 350, 700, "หน้าร้าน", "ปกติ"],
        ["ORD-910", "2026-03-04", "คุณชาญ", "กระเป๋าผ้าแคนวาส", "ดำ", "Free", 1, -199, -199, "LINE OA", "Trap 5: ราคาสินค้าติดลบ -199 บาท"],
        ["ORD-911", "05/03/2026", "คุณดาริน", "เดรสผ้าซาติน", "ขาวออฟไวท์", "L", 1, 450, 450, "TikTok", "Trap 2 & 4: สีสะกดนอกมาตรฐาน + วันที่ ว/ด/ป"],
        ["ORD-912", "2026-03-05", "คุณธีระ", "กางเกงยีนส์ขากระบอก", "ยีนส์เข้ม", "xl", 1, 890, 890, "Shopee", "Trap 2: ไซส์ตัวพิมพ์เล็ก 'xl'"],
        ["ORD-913", "2026-03-05", "คุณนภาพร", "เสื้อเชิ้ตโอเวอร์ไซส์", "ขาว", "M", 2, "420.-", "840.-", "หน้าร้าน", "Trap 4: ราคามี .-\" กลายเป็น Text ชิดซ้าย"],
        ["ORD-914", "2026-03-06", "คุณวราภรณ์", "เสื้อยืด Oversize", "ดำ", "L", 1, 350, 350, "TikTok", "Trap 1: แถวซ้ำ (Row 1)"],
        ["ORD-914", "2026-03-06", "คุณวราภรณ์", "เสื้อยืด Oversize", "ดำ", "L", 1, 350, 350, "TikTok", "Trap 1: แถวซ้ำ (Row 2 - Exact Duplicate)"],
        ["ORD-915", "2026-03-06", "คุณพิเชษฐ์", "เสื้อเบลเซอร์ลำลอง", "เบจ", "L", 1, 890, 890, "LINE OA", "ปกติ"],
        ["ORD-916", "2026-03-06", "คุณมณีรัตน์", "เสื้อครอปไหมพรม", "ครีม", "Free", 1, 290, 290, "หน้าร้าน", "ปกติ"],
        ["ORD-917", "2026-03-07", "คุณอนุพงศ์", "กางเกงสแล็คทำงาน", "ดำ", "34", 1, 690, 690, "Shopee", "ปกติ"],
        ["ORD-918", "2026-03-07", "คุณศิริพร", "เสื้อยืด Oversize", " ชมพู ", "m", 1, 350, 350, "TikTok", "Trap 2: ช่องว่างแฝงสี + ไซส์ตัวเล็ก"],
        ["ORD-919", "2026-03-07", "คุณเกรียงไกร", "เสื้อโปโลคลาสสิก", "กรมท่า", "XXL", 1, None, 0, "หน้าร้าน", "Trap 3: ราคาเว้นว่าง (Missing)"],
        ["ORD-920", "2026-03-08", "คุณลลิตา", "เดรสผ้าซาติน", "ฟ้า", "M", 1, 450, 450, "TikTok", "ปกติ"],
        ["ORD-921", "2026-03-08", "คุณอดิศร", "แจ็คเก็ตยีนส์ย้อนยุค", "ยีนส์ฟอก", "XL", 1, 990, 990, "Shopee", "ปกติ"],
        ["ORD-922", "2026-03-08", "คุณนงลักษณ์", "เสื้อยืด Oversize", "ขาว", "S", 1, 350, 350, "LINE OA", "ปกติ"],
        ["ORD-923", "2026-03-09", "คุณธนกร", "กางเกงขาสั้นชิโน", "กากี", "32", 1, 390, 390, "หน้าร้าน", "ปกติ"]
    ]
    
    for c_idx, h in enumerate(headers, 1):
        cell = ws_raw.cell(row=1, column=c_idx, value=h)
        cell.font = styles["font_header"]
        cell.fill = styles["fill_header"]
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = styles["thin_border"]
        
    for r_idx, row_data in enumerate(raw_rows, 2):
        has_trap = row_data[10] != "ปกติ"
        for c_idx, val in enumerate(row_data, 1):
            cell = ws_raw.cell(row=r_idx, column=c_idx, value=val)
            cell.font = styles["font_data"]
            cell.border = styles["thin_border"]
            if has_trap:
                if c_idx == 11:
                    cell.fill = styles["fill_warning"]
                    cell.font = Font(name="Noto Sans Thai", size=9, bold=True, color="92400E")
                elif "Trap 1" in row_data[10] and "Row 2" in row_data[10]:
                    cell.fill = styles["fill_bad"]
                elif "Trap 3" in row_data[10] and c_idx in [8, 9]:
                    cell.fill = styles["fill_bad_cell"]
                elif "Trap 5" in row_data[10] and c_idx in [7, 8, 9]:
                    cell.fill = styles["fill_bad_cell"]
            if c_idx in [7, 8, 9]:
                if isinstance(val, (int, float)):
                    cell.alignment = Alignment(horizontal="right")
                    cell.number_format = "#,##0"
                else:
                    cell.alignment = Alignment(horizontal="left")
            elif c_idx in [1, 2, 5, 6, 10]:
                cell.alignment = Alignment(horizontal="center")
                
    auto_fit_columns(ws_raw, len(headers))
    
    # Sheet 2: Cleaned Data Solution (ตารางเฉลยที่คลีนแล้ว)
    ws_clean = wb.create_sheet(title="cleaned_data_solution")
    clean_headers = ["Order_ID", "Date", "Customer_Name", "Product_Name", "Color", "Size", "Quantity", "Price", "Total_Amount", "Channel", "Clean_Status"]
    
    clean_rows = [
        ["ORD-901", "2026-03-01", "คุณกานดา", "เสื้อยืด Oversize", "ขาว", "M", 1, 350, 350, "TikTok", "Cleaned 100%"],
        ["ORD-902", "2026-03-01", "คุณวิชัย", "กางเกงยีนส์คาร์โก้", "ยีนส์เข้ม", "L", 2, 890, 1780, "Shopee", "ลบแถวซ้ำออก 1 แถว"],
        ["ORD-903", "2026-03-02", "คุณเมย์", "เสื้อยืด Oversize", "ขาว", "M", 1, 350, 350, "TikTok", "Trim space, ปรับสีเป็น 'ขาว', ไซส์เป็น 'M', วันที่เป็น YYYY-MM-DD"],
        ["ORD-904", "2026-03-02", "คุณพงษ์", "เดรสผ้าซาติน", "ฟ้า", "M", 1, 450, 450, "LINE OA", "แก้ Outlier จาก 999 เป็น 1 ตัวตามสลิปจริง"],
        ["ORD-905", "2026-03-02", "คุณแอน", "เสื้อครอปไหมพรม", "ชมพู", "S", 1, 290, 290, "TikTok", "เติม Missing Price 290 บาทจาก Master Catalog"],
        ["ORD-906", "2026-03-03", "คุณเอก", "เสื้อยืด Oversize", "ขาว", "XL", 1, 350, 350, "หน้าร้าน", "Trim ช่องว่างแฝงหน้าหลัง"],
        ["ORD-907", "2026-03-03", "คุณนุช", "กางเกงสแล็คทำงาน", "ดำ", "32", 1, 690, 690, "Shopee", "แปลง พ.ศ. เป็น ค.ศ. และแปลงราคาเป็นตัวเลขชิดขวา"],
        ["ORD-908", "2026-03-03", "คุณตั้ม", "เสื้อฮู้ดดี้แขนยาว", "เทา", "XL", 1, 650, 650, "TikTok", "Cleaned 100%"],
        ["ORD-909", "2026-03-04", "คุณโบว์", "เสื้อยืด Oversize", "ขาว", "S", 2, 350, 700, "หน้าร้าน", "Cleaned 100%"],
        ["ORD-910", "2026-03-04", "คุณชาญ", "กระเป๋าผ้าแคนวาส", "ดำ", "Free", 1, 199, 199, "LINE OA", "แก้ราคาติดลบเป็นบวก 199 บาท"],
        ["ORD-911", "2026-03-05", "คุณดาริน", "เดรสผ้าซาติน", "ขาว", "L", 1, 450, 450, "TikTok", "แก้สี 'ขาวออฟไวท์' เป็น 'ขาว' + จัดรูปแบบวันที่"],
        ["ORD-912", "2026-03-05", "คุณธีระ", "กางเกงยีนส์ขากระบอก", "ยีนส์เข้ม", "XL", 1, 890, 890, "Shopee", "ปรับไซส์ 'xl' เป็น 'XL' ด้วย =UPPER()"],
        ["ORD-913", "2026-03-05", "คุณนภาพร", "เสื้อเชิ้ตโอเวอร์ไซส์", "ขาว", "M", 2, 420, 840, "หน้าร้าน", "ตัด .-\" ออก แปลงเป็นตัวเลข"],
        ["ORD-914", "2026-03-06", "คุณวราภรณ์", "เสื้อยืด Oversize", "ดำ", "L", 1, 350, 350, "TikTok", "ลบแถวซ้ำออก 1 แถว"],
        ["ORD-915", "2026-03-06", "คุณพิเชษฐ์", "เสื้อเบลเซอร์ลำลอง", "เบจ", "L", 1, 890, 890, "LINE OA", "Cleaned 100%"],
        ["ORD-916", "2026-03-06", "คุณมณีรัตน์", "เสื้อครอปไหมพรม", "ครีม", "Free", 1, 290, 290, "หน้าร้าน", "Cleaned 100%"],
        ["ORD-917", "2026-03-07", "คุณอนุพงศ์", "กางเกงสแล็คทำงาน", "ดำ", "34", 1, 690, 690, "Shopee", "Cleaned 100%"],
        ["ORD-918", "2026-03-07", "คุณศิริพร", "เสื้อยืด Oversize", "ชมพู", "M", 1, 350, 350, "TikTok", "Trim whitespace และปรับไซส์เป็น M"],
        ["ORD-919", "2026-03-07", "คุณเกรียงไกร", "เสื้อโปโลคลาสสิก", "กรมท่า", "XXL", 1, 450, 450, "หน้าร้าน", "เติมราคา 450 บาท"],
        ["ORD-920", "2026-03-08", "คุณลลิตา", "เดรสผ้าซาติน", "ฟ้า", "M", 1, 450, 450, "TikTok", "Cleaned 100%"],
        ["ORD-921", "2026-03-08", "คุณอดิศร", "แจ็คเก็ตยีนส์ย้อนยุค", "ยีนส์ฟอก", "XL", 1, 990, 990, "Shopee", "Cleaned 100%"],
        ["ORD-922", "2026-03-08", "คุณนงลักษณ์", "เสื้อยืด Oversize", "ขาว", "S", 1, 350, 350, "LINE OA", "Cleaned 100%"],
        ["ORD-923", "2026-03-09", "คุณธนกร", "กางเกงขาสั้นชิโน", "กากี", "32", 1, 390, 390, "หน้าร้าน", "Cleaned 100%"]
    ]
    
    fill_clean_header = PatternFill(start_color="065F46", end_color="065F46", fill_type="solid") # Emerald 800
    for c_idx, h in enumerate(clean_headers, 1):
        cell = ws_clean.cell(row=1, column=c_idx, value=h)
        cell.font = styles["font_header"]
        cell.fill = fill_clean_header
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = styles["thin_border"]
        
    for r_idx, row_data in enumerate(clean_rows, 2):
        for c_idx, val in enumerate(row_data, 1):
            cell = ws_clean.cell(row=r_idx, column=c_idx, value=val)
            cell.font = styles["font_data"]
            cell.border = styles["thin_border"]
            if c_idx == 11:
                cell.fill = styles["fill_fix"]
                cell.font = Font(name="Noto Sans Thai", size=9, bold=True, color="065F46")
            if c_idx in [7, 8, 9]:
                cell.alignment = Alignment(horizontal="right")
                cell.number_format = "#,##0"
            elif c_idx in [1, 2, 5, 6, 10]:
                cell.alignment = Alignment(horizontal="center")
                
    auto_fit_columns(ws_clean, len(clean_headers))
    
    # Sheet 3: Data Cleaning Log (สมุดบันทึกประวัติการชำระข้อมูล)
    ws_log = wb.create_sheet(title="data_cleaning_log")
    log_headers = ["Log_ID", "Timestamp", "Target_Column", "Issue_Detected", "Action_Tool_Used", "Rows_Affected", "Operator", "Verification_Result"]
    log_data = [
        ["LOG-01", "2026-03-23 10:00", "Order_ID (All)", "ออเดอร์ซ้ำซ้อนจากระบบ Shopee และ TikTok (ORD-902, ORD-914)", "Data > Remove duplicates (เช็ค Order_ID)", "2 แถวถูกลบ", "สมชาย (Project Lead)", "คงเหลือ 23 แถว ยอดขายไม่พองซ้ำซ้อน"],
        ["LOG-02", "2026-03-23 10:05", "Color, Size", "มีช่องว่างแฝงหน้า-หลังคำว่า 'ขาว', 'ชมพู' ('  ขาว  ')", "Data > Trim whitespace & สูตร =TRIM()", "3 แถว", "กานดา (Sheet Master)", "ตัดช่องว่างสำเร็จ Pivot Table รวมกลุ่มได้"],
        ["LOG-03", "2026-03-23 10:10", "Color", "สีสินค้าใช้คำปะปน ('White', 'ขาวออฟไวท์')", "Edit > Find & Replace (Ctrl+H) ติ๊ก Match entire cell", "2 แถว", "กานดา (Sheet Master)", "ปรับเป็นคำมาตรฐาน 'ขาว' ทั้งหมด"],
        ["LOG-04", "2026-03-23 10:15", "Size", "ขนาดไซส์เสื้อบันทึกเป็นตัวพิมพ์เล็ก ('m', 's', 'xl')", "สูตร =UPPER() แปลงเป็นตัวพิมพ์ใหญ่", "4 แถว", "ดาริน (Data Auditor)", "เป็น 'S', 'M', 'XL' ตามมาตรฐานสากล"],
        ["LOG-05", "2026-03-23 10:20", "Price, Total_Amount", "เซลล์ราคาว่างเปล่า (ORD-905 เสื้อครอป, ORD-919 โปโล)", "Imputation: ดึงราคาจาก Master Menu (290 บ., 450 บ.)", "2 แถว", "วิชัย (Log Keeper)", "คำนวณยอดเงินรวมได้ครบถ้วน ไม่เป็น 0"],
        ["LOG-06", "2026-03-23 10:25", "Quantity, Price", "Outlier: สั่ง 999 ชิ้น (ORD-904) และ ราคาติดลบ -199 บ. (ORD-910)", "ตรวจสอบสลิปจริง แก้ไขเป็น 1 ชิ้น และยอดบวก 199 บ.", "2 แถว", "สมชาย (Project Lead)", "ยอดขายเฉลี่ยกลับสู่ระดับปกติที่ 600-800 บาท"],
        ["LOG-07", "2026-03-23 10:30", "Date, Price", "วันที่ปี พ.ศ. 2569 และราคามีสัญลักษณ์ '฿', '.-' ชิดซ้าย", "แปลง พ.ศ. เป็น ค.ศ. และใช้ Format > Number", "3 แถว", "กานดา (Sheet Master)", "ตัวเลขชิดขวาทั้งหมด พร้อมคำนวณและป้อน AI"]
    ]
    
    fill_log_header = PatternFill(start_color="1E1B4B", end_color="1E1B4B", fill_type="solid")
    for c_idx, h in enumerate(log_headers, 1):
        cell = ws_log.cell(row=1, column=c_idx, value=h)
        cell.font = styles["font_header"]
        cell.fill = fill_log_header
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = styles["thin_border"]
        
    for r_idx, row_data in enumerate(log_data, 2):
        for c_idx, val in enumerate(row_data, 1):
            cell = ws_log.cell(row=r_idx, column=c_idx, value=val)
            cell.font = styles["font_data"]
            cell.border = styles["thin_border"]
            if c_idx in [1, 2]:
                cell.alignment = Alignment(horizontal="center")
            elif c_idx == 6:
                cell.alignment = Alignment(horizontal="center")
                cell.fill = styles["fill_fix"]
                cell.font = Font(name="Noto Sans Thai", size=9, bold=True, color="065F46")
                
    auto_fit_columns(ws_log, len(log_headers))
    
    # Sheet 4: Explanation & Guide
    why_bad = [
        "ข้อมูลธุรกิจจริงไม่เคยมีข้อผิดพลาดแค่แบบเดียว แต่มักเจอผสมปนเปกันทั้ง 5 Traps",
        "หากไม่จัดลำดับขั้นตอนการคลีน อาจเผลอลบข้อมูลสำคัญ หรือแปลงข้อมูลจนผิดเพี้ยนถาวร",
        "การแก้ไขทับไฟล์ดิบโดยตรงถือเป็นหายนะ เพราะไม่สามารถตรวจสอบย้อนกลับ (Audit) ได้"
    ]
    how_to_fix = [
        "Step 1: Backup Raw Data ทำสำเนาเป็น cleaned_data เสมอ (ห้ามแตะต้อง raw_data)",
        "Step 2: Remove Duplicates ลบแถวซ้ำซ้อนออกก่อนเป็นอันดับแรก",
        "Step 3: Trim Whitespace & Canonical Text ล้างช่องว่างและสะกดมาตรฐานเดียวกัน",
        "Step 4: Handle Missing & Outliers ตรวจหาเซลล์ว่างและแก้ค่าหลุดโลกตามสลิปจริง",
        "Step 5: Document Everything บันทึกทุกขั้นตอนลงใน Data Cleaning Log ครบ 6 องค์ประกอบ"
    ]
    create_explanation_sheet(wb, "ชุดข้อมูลจำลองเสมือนจริง: ปฏิบัติการกู้วิกฤตข้อมูลร้านชบา โคลทติ้ง", "ตารางรวม 5 กับดักข้อมูลสกปรกครบถ้วน สำหรับฝึกซ้อมกระบวนการ Data Cleaning แบบ End-to-End", "Master Dataset", "All 5 Traps Comprehensive", "ชุดข้อมูลยอดขาย 25 แถวที่มีทั้ง Duplicate, Whitespace, Typos, Missing, Format Chaos, และ Outliers ครบในไฟล์เดียว", why_bad, how_to_fix, "Data cleanup, TRIM, UPPER, PROPER, Find/Replace, Format Number/Date, Validation, Cleaning Log")
    
    wb.save(os.path.join(OUTPUT_DIR, "bad_data_all_traps_comprehensive.xlsx"))
    print("Generated: bad_data_all_traps_comprehensive.xlsx")

if __name__ == "__main__":
    generate_trap_01()
    generate_trap_02()
    generate_trap_03()
    generate_trap_04()
    generate_trap_05()
    generate_comprehensive_file()
    try:
        from combine_bad_data_traps import build_combined_workbook
        build_combined_workbook()
    except Exception as e:
        print(f"Combined file generation note: {e}")
    print("All Session 05 Bad Data files generated successfully!")

