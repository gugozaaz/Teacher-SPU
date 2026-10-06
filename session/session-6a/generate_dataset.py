import csv
import datetime
import random
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

# Seed for reproducible realistic data
random.seed(42)

# Fictional Cartoon Characters with consistent CRM Profiles
CHARACTERS = [
    {"name": "โดราเอมอน", "gender": "ชาย", "age_group": "Gen Y (26-40)", "tier": "Platinum"},
    {"name": "โนบิตะ", "gender": "ชาย", "age_group": "Gen Z (18-25)", "tier": "Regular"},
    {"name": "ชิซุกะ", "gender": "หญิง", "age_group": "Gen Z (18-25)", "tier": "Gold"},
    {"name": "ซูเนโอะ", "gender": "ชาย", "age_group": "Gen Y (26-40)", "tier": "Platinum"},
    {"name": "ไจแอนท์", "gender": "ชาย", "age_group": "Gen Y (26-40)", "tier": "Silver"},
    {"name": "มังกี้ ดี ลูฟี่", "gender": "ชาย", "age_group": "Gen Z (18-25)", "tier": "Gold"},
    {"name": "โรโรโนอา โซโร", "gender": "ชาย", "age_group": "Gen Y (26-40)", "tier": "Silver"},
    {"name": "นามิ", "gender": "หญิง", "age_group": "Gen Y (26-40)", "tier": "Platinum"},
    {"name": "ซันจิ", "gender": "ชาย", "age_group": "Gen Y (26-40)", "tier": "Gold"},
    {"name": "โทนี่ ช็อปเปอร์", "gender": "ชาย", "age_group": "Gen Z (18-25)", "tier": "Regular"},
    {"name": "นิโค โรบิน", "gender": "หญิง", "age_group": "Gen X (41-55)", "tier": "Platinum"},
    {"name": "อาเนีย ฟอร์เจอร์", "gender": "หญิง", "age_group": "Gen Z (18-25)", "tier": "Regular"},
    {"name": "ลอยด์ ฟอร์เจอร์", "gender": "ชาย", "age_group": "Gen Y (26-40)", "tier": "Platinum"},
    {"name": "ยอร์ ฟอร์เจอร์", "gender": "หญิง", "age_group": "Gen Y (26-40)", "tier": "Gold"},
    {"name": "เอโดงาวะ โคนัน", "gender": "ชาย", "age_group": "Gen Z (18-25)", "tier": "Silver"},
    {"name": "โมริ รัน", "gender": "หญิง", "age_group": "Gen Z (18-25)", "tier": "Silver"},
    {"name": "โมริ โคโกโร่", "gender": "ชาย", "age_group": "Gen X (41-55)", "tier": "Regular"},
    {"name": "ไฮบาระ ไอ", "gender": "หญิง", "age_group": "Gen Z (18-25)", "tier": "Gold"},
    {"name": "ชินจัง (โนฮาระ ชินโนะสุเกะ)", "gender": "ชาย", "age_group": "Gen Z (18-25)", "tier": "Regular"},
    {"name": "มิซาเอะ", "gender": "หญิง", "age_group": "Gen X (41-55)", "tier": "Gold"},
    {"name": "ฮิโรชิ", "gender": "ชาย", "age_group": "Gen X (41-55)", "tier": "Silver"},
    {"name": "โกโจ ซาโตรุ", "gender": "ชาย", "age_group": "Gen Y (26-40)", "tier": "Platinum"},
    {"name": "อิตาโดริ ยูจิ", "gender": "ชาย", "age_group": "Gen Z (18-25)", "tier": "Regular"},
    {"name": "ฟุชิงุโระ เมกุมิ", "gender": "ชาย", "age_group": "Gen Z (18-25)", "tier": "Silver"},
    {"name": "คูกิซากิ โนบาระ", "gender": "หญิง", "age_group": "Gen Z (18-25)", "tier": "Gold"},
    {"name": "คามาโดะ ทันจิโร่", "gender": "ชาย", "age_group": "Gen Z (18-25)", "tier": "Silver"},
    {"name": "คามาโดะ เนซึโกะ", "gender": "หญิง", "age_group": "Gen Z (18-25)", "tier": "Gold"},
    {"name": "อากาสึมะ เซ็นอิตสึ", "gender": "ชาย", "age_group": "Gen Z (18-25)", "tier": "Regular"},
    {"name": "ฮาชิบิระ อิโนะสุเกะ", "gender": "ชาย", "age_group": "Gen Z (18-25)", "tier": "Regular"},
    {"name": "เร็นโกคุ เคียวจูโร่", "gender": "ชาย", "age_group": "Gen Y (26-40)", "tier": "Platinum"},
    {"name": "อุซึมากิ นารูโตะ", "gender": "ชาย", "age_group": "Gen Y (26-40)", "tier": "Gold"},
    {"name": "อุจิวะ ซาสึเกะ", "gender": "ชาย", "age_group": "Gen Y (26-40)", "tier": "Silver"},
    {"name": "ฮารุโนะ ซากุระ", "gender": "หญิง", "age_group": "Gen Y (26-40)", "tier": "Silver"},
    {"name": "ฮาตาเกะ คาคาชิ", "gender": "ชาย", "age_group": "Gen X (41-55)", "tier": "Platinum"},
    {"name": "ฮิวงะ ฮินาตะ", "gender": "หญิง", "age_group": "Gen Y (26-40)", "tier": "Gold"},
    {"name": "ปิกาจู", "gender": "ไม่ระบุ", "age_group": "Gen Z (18-25)", "tier": "Platinum"},
    {"name": "ซาโตชิ", "gender": "ชาย", "age_group": "Gen Z (18-25)", "tier": "Silver"},
    {"name": "เซเลอร์มูน (อุซางิ)", "gender": "หญิง", "age_group": "Gen Y (26-40)", "tier": "Gold"},
    {"name": "หน้ากากทักซิโด้", "gender": "ชาย", "age_group": "Gen Y (26-40)", "tier": "Platinum"},
    {"name": "โทโทโร่", "gender": "ไม่ระบุ", "age_group": "Gen X (41-55)", "tier": "Platinum"},
    {"name": "จิฮิโระ", "gender": "หญิง", "age_group": "Gen Z (18-25)", "tier": "Regular"},
    {"name": "ฮากุ", "gender": "ชาย", "age_group": "Gen Z (18-25)", "tier": "Silver"},
    {"name": "ซุน โกคู", "gender": "ชาย", "age_group": "Gen X (41-55)", "tier": "Gold"},
    {"name": "เบจิต้า", "gender": "ชาย", "age_group": "Gen X (41-55)", "tier": "Platinum"},
    {"name": "บลูม่า", "gender": "หญิง", "age_group": "Gen X (41-55)", "tier": "Platinum"},
    {"name": "เอเรน เยเกอร์", "gender": "ชาย", "age_group": "Gen Z (18-25)", "tier": "Regular"},
    {"name": "มิคาสะ แอคเคอร์แมน", "gender": "หญิง", "age_group": "Gen Z (18-25)", "tier": "Gold"},
    {"name": "รีไวล์ แอคเคอร์แมน", "gender": "ชาย", "age_group": "Gen Y (26-40)", "tier": "Platinum"},
    {"name": "คิริโตะ", "gender": "ชาย", "age_group": "Gen Z (18-25)", "tier": "Gold"},
    {"name": "อาสึนะ", "gender": "หญิง", "age_group": "Gen Z (18-25)", "tier": "Platinum"},
]

