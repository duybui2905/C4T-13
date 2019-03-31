month = int(input("enter a month: "))

if month == 2:
    print("28 days in normal year, 29 days in leap year")
elif month in (1,3,5,7,8,10,12):
    print("this month have 31 days")
elif month in (4,6,9,11):
    print("this month have 30 days")
else:
    print("this is not a month")