from turtle import *
mau = ["blue", "green", "red", "orange"]
speed(-1)
shape("turtle")
for i in range (len(mau)):
    color(mau[i])
    forward(50)
mainloop()