# Assign Customer IDs
for i, c in enumerate(CHARACTERS, 1):
    c["cust_id"] = f"CUST-{i:03d}"

# Products & Prices
PRODUCTS = [
    # Coffee
    {"category": "Coffee", "name": "Espresso (Single/Double)", "base_price": 65, "sizes": ["Regular"]},
    {"category": "Coffee", "name": "Iced Americano", "base_price": 75, "sizes": ["Regular", "Large"]},
    {"category": "Coffee", "name": "Hot Cafe Latte", "base_price": 80, "sizes": ["Regular"]},
    {"category": "Coffee", "name": "Iced Cafe Latte", "base_price": 85, "sizes": ["Regular", "Large"]},
    {"category": "Coffee", "name": "Iced Caramel Macchiato", "base_price": 95, "sizes": ["Regular", "Large"]},
    {"category": "Coffee", "name": "Signature Cold Brew", "base_price": 105, "sizes": ["Regular"]},
    {"category": "Coffee", "name": "Dirty Coffee", "base_price": 90, "sizes": ["Regular"]},
    # Non-Coffee
    {"category": "Non-Coffee", "name": "Uji Matcha Latte", "base_price": 95, "sizes": ["Regular", "Large"]},
    {"category": "Non-Coffee", "name": "Thai Milk Tea Special", "base_price": 70, "sizes": ["Regular", "Large"]},
    {"category": "Non-Coffee", "name": "Dark Cocoa Extreme", "base_price": 85, "sizes": ["Regular", "Large"]},
    {"category": "Non-Coffee", "name": "Peach Sparking Soda", "base_price": 80, "sizes": ["Regular", "Large"]},
    {"category": "Non-Coffee", "name": "Hojicha Roasted Tea", "base_price": 90, "sizes": ["Regular", "Large"]},
    # Bakery
    {"category": "Bakery", "name": "Butter Croissant", "base_price": 75, "sizes": ["Standard"]},
    {"category": "Bakery", "name": "Almond Cream Croissant", "base_price": 95, "sizes": ["Standard"]},
    {"category": "Bakery", "name": "Chocolate Truffle Croffle", "base_price": 110, "sizes": ["Standard"]},
    {"category": "Bakery", "name": "Basque Burnt Cheesecake", "base_price": 125, "sizes": ["Standard"]},
    {"category": "Bakery", "name": "Carrot Walnut Cake", "base_price": 115, "sizes": ["Standard"]},
    # Merchandise
    {"category": "Merchandise", "name": "Anime Tumbler 500ml", "base_price": 390, "sizes": ["Standard"]},
    {"category": "Merchandise", "name": "House Blend Beans 250g", "base_price": 280, "sizes": ["Standard"]},
]

