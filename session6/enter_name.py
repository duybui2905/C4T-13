while True:
 name = input("please insert your name: ")
 if name.isalpha():
     print("hello", name)
     break
 else:
     print("your name is not allowed to have numbers")
