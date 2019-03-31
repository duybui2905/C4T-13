items = ['com', 'pho', 'bun', 'chao', 'mien']


for i in range (len(item)):
    print(items[i])

for item in items:
    print(item)

for i, item in enumerate(items):
    print(i+1, ".", item)