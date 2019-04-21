p1 = {
    'name' : 'Huy',
    'job' : 'waiter',
    'hours' : 12,
    'dollars' : 0.8,
}
p2 = {
    'name' : 'Phuc',
    'job' : 'chef',
    'hours' : 13,
    'dollars' : 4,
}
p3 = {
    'name' : 'Tuan',
    'job' : "chef's helper",
    'hours' : 12,
    'dollars' : 2,
}
restaurant = [p1, p2, p3]
# print(restaurant[2])
restaurant[0] = {
    'name' : 'Huyen',
    'job' : 'waitress',
    'hours' : 14,
    'dollars' : 1,
}
# print(restaurant[0])
# # restaurant.pop(2)
# # print(restaurant)

# for i in restaurant:
#     print(i)
sum_money = 0
for j in range (len(restaurant)):
    a = restaurant[j]['hours']
    b = restaurant[j]['dollars']
    c = a*b
    print('money of', restaurant[j]['name'], 'earn per day is', c, 'dollars')
    sum_money = sum_money + c
print('all of the money they have to pay to their employe is',sum_money, 'dollars')