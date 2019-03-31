color = ["red", "green", "blue"]
print("the color list: ")
print(*color, sep = ", ")
new_color = input("enter a new color: ")
color.append(new_color)
print("the new color list: ")
print(*color, sep = ", ")
place = int(input("enter a position: "))
print("color at position:", color[place])
for i, item in enumerate(color):
    print(i+1, ".", item)
color_to_delete = input("enter the color you want to delete (value or position): ")
if color_to_delete.isdigit():
    color.pop(int(color_to_delete))
else:
    color.remove(color_to_delete)
print(color)