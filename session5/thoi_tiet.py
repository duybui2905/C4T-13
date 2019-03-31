from random import randint

a = randint(0, 100)

if a < 30:
    print("rainly")
elif a >= 30 and a < 60:
    print("cloudy")
elif a > 60:
    print("sunny")