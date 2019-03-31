color = ["red", "green", "blue"]
print("the color list: ")
print(*color, sep = ", ")
new_color = input("enter a new color: ")
color.append(new_color)
print("the new color list: ")
print(*color, sep = ", ")
place = int(input("enter a position: "))
print("color at position:", )