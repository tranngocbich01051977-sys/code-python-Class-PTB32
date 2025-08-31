# Bài 1: Tính tổng của 1 danh sách
# Cơ bản: có danh sách sẵn
# Nâng cao Nhập bàn phím, có độ dài danh sách ít nhất là 5

# Cơ bản:
def tinh_tong(danh_sach):
    tong = 0
    for so in danh_sach:
        tong += so
    return tong    

danh_sach_new = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

tong_danh_sach = tinh_tong(danh_sach_new)
print(f"Tổng danh sách là: {tong_danh_sach}")


# Nâng cao
def nhap_danh_sach():
    while True:
        input_str = input("Nhập ít nhất 5 số, cách nhau bởi dấu cách: ")
        items = input_str.strip().split()

        if len(items) >= 5:
            try:
                numbers = [float(item) for item in items]
                return numbers
            except ValueError:
                print(f"Vui lòng chỉ nhập số vì có lỗi {ValueError}")
        else:
            print("Bạn phải nhập ít nhất 5 số")

# Hàm tính tổng
def tinh_tong_danh_sach(danh_sach):
    tong = 0
    for so in danh_sach:
        tong += so
    return tong

# Gọi hàm
tong_danh_sach_so = nhap_danh_sach()
tong = tinh_tong(tong_danh_sach_so)
print(f"Tổng danh sách là: {tong}")



# Bài tập 2: Tạo 1 chương trình tính lương cho nhân viên

def tinhluong(giolam, luonggio):
    tongluong = giolam * luonggio
    return tongluong

def inthongtin(ten, giolam, luonggio, tongluong):
    print("Thông tin nhân viên: ")
    print(f"Tên: {ten}")
    print(f"Số giờ làm: {giolam}")
    print(f"Mức lương theo giờ: {luonggio}")
    print(f"Tổng tiền lương: {tongluong}")

# Nhập thông tin người dùng:
ten = input("Nhập tên nhân viên: ")
giolam = float(input("Nhập số giờ làm: "))
luonggio = float(input("Nhập mức lương theo giờ: "))

# Tính tổng tiền lương:
def tongluong(giolam, luonggio):
    tong = 0
    for so in tongluong:
        tong += so
        return tong