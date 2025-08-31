'''
    1. Ghi chú trong python 
      - Ghi chú 1 dòng: ký hiệu #
      - Ghi chú nhiều dòng: ''' '''
    2. Biến số trong python
    Biến (Variable): Dùng để lưu trữ các dữ liệu
        - Tên biến: Bắt đầu bằng chữ cái hoặc dấu gạch dưới, 
    theo sau là chữ cái, số hoặc dấu gạch dưới. Không bắt đầu bằng số 
    và ký hiệu đặc biệt.
    3. Kiểu dữ liệu trong python
      - Kiểu chuỗi (string-str): Dùng để lưu trữ ký tự vd: "Hello World"
      - Kiểu số nguyên (integer-int): Dùng để lưu trữ số nguyên vd: 10, -10,..
      - Kiểu số thực (float): Dùng để lưu trữ số thực vd: 10.5, -10.5,..
      - Kiểu boolean (bool): Dùng để lưu trữ giá trị đúng hoặc sai vd: True, False
    4. Đầu ra và đầu vào trong python
     - Đầu ra: print() - Dùng để in ra kết quả 
     - Input: input() - Dùng để nhận dữ liệu từ người dùng 
'''
# Ví dụ về biến số 
a = 10
print(a)
# Ví dụ về kiểu dữ liệu 
name = "Hà xinh goái" # Kiểu chuỗi
print("Tên của tôi là: " + name)
age = 13 #Kiểu số nguyên
print("Tuổi của tôi là: " + str(age))
height = 1.63 # Kiểu số thực
print("Chiều cao của tôi là: " + str(height) + "m")
isStudent = True # Kiểu boolean
print("Tôi có phải là sinh viên không? " + str(isStudent))

# Ví dụ về đầu vào và đầu ra
# input() - là kiểu dữ liệu string 
name = input("Tên của tôi là: ") # Nhận dữ liệu từ người dùng
# In ra kết quả
print("Là một người xinh gái, tên của tôi là: " + name)