month = int(input("Insert month: "))
if month <= 3 and month > 0:
    print("this is winter")
elif month <= 6:
    print("this is spring")
elif month <= 9:
    print("this is summer")
elif month <= 12:
    print("this is fall")
else:
    print("THIS IS NOT A MONTH !!!!!!!")
    