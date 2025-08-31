'''
    List (Danh sách)
    - Tạo ra danh sách 
    - Truy cập phần tử trong danh sách 
    - Thêm phần tử vào danh sách
    - Xóa phần tử ra khỏi danh sách
    - Độ dài danh sách
    - Lặp qua danh sách
'''
# 1. Tạo ra danh sách
# Danh sách (list): ký hiệu [] - có thể chữa các kiểu dữ liệu khác nhau
empty_list = [] # Danh sách rỗng
my_list = [1, 2, 3, -1, 1.4, "Hưng Đz", True]
#index     0, 1, 2, 3,  4,    5,        6
''' Index - ký hiệu []: dùng để đánh dấu các phần tử (item) theo số thứ tự bắt đầu 
từ 0
item (Phần tử - giá trị)- ký hiệu () là kiểu dữ liệu tồn tại trong list'''

# Truy cập phần tử trong danh sách 
#  Chú ý: Có thể truy cập các phần tử bằng (index)
num = my_list[2]
print("Giá trị ở vị trí số 2 là:", num)
name = my_list[5]
print("Giá trị ở vị trí số 5 là:", name)

# Thêm phần tử vào danh sách "append()" - "insert()"
print("Danh sách trước khi được thêm: " , my_list)
my_list.append("Nguyên XZ") # Thêm phần tử "Nguyên XZ" vào cuối list
print("Danh sách sau khi được thêm: " , my_list)
my_list.insert(2, "Nguyên") # Thêm phần tử "Nguyên" vào vị trí số 2
print("Danh sách sau khi được thêm bởi insert: " , my_list)

# Xóa phần tử ra khỏi danh sách "remove()"-"del"-"pop()"-"clear()"
my_list.remove("Hưng Đz") # Xóa phần tử -item ("Hưng Đz") ra khỏi list
print("Danh sách sau khi bị xóa khi dùng remove: " , my_list)
del my_list[2] # Xóa phần tử ở vị trí số 2 ra khỏi list
print("Danh sách sau khi bị xóa khi dùng del: " , my_list)
my_list.pop() # Xóa phần tử cuối cùng ra khỏi danh sách
print("Danh sách sau khi bị xóa khi dùng pop: " , my_list)
# my_list.clear() # Xóa toàn bộ danh sách
# print("Danh sách sau khi bị xóa khi dùng clear: " , my_list)

# Độ dài của danh sách - Được tính từ 1
length = len(my_list)
print("Độ dài danh sách: ", length)

# Lặp qua danh sách - for loop
for index in my_list:
    print(index)

# Sắp xếp danh sách theo chiều tăng dần
new_list = [5, 3, 1, 2, 4]
# new_list.sort() # Sắp xếp danh sách theo chiều tăng dần 
for index in new_list:
    for j in range(len(new_list) - 1):
        if new_list[j] > new_list[j + 1]:
            new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]  # Hoán đổi vị trí

print("Sắp xếp danh sách theo chiều tăng dần: ", new_list)

# Sắp xếp danh sách theo chiều giảm dần theo sort
new_list.sort(reverse=True)
print("Sắp xếp danh sách theo chiều giảm dần: ", new_list)

a = 12
b = 4
c = a * b
print("kết quả của 12 x 4 là: ", c)