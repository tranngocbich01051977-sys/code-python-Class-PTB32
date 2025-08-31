'''
    Các loại toán tử trong python 
    1. Toán tử số học (+, -, *, /)
        3 toán tử đặc biệt 
        - Chia lấy dư: %
        - Lũy thừa: **
        - Chia lấy phần nguyên: //
'''
# Ví dụ về toán tử số học 
a = 10
b = 3
c = a * b
print("Sau khi a * b là: ", c)
#  Chia lấy dư
d = a % b # 10 % 3 => (9 + 1)/3  
print("Sau khi chia lấy dư: ", d)
# Phép toán lũy thừa
e = a**b # 10**3 => 10 * 10 * 10
print("Sau khi lũy thừa", e)
# Phép chia lấy phần nguyên, Bỏ đi phần thập phân, phân số
r = a // b # 10 // 3 = 3
print("Sau khi chia lấy nguyên: ", r)

'''
    2.  Toán tử gán 
    - Giá trị gán: =
    - Cộng và gán: +=
    - Trừ và gán: -=
    - Nhân và gán: *=
    - Chia và gán: /=
    - Chia lấy dư và gán: %=
    - Chia lấy phần nguyên và gán: //=
'''
# Ví dụ về toán tử gán 
gan = 10
gan += 10 # gan = gan + 10
print("Sau khi gán: ", gan)
gan %= 3
print("Sau khi chia lấy phần dư và gán: ", gan)

'''
    3. Toán tử so sánh
    - Toán tử so sánh cơ bản: >, <, >=, <=
    - Toán tử bằng: ==
    - Toán tử khác: !=
'''
# Ví dụ về toán tử so sánh
num1 = 10
num2 = 30
if num1 != num2:
    print("Đúng")
else:
    print("Sai")

'''
    4. Toán tử Logic
    and: Và Logic/ Tất cả các điều kiện đều phải đúng mới thỏa mãn
    or: Hoặc Logic/ Chỉ cần 1 điều kiện đúng sẽ thỏa mãn
    not: Phủ định/ Đảo ngược Logic
'''
t = 20
f = 30
if not(t == f) and t <= f:
    print(True)
else:
    print(False)