while True:
    password = input("enter a password: ")
    if password.isalpha() == False:
        print("valid password")
        break
    elif password.isalpha():
        print("invalid password")

    