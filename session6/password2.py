while True:
    password = input("enter a password: ")
    if password.isalpha() == False and len(password) >= 8:
        print("valid password")
        break
    elif password.isalpha() or len(password) < 8:
        print("make sure that your password have equal or over 8 characters and contain numbers")