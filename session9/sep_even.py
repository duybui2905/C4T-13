items = (input("Enter a list of number: ").split(" "))
evens = []
for i in items:
    if int(i) % 2 == 0:
        evens.append(i)
print(*evens, sep = ", ")