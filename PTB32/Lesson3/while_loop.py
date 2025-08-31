'''
    - Vòng lặp while: Là một cấu trúc các ngôn ngữ lập trình, cho 
phép lặp lại một khối mã lệnh cho đến khi điều kiện trở thành False
    - Vòng lặp vô hạn: Là vong lặp không bao giờ kết thúc, gây ra hiện 
tượng treo ứng dụng. Thường sảy ra trong vòng lặp while
    -  break: Giúp thoát khỏi vong lặp, tránh lặp vô hạn, dừng lại khi
điều kiện break bằng True
'''
# Vòng lặp thường
count = 0
while count < 1001:
    print("Giá trị của count là: ", count)
    count += 1 # count = count + 1

# Vòng lặp vô hạn 
# count = 0
# while True:
#     print("Giá trị của count là: ", count)
#     count += 1 # count = count + 1

# Vòng lặp khi sử dụng break
count = 0
while True:
    print("Giá trị của count là: ", count)
    count += 1 # count = count + 1

    if count == 100:
        print("Giới hạn")
        break

# Yêu cầu chương trình in ra 1000 từ "Làm bài tập về nhà đầu đủ - không ở lại" 
count = 0 
while count < 1001:
    print("Làm bài tập về nhà đầy đủ lần: ", count)
    count += 1

count = 0
while True:
    print("Làm bài tập về nhà đầy đủ lần: ", count)
    count += 1 # count = count + 1

    if count == 1001:
        print("Giới hạn")
        break