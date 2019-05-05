question1 = {
    'Question' : 'How many legs does an octopus have?',
    'a' : '1 legs',
    'b' : '2 legs',
    'c' : '8 legs',
    'd' : '5 legs',
    'e' : '7+1 legs',
}
for k, v in question1.items():
    print(k+':',v)

answer1 = input('enter your first answer: ').lower()
answer2 = input('enter your second answer: ').lower()

if answer1 == 'c' and answer2 == 'e' or answer1 == 'e' or answer2 == 'c':
    print("you're right")
elif answer1 == '8 legs' and answer2 == '7+1 legs' or answer1 == '7+1 legs' or answer2 == '8 legs': 
    print("you're right")
else:
    print("you're wrong")