map = {
    "x":4,
    "y":4
}
P = {
    "x":1,
    "y":2
}
E = {
    "x":2,
    "y":1
}
K = {
    "x":1,
    "y":3
}
W = {
    "x":1,
    "y":1
}
key_storage=0
while True:
    for y in range(map["y"]):
        for x in range(map["x"]):
            # P_is_here = False
            if x==P["x"]and y==P["y"]:
                print("P",end=" ")
                # P_is_here = True
            elif E["x"]==x and E["y"]==y:
                print("E", end=" ")
            elif K["x"]==x and K["y"]==y:
                if key_storage ==0:
                    print('K', end=' ')
                else:
                    print('-',end=' ')
            elif W['x']==x and W['y']==y:
                print('W', end=' ')
            else:
                print('-', end = ' ')
            # ------------------------
            # if P_is_here:
            #     print("P ",end="")
            # else:
            #     print("- ",end="")
        print()
    if P["x"] == E["x"] and P["y"] == E["y"] and key_storage == 1:
        print('Congrats, you’ve just escaped the dungeon')
        break
    

    a = input("Your move(s/w/a/d): ").upper()
    dx = 0
    dy = 0 
    if a == "A":
        dx = -1
    elif a == "D":
        dx = 1
    elif a == "W":
        dy = -1
    elif a == "S":
        dy = 1
    else:
        print("Wrong move")
    if P["x"]+dx in range(map["x"]) and P["y"]+dy in range(map["y"]):
        P["x"]+=dx
        P["y"]+=dy
    if P["x"] == K["x"] and P["y"] == K["y"]:
        key_storage+=1
        print("You’ve just picked up a key!!!")