BRANCHES = ["สาขาสยามสแควร์", "สาขาอารีย์", "สาขาทองหล่อ", "สาขาลาดพร้าว"]
BRANCH_WEIGHTS = [0.38, 0.24, 0.22, 0.16]

CHANNELS = ["หน้าร้าน (Dine-in)", "ซื้อกลับ (Takeaway)", "เดลิเวอรี่ (Delivery)"]
CHANNEL_WEIGHTS = [0.42, 0.38, 0.20]

PAYMENTS = ["QR PromptPay", "บัตรเครดิต", "TrueMoney Wallet", "เงินสด"]
PAYMENT_WEIGHTS = [0.48, 0.28, 0.14, 0.10]

SWEETNESS_LEVELS = ["0% (ไม่หวาน)", "25% (หวานน้อยมาก)", "50% (หวานน้อย)", "100% (หวานปกติ)"]

DAY_NAMES = ["จันทร์", "อังคาร", "พุธ", "พฤหัสบดี", "ศุกร์", "เสาร์", "อาทิตย์"]

START_DATE = datetime.date(2026, 1, 1)
END_DATE = datetime.date(2026, 3, 31)
TOTAL_DAYS = (END_DATE - START_DATE).days + 1

# Generate 1,000 order item rows across multiple orders
TARGET_ROWS = 1000
rows = []
txn_counter = 1

