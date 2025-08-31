from random import randint

# Tạo ra cơ chế chọn ngẫu nhiên cho máy tính
computer = randint(0, 2)
# Gán giá trị ngẫu nhiên cho máy tính
if computer == 0:
    computer = "Keo"
elif computer == 1:
    computer = "Bua"
elif computer == 2:
    computer = "Bao" 
# Tạo người chơi
player = input("Nhập sự lựa chọn của bạn: ") 
# So sánh các kết quả của 2 người chơi
if computer == player:
    print("Hòa")
if player == "Keo":
    if computer == "Bua":
       print("THUA")
    if computer == "Bao":
       print("THẮNG")

if player == "Bao":
    if computer == "Keo":
       print("THUA")
    if computer == "Bua":
        print("THẮNG")

if player == "Bua":
    if computer == "Bao":
        print("THUA")
    if computer == "Keo":
        print("THẮNG")               
print(computer)