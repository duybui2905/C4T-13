items = [1, 5, 3, 2, 4, 82, 64, 81]
evens = []
for i in items:
        if i % 2 == 0:
                evens.append(i)
print(*evens, sep = ", ")