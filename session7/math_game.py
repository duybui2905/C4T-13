from random import randint
p = 0
while True:
 if p == 0:
     a = randint(-10, 10)
     b = randint(-10, 10)
 elif p >= 5:
     a = randint(-15,15)
     b = randint(-15,15)
 elif p >= 10:
     a = randint(-20,20)
     b = randint(-20,20)
 elif p >= 15:
     a = randint(-25,25)
     b = randint(-25,25)
 elif p >= 20:
     a = randint(-30,30)
     b = randint(-30,30)
 x = randint(-1,1)
 
 s = randint(0,1)
 if s == 0:
     c = a + b + x
     print( a, " + " , b , "=" , c)
 elif s == 1:
     c = a - b + x
     print( a, " - " , b , "=" , c)

 d = str(input("right or wrong: "))
 
 if d == "right" and x == 0:
     print("correct")
     p += 1
     print("your points is:", p)
 elif d == "wrong" and x != 0:
     print("correct")
     p += 1
     print("your points is:", p)
 else:
     print("incorrect, game over")
     print("your points is:", p)
     break
 

 

 