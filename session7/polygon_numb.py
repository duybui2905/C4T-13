so_canh = int(input("nhap so canh: "))

from turtle import *

speed(-1)

for i in range(so_canh):
    forward(50)
    left(360/so_canh)

shape("turtle")

mainloop()