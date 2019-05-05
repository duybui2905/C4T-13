import time
p = 0
question1 = {
    'Question' : '1 + 1 = ?',
    'a' : 'one',
    'b' : 'two',
    'c' : 'three',
    'd' : 'four',
    'e' : '2',
    "correct_answer" : ['b','e']
}
for k, v in question1.items():
    if k != "correct_answer":
        print(k+':',v)

answer1 = input('enter your first answer: ')
answer2 = input('enter your second answer: ')

if answer1 == 'b' and answer2 == 'e' or answer1 == 'e' and answer2 == 'b':
    print("you're right")
    p += 1
    print('your points is:', p)
elif answer1 == '2' and answer2 == 'two' or answer1 == 'two' and answer2 == '2': 
    print("you're right")
    p += 1
    print('your points is:', p)
else:
    print("you're wrong")
    print('the correct answer is:', question1['correct_answer'])
    print('your points is:', p)

time.sleep(2)

question1 = {
    'Question' : '3 + 5 = ?',
    'a' : 'seven',
    'b' : 'nine',
    'c' : 'eight',
    'd' : '9',
    'e' : '8',
    'correct_answer' : ['c','e']
}
for k, v in question1.items():
    if k != "correct_answer":
        print(k+':',v)

answer1 = input('enter your first answer: ')
answer2 = input('enter your second answer: ')

if answer1 == 'c' and answer2 == 'e' or answer1 == 'e' and answer2 == 'c':
    print("you're right")
    p += 1
    print('your points is:', p)
elif answer1 == '8' and answer2 == 'eight' or answer1 == 'eight' and answer2 == '8': 
    print("you're right")
    p += 1
    print('your points is:', p)
else:
    print("you're wrong")
    print('the correct answer is:', question1['correct_answer'])
    print('your points is:', p)

time.sleep(2)

question1 = {
    'Question' : '9 + 10 = ?',
    'a' : '12',
    'b' : 'seventeen',
    'c' : 'nineteen',
    'd' : '19',
    'e' : '6',
    'correct_answer' : ['c','d']
}
for k, v in question1.items():
    if k != "correct_answer":
        print(k+':',v)

answer1 = input('enter your first answer: ')
answer2 = input('enter your second answer: ')

if answer1 == 'c' and answer2 == 'd' or answer1 == 'd' and answer2 == 'c':
    print("you're right")
    p += 1
    print('your points is:', p)
elif answer1 == '9' and answer2 == 'nineteen' or answer1 == 'nineteen' and answer2 == '9': 
    print("you're right")
    p += 1
    print('your points is:', p)
else:
    print("you're wrong")
    print('the correct answer is:', question1['correct_answer'])
    print('your points is:', p)

per = p / 3 * 100
print('your points percentage is:', per,'%')