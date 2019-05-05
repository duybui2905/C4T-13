my_mov = {
    'name' : 'Interstella',
    'actors' : ['Matthew McConaughey', 'Anne Hathaway', 'Jessica Chastain', 'Bill Irwin'],
    'director' : 'Christopher Nolan',
    'year' : 2014,
}
# print(my_mov)
my_mov['country'] = 'USA'
# print(my_mov)
for k,v in my_mov.items():
    print(k, '-', v)

# my_mov['actors'] = [1, 2, 3, 4]
# print(my_mov['actors'])

actors = my_mov['actors']
# actors.append('dfedfrd')
# print(my_mov['actors'])

# actors.pop(0)
# print(my_mov['actors'])

# print(actors[1])

# for i in actors:
#     print(i)
