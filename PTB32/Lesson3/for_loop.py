'''
    Vòng lặp: Có 2 kiểu vòng lặp 
    1. Vòng lặp for
        Cú pháp:
            for (index: số lần lặp) in "Tập hợp":
                Các cú pháp và câu lệnh

    - Index: Sẽ lấy giá trị và thay đổi qua mỗi vòng lặp 
    - Tập hợp: Là tập hợp các phần tử muốn lặp qua 
'''
# Sử dụng hàm range() để vẽ hình tam giác
n = 10
for index in range(1, n + 1): # range(a, b - 1) 
    print("*" * index)

# Ví dụ vòng lặp qua list 
nums = [1, 2, 3, 4, 5, 6, 7]
# Index: số thứ tự - Bắt đầu từ 0 

for num in nums:
    print(num)

# Đếm số chẵn lẻ trong 1 danh sách 
numbers = [1, 2, 3, 4, 5, 6, 7, 10, 20] 
even_count = 0 # Biến lưu trữ số chẵn
odd_count = 0 # Biến lưu trữ số lẻ

for num in numbers:
    print(num)
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Số chẵn là: " +  str(even_count))
print("Số lẻ là: ", odd_count)