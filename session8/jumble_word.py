import random
item = ["cat", "dog", "bird", "mice"]
random_choice = (random.choice(item))
shuffled = ''.join(random.sample(random_choice,len(random_choice)))
print(shuffled)
guess = input("enter your guess: ")
if guess == random_choice:
    print("you're correct!")
else:
    print("you're wrong!!!")