items = [2, 5, 9, 10, 21, 32]
a = int(input("Enter a number you wanna search: "))
if a in items:
    print("Found this item. Postion:", items.index(a))
else:
    print("This number isn't conntain in this list, please try again.")