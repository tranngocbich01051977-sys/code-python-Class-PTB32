class hocsinh:
    def __init__(self, name, address, high, weight, learn):
        self.name = name
        self.address = address
        self.high = high
        self.weight = weight
        self.learn = learn
    def show(self):
        print("Thông tin học sinh:")
        print(f"Tên học sinh: {self.name}")
        print(f"Địa chỉ: {self.address}")
        print(f"Chiều cao: {self.high}")
        print(f"Cân nặng: {self.weight}")
        print(f"Học lực: {self.learn}")
    def update_address(self):
        self.address = input("Nhập địa chỉ mới: ")
    def update_health(self):
        self.high = float(input("Nhập chiều cao mới:"))
        self.weight = float(input("Nhập cân nặng mới:"))
Hoc_sinh = hocsinh("Đào Thị Hạnh Nhân", "Yên Mỹ", "1.62", "49", "Giỏi")
Hoc_sinh.show()
Hoc_sinh.update_address()
Hoc_sinh.update_health()
