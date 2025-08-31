'''
    - Câu lệnh điều kiện rẽ nhánh (if - else)
    Gồm 3 trường hợp 
        1. Xảy ra 1 điều kiện 
        2. Xảy ra 1 điều kiện và phần còn lại 
        3. Nhiều điều kiện khác nhau và phần còn lại
'''
# 1. Xảy ra 1 điều kiện/ Nêu không đúng sẽ không trả ra kết quả
a = 10
b = 20
if a < b:
    print(True)

# 2. Xảy ra 1 điều kiêmk và các phần còn lại 
if a == b: 
    print("a sẽ bằng b") # Nếu đúng thì chạy logic ở đây
else:
    print("a không bằng b") # Nếu sai thì chạy logic ở đây 

# 3. Nhiều điều kiện và phần còn lại 
x = 20
z = 30
if x == z:
    print("x bằng z")
elif x < z:
    print("x bé hơn z")  
elif x > z:
    print("x lớn hơn z")
else:
    print("Kệ")