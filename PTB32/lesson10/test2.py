# Bài 2:
while True:
    n = int(input("Nhập số nguyên dương n: "))
    if n < 0:
        print("Nhập lại số nguyên dương: ")
    elif n == 0:
        print("Dừng chương trình!")
        break
    else:
        tong = 0
        for index in range(1, n + 1):
            tong += index
            print(f"Tổng các số {n} là: {tong}")
