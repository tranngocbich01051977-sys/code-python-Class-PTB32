  # Bài 1: Viết chương trình nhập vào 3 cạnh của tam giác.
a = int(input("Nhập giá trị của cạnh thứ nhất tam giác: "))
b = int(input("Nhập giá trị của cạnh thứ hai tam giác: "))
c = int(input("Nhập giá trị của cạnh thứ ba tam giác: "))
while True:
    if a == 3 and b == 4 and c == 5:
        print("Tam giác vuông")
        break
    elif a == 5 and b == 5 and c == 5:
        print("Tam giác đều")
        break
    elif a == 4 and b == 4 and c == 6:
        print("Tam giác cân")
        break
    elif a == 4 and b == 5 and c == 6:
        print("Tam giác thường")
        break
    else:
        print("Không phải tam giác")
        break
    
   # Bài 3:
name = input("Nhập tên của bạn: ")
parts = name.split(" ")
if len(parts) == 3:
    first_name = parts[0]
    middle_name = parts[1]
    last_name = parts[2]
    print(f"Tên của bạn là: {last_name}")
    print(f"Tên đệm của bạn là: {middle_name}")
    print(f"Họ của bạn là: {first_name}")

  # Bài 2:
def nam_nhuan(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
def ngay_trong_thang(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if nam_nhuan(year):
            return 29
        else:
            return 28
    else:
        return -1
date = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))