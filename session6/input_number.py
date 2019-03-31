while True:
 txt = input("enter your yob: ")
 if txt.isdigit():
     break
 else:
     print(txt, "is not a number")

a = 2019 - int(txt)
print("your are", a, "year(s) old")