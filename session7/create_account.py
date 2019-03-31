username = input("enter your username: ")


while True:
    password = input("enter your password: ")
    if len(password) < 8:
        print("your password need more than 8 characters")
    elif password.isdigit() == True:
        print("your password need to contain letters")
    elif password.isalpha() == True: 
        print("your password need to contain numbers")
    else:
        print("valid password")
        break
    

while True:
    password2 = input("enter the password again: ")
    if password == password2:
        print("the password is matched")
        break
    else:
        print("the password isn't matched")

while True:
    email = input("enter your email: ")
    if ("@") in email and (".") in email:
        print("valid")
        break
    else:
        print("unvalid")

