import random 

character = {
    'Name' : 'Light',
    'Age' : 17,
    'Strength' : 8,
    'Defense' : 10,
    'HP' : 100,
    'Backpack' : ['Shield', 'Bread Loaf'],
    'Gold' : 100,
    'Level' : 2,
}
# print(character)

character['Gold'] += 50
# print(character)

character['Backpack'].append('FlintStone')
# print(character)

character['Pocket'] = ['MonsterDex', 'Flashlight']
# print(character)
character_skill = [
    {
    'Name' : 'Tackle',
    'Minimum level': 1,
    'Damage' : 5,
    'Hit rate' : 0.3,
    },
    {
    'Name' : 'Quick attack',
    'Minimum level': 2,
    'Damage': 3,
    'Hit rate': 0.5,
    },
    {
    'Name': 'Strong Kick',
    'Minimum level': 4,
    'Damage': 9,
    'Hit rate': 0.2,    
    }
]
# print(character_skill)
length = len(character_skill)
# skill = int(input('enter a skill number: '))

# for i in range (length):
#     print('the level of the skill is:', character_skill[i]['Minimum level'])
#     if character['Level'] < character_skill[i]['Minimum level']:
#         print('the damage is:', character_skill[i]['Damage'])
#     else:
#         print('level to large')
r1 = random.randint(0, 1)
print(r1)
for i in range (length):
    print('the hit rate of the skill is:', character_skill[i]['Hit rate'])
    if r1 < character_skill[i]['Hit rate']:
        print('the damage is:', character_skill[i]['Damage'])
    elif r1 > character_skill[i]['Hit rate']:
        print('hit failed')
