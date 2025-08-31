'''
   Tạo 1 chương trình "Shopping Phone"
      1. Tạo ra danh sách sản phẩm
      2. Xem giỏ hàng
      3. Thêm sản phẩm vào giỏ hàng
      4. Xoá sản phẩm ra khỏi giỏ hàng 
      5. Thoát chương trình 

    Có yêu cầu chọn tính năng
    Chú ý: Phải sử dụng hàm để xử lý 
'''
product = ["apple", "Samsung", "lenovo"]
Shopping_list = []

# 1. Hiển thị sản phẩm
def product_list(product):
    # Hiển thị sản phẩm
    for index in range(len(product)):
        print(f"{index + 1}: {product[index]}")
        


# 2. Xem giỏ hàng
def shopping(Shopping_list):
    # Khi giỏ hàng rỗng
    if not Shopping_list: # Nếu giỏ hàng rỗng
        print("Chưa có sản phẩm trong giỏ hàng !!")
    else:
        print("Mặt hàng của bạn bao gồm là: ")
        for index in range(len(Shopping_list)):
            print(f"{index + 1}: {Shopping_list[index]}")


# 3. Thêm sản phẩm vào giỏ hàng
def add_shopping_list(product, Shopping_list):
    print("Danh sách sản phẩm là: ")
    product_list(product) # Goi lại hàm product_list(product) để hiển thị sản phẩm
    # Tạo biến số lưu trữ vị trí sản phẩm
    item_index = int(input("Nhập sản phẩm bạn muốn thêm vào: ")) - 1
    if item_index >= 0 and item_index < len(product):
        selected_item = product[item_index] # Tạo biến số lưu trữ sản phẩm đã chọn
        Shopping_list.append(selected_item)
        print(f"{selected_item} đã được thêm vào giỏ hàng của bạn")
    else:
        print("Sản phẩm không hợp lệ") 



# 4. Xóa sản phẩm ra khỏi giỏ hàng
def remove_item(Shopping_list):
    if not Shopping_list:
        print("Giỏ hàng của bạn đang trống")
    else:
        print("Các sản phẩm có trong giỏ hàng là: ") 
        shopping(Shopping_list)   
        item_index = int(input("Nhập vị trí sản phẩm bạn muốn xóa: ")) - 1
        if item_index >= 0 and item_index < len(Shopping_list):
            delete_item = Shopping_list.pop(item_index)
            print(f"{delete_item} đã được xóa ra khỏi giỏ hàng")
        else: 
            print("Không hợp lệ !")

# Gọi hàm remove_item(Shopping_list)
remove_item(Shopping_list) 

# Hàm quản lý chương trình
def main():
    product = ["apple", "Samsung", "lenovo"]
    Shopping_list = []

    while True:
        print("1. Xem danh sách sản phẩm")
        print("2. Xem giỏ hàng")
        print("3. Thêm sản phẩm vào giỏ hàng")
        print("4. Xóa sản phẩm ra khỏi giỏ hàng")
        print("5. Thoát")
        choice = int(input("Nhập tính năng bạn muốn lựa chọn (1-5): "))

        if choice == 1:
            # Gọi hàm product_list để hiển thị sản phẩm
            product_list(product)
        elif choice == 2:
            # Gọi hàm shopping để xem giỏ hàng
            shopping(Shopping_list)
        elif choice == 3:
            # Gọi hàm add_shopping_list(product, Shopping_list)
            add_shopping_list(product, Shopping_list)
        elif  choice == 4:
            # Gọi hàm remove_item(Shopping_list)
            remove_item(Shopping_list)
        elif choice == 5:
             break 
# Gọi hàm quản lý chương trình
main()           