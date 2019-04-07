scores = [9, 5, 2, 10, 21, 1, 31, 99]
scores.sort (reverse = True)
for i in range (5):
    print(str(i+1)+".", scores[i])
new_score = int(input("enter a new score: "))
scores.append(new_score)
scores.sort (reverse = True)
for i in range (5):
    print(str(i+1)+".", scores[i])