'''
Xâu chuỗi trong python có thể hiểu là chuỗi kỹ tự strings
 1.Tạo chuỗi
 2.Nối chuỗi
 3.Truy cập vị trí của chuỗi
 4.Cắt chuỗi
 5.Định dạng của chuỗi
 6.Các phương thức của chuỗi
'''
# 1.Tạo chuỗi: Được khai báo trong dấu nháy đơn (' ') hoặc nháy kép (" ")
name = "Hà"
age = "13"
print("Đây là kiểu dữ liệu của age: ", type(age))

# 2.Nối chuỗi: sử dụng toán tử (+) - chỉ được nối chuỗi bởi kiểu dữ liệu strings
address = " Hà Nội"
info = name + " sống ở" + address + " tuổi:" + str(age)
print(info)

# 3.Truy cập vị trí của chuỗi: sử dụng index để truy cập vị trí
# Khoảng trắng cũng được tính là 1 đơn vị
name = "Thu Hà"
index_name = name[4]
print("Vị trí của 4 là: ", index_name)

# 4.Cắt chuỗi: sử dụng index để cắt theo vị trí
strings = "0123456789"
print(strings[: 4]) # Cắt từ 0 -> 4
print(strings[3 : 7]) # Cắt từ vị trí 3 -> 7
print(strings[5 : ]) # Cắt từ 5 -> hết

# 5.Định dạng của chuỗi: gồm 3 định dạng
name = "Thu Hà"
address = "Thanh Hóa"
age = 13
# Định dạng thường
print("Tên tôi là: ", name, "Địa chỉ: ", address, "Tuổi là: ", str(age))
# Định dạng sử dụng "Format()"
print("TÊN TÔI LÀ: {} ĐỊA CHỈ: {} TUỔI LÀ: {}". format(name, address, str(age)))
# Định dạng sử dụng f""
print(f"Tên tôi là {name} Địa chỉ là {address} Tuổi là: {str(age)}")

# 6.Các phương thức của chuỗi
# Phương thức upper(): chuyển đổi chuỗi thành chữ hoa
name = "Hà"
print(f"Sử dụng upper(): {name.upper()}")
# Phương thức lower(): chuyển đổi chuỗi thành chữ thường
name = "Hà"
print(f"Sử dụng lower(): {name.lower()}")

# split(): sử dụng để chuyển đổi chuỗi sang danh sách (list)
strings = "Thu Hà . xinh gái"
strings_list = strings.split(".")
print(f"Strings sau khi tách bởi split(): {strings_list}")

# find(), index(): Tìm vị trí xuất hiện - nếu không tìm thấy kết quả sẽ trả ra -1 nếu dùng find()
new_strings = "Tốt bụng"
print(new_strings.find("bụng"))
print(new_strings.index("Tốt"))

# replace(): thay thế các trường hợp của một chuỗi khác
# Chú ý: bắt buộc giá trị thay đổi phải thuộc strings
string2 = "Hà rất xấu"
new_string2 = string2.replace("xấu", "xinh gái")
print(new_string2)