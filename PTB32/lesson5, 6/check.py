# Nhập số điện đã tiêu thụ
kWh = int(input("Nhập số điện đã tiêu thụ: "))
# Biến lưu trữ tổng tiền tính theo hóa đơn
bill = 0
# ính số tiền điện theo đơn giá kWh tiêu thụ
if kWh <= 50:
    bill = kWh * 1700
elif kWh <= 100:
    bill = 50 * 1700 + (kWh - 50) * 1900
elif kWh <= 200:
    bill = 50 * 1700 + 50 * 1900 + (kWh - 100) * 2100
else:
    bill = 50 * 1700 + 50 * 1900 + 100 * 2100 + (kWh - 200) * 3000
# In ra số tiền mà người dùng phải trả
print(f"Số tiền cần phải trả là: {bill}vnd ")            