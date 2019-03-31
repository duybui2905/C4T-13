import random
word = input("enter a word: ")
shuffled = ''.join(random.sample(word,len(word)))
for i in range (len(shuffled)):
    print(shuffled[i].upper())