while len(rows) < TARGET_ROWS:
    txn_id = f"TXN-2026-{txn_counter:04d}"
    
    # Date & Day
    random_day_offset = random.randint(0, TOTAL_DAYS - 1)
    trans_date = START_DATE + datetime.timedelta(days=random_day_offset)
    day_name = DAY_NAMES[trans_date.weekday()]
    day_type = "วันหยุด (Weekend)" if trans_date.weekday() >= 5 else "วันธรรมดา (Weekday)"
    
    # Time & Slot (peak in morning 8-10, noon 12-13, afternoon 14-16)
    time_weights = [0.32, 0.28, 0.26, 0.14]
    slot_choice = random.choices(["เช้า (07:00-10:59)", "กลางวัน (11:00-13:59)", "บ่าย (14:00-16:59)", "เย็น (17:00-20:30)"], weights=time_weights)[0]
    
    if slot_choice.startswith("เช้า"):
        hour = random.randint(7, 10)
    elif slot_choice.startswith("กลางวัน"):
        hour = random.randint(11, 13)
    elif slot_choice.startswith("บ่าย"):
        hour = random.randint(14, 16)
    else:
        hour = random.randint(17, 20)
    minute = random.randint(0, 59)
    time_str = f"{hour:02d}:{minute:02d}"
    
    # Customer Selection (85% member cartoon character, 15% Walk-in Guest)
    is_member = random.random() < 0.85
    if is_member:
        char = random.choice(CHARACTERS)
        cust_id = char["cust_id"]
        cust_name = char["name"]
        gender = char["gender"]
        age_group = char["age_group"]
        tier = char["tier"]
    else:
        cust_id = "GUEST"
        cust_name = "ลูกค้าทั่วไป (Walk-in)"
        gender = random.choice(["ชาย", "หญิง", "ไม่ระบุ"])
        age_group = random.choice(["Gen Z (18-25)", "Gen Y (26-40)", "Gen X (41-55)"])
        tier = "Non-Member"
        
    branch = random.choices(BRANCHES, weights=BRANCH_WEIGHTS)[0]
    channel = random.choices(CHANNELS, weights=CHANNEL_WEIGHTS)[0]
    payment = random.choices(PAYMENTS, weights=PAYMENT_WEIGHTS)[0]
    rating = random.choices([5, 4, 3, 2, 1], weights=[0.65, 0.25, 0.06, 0.03, 0.01])[0]
    
    # Discount rate by Tier
    if tier == "Platinum":
        disc_rate = 0.15
    elif tier == "Gold":
        disc_rate = 0.10
    elif tier == "Silver":
        disc_rate = 0.05
    else:
        disc_rate = 0.0

    # Determine how many items are ordered in this transaction
    remaining_rows = TARGET_ROWS - len(rows)
    if remaining_rows == 1:
        num_items = 1
    elif remaining_rows == 2:
        num_items = random.choices([1, 2], weights=[0.60, 0.40])[0]
    elif remaining_rows == 3:
        num_items = random.choices([1, 2, 3], weights=[0.50, 0.35, 0.15])[0]
    else:
        # Multi-item distribution: 1 item (52%), 2 items (32%), 3 items (11%), 4 items (5%)
        num_items = random.choices([1, 2, 3, 4], weights=[0.52, 0.32, 0.11, 0.05])[0]
        num_items = min(num_items, remaining_rows)
        
    # Choose distinct products for this transaction if possible
    chosen_products = random.sample(PRODUCTS, k=min(num_items, len(PRODUCTS)))
    
    for item_idx in range(num_items):
        prod = chosen_products[item_idx]
        cat = prod["category"]
        prod_name = prod["name"]
        base_price = prod["base_price"]
        
        # Size
        size = random.choice(prod["sizes"])
        unit_price = base_price
        if size == "Large":
            unit_price += 15  # Up-size +15 baht
            
        # Sweetness
        if cat in ["Coffee", "Non-Coffee"]:
            if "Cold Brew" in prod_name or "Espresso" in prod_name:
                sweetness = "0% (ไม่หวาน)"
            else:
                sweetness = random.choice(SWEETNESS_LEVELS)
        else:
            sweetness = "-"
            
        # Quantity per line item (mostly 1, sometimes 2)
        qty = random.choices([1, 2], weights=[0.82, 0.18])[0]
        subtotal = unit_price * qty
        
        discount = round(subtotal * disc_rate, 2)
        net_total = round(subtotal - discount, 2)
        points = int(net_total // 25) if is_member else 0
        
        rows.append([
            txn_id,
            trans_date.strftime("%Y-%m-%d"),
            time_str,
            slot_choice,
            day_name,
            day_type,
            cust_id,
            cust_name,
            tier,
            gender,
            age_group,
            branch,
            channel,
            cat,
            prod_name,
            size,
            sweetness,
            unit_price,
            qty,
            subtotal,
            discount,
            net_total,
            payment,
            points,
            rating
        ])
        
    txn_counter += 1

HEADERS = [
    "Transaction_ID", "Date", "Time", "Time_Slot", "Day_of_Week", "Day_Type",
    "Customer_ID", "Customer_Name", "Member_Tier", "Gender", "Age_Group",
    "Branch", "Sales_Channel", "Product_Category", "Product_Name", "Size",
    "Sweetness_Level", "Unit_Price", "Quantity", "Subtotal", "Discount_Baht",
    "Net_Amount", "Payment_Method", "Points_Earned", "Rating_Score"
]

# Write CSV with UTF-8 BOM
csv_path = "session/session-6a/session-6a-coffee-sales-crm.csv"
with open(csv_path, mode="w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(HEADERS)
    writer.writerows(rows)
print(f"Generated CSV: {csv_path} ({len(rows)} rows, {txn_counter - 1} unique transactions)")

# Write Excel (.xlsx) with styled header
wb = Workbook()
ws = wb.active
ws.title = "Coffee_Sales_CRM"

# Colors & styles
header_fill = PatternFill(start_color="1E293B", end_color="1E293B", fill_type="solid") # Dark slate
header_font = Font(name="Noto Sans Thai", size=10, bold=True, color="FFFFFF")
data_font = Font(name="Noto Sans Thai", size=9)
border_thin = Side(border_style="thin", color="CBD5E1")
cell_border = Border(top=border_thin, left=border_thin, right=border_thin, bottom=border_thin)

ws.append(HEADERS)
for col_idx in range(1, len(HEADERS) + 1):
    cell = ws.cell(row=1, column=col_idx)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

for r in rows:
    ws.append(r)

# Format rows
for row_idx in range(2, len(rows) + 2):
    for col_idx in range(1, len(HEADERS) + 1):
        c = ws.cell(row=row_idx, column=col_idx)
        c.font = data_font
        c.border = cell_border
        # Center align ID, Date, Time, etc.
        if col_idx in [1, 2, 3, 5, 7, 9, 10, 16, 25]:
            c.alignment = Alignment(horizontal="center")
        elif col_idx in [18, 19, 20, 21, 22, 24]:
            c.alignment = Alignment(horizontal="right")
            if col_idx in [18, 20, 21, 22]:
                c.number_format = "#,##0.00"

# Adjust column widths
for col in ws.columns:
    max_len = max(len(str(cell.value or '')) for cell in col)
    col_letter = col[0].column_letter
    ws.column_dimensions[col_letter].width = max(max_len + 3, 11)

xlsx_path = "session/session-6a/session-6a-coffee-sales-crm.xlsx"
wb.save(xlsx_path)
print(f"Generated XLSX: {xlsx_path} ({len(rows)} rows, {txn_counter - 1} unique transactions)")
