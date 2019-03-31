item = ["1", "2", "3", "4"]
while True:
    print(item)
    choose = input("Nhập 1 trong 4 thao tác CRUD: ")
    if choose == "C":
        new_item = input("Thêm một thứ gì đó cho danh sách: ")
        item.append(new_item)
    elif choose == "R":
        print("Đọc danh sách:")
        if len(item) == 0:
            print("Danh sách này rỗng")
        for i in  range (len(item)):
            print(item[i])
    elif choose == "U":
        while True:
            a = int(input("Nhập vị trí mà bạn muốn cập nhật (số): "))
            if a >= len(item):
                print("Số này lớn quá!")
            else:
                break
        b = input("Nhập một thứ gì đó để thay thế cho vị trí vừa rồi: ")
        item[a] = b
    elif choose == "D":
        while True:
            item_to_delete = int(input("Nhập vị trí mà bạn muốn xóa: "))
            if item_to_delete >= len(item):
                print("Số này lớn quá!")
            else:
                break
        item.pop(item_to_delete)
    else:
        print("Xin hãy nhập C,R,U,D hoặc c,r,u,d")