character = {
    'name' : 'Light',
    'age' : 17,
    'strength' : 8,
    'defense' : 10,
    'HP' : 100,
    'backpack' : ['Shield', 'Bread Loaf'],
    'gold' : 100,
    'level' : 2,
}
print(character)

character['gold'] += 50
print(character)

character['backpack'].append('FlintStone')
print(character)

character['pocket'] = ['MonsterDex', 'Flashlight']
print(character)~