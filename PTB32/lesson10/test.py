 # Bài 1:
#  Nhập số lượng bài kiểm tra
diem_so = []
n = int(input("Nhập số lượng bài kiểm tra: ")) # 10
# Nhập điểm cho bài kiểm tra
for index in range(n):
    diem = float(input(f"Nhập số điểm cho bài kiểm tra thứ {index + 1}: "))
    diem_so.append(diem)

# Lập trình sắp xếp theo chiều tăng dần (1, 2)
def sap_xep_va_xoa_diem(diem_so):
    # Sắp xếp danh sách tăng dần 
    diem_so.sort()
    # Xóa điểm số nhỏ nhất
    while diem_so[0] == diem_so[1]: # Kiểm tra nếu có 2 số nhỏ nhất
        diem_so.remove(diem_so[0])
        diem_so.remove(diem_so[0])

    return diem_so

# Lập trình xử lý lớn hơn 8
def diem_lon_hon_8(diem_so):
    count = 0
    for diem in diem_so:
        if diem >= 8:
            count += 1
    return count

#  Gọi hàm và xuất ra danh sách sau khi xử lý 1 và 2
sap_xep = sap_xep_va_xoa_diem(diem_so)
print(f"Danh sách sau khi xử lý 1 và 2 là: {sap_xep}")

# Gọi hàm đếm số lượng điểm lớn hơn 8
count = diem_lon_hon_8(diem_so)
print(f"Số lượng điểm hơn hơn và bằng 8 là: {count}")

# Cách 2
# Nhập số lượng bài tập
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập số nguyên dương!")
else:
    diem_bai_tap = []
    for i in range(n):
        diem = float(input(f"Nhập điểm cho bài tập {i+1}: "))
        diem_bai_tap.append(diem)
    print("Danh sách điểm các bài tập:", diem_bai_tap)
#1
diem_bai_tap.sort()
print(f"Điểm bài tập sai khi được sắp xếp là:{diem_bai_tap}")
# 2
diem_be_nhat = diem_bai_tap[0]
so_lan = diem_bai_tap.count(diem_be_nhat)
for i in range(so_lan) :
    diem_bai_tap.remove(diem_be_nhat)
print(f"Điểm bài tập sau khi xóa đi điểm bé nhất là {diem_bai_tap}")
#4
count = 0
for i in range(len(diem_bai_tap)) :
    if diem_bai_tap[i] >= 8 :
        count += 1
    else :
        count += 0
print(f"Số bài tập điểm lớn hơn 8 là: {count}")