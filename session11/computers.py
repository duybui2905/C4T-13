computers = {
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30,
}

# print('the number of MACBOOK computer is:', computers['MACBOOK'])

# computer_type = input('enter type of computer: ').upper()
# print('the number of', computer_type, 'computer is: ', computers[computer_type])

# new_computer = input("enter new type of computer: ").upper()
# number = input('enter the number of it: ')
# computers[new_computer] = number
# print(computers)
computers['TOSHIBA'] = 50
computers['DELL'] = 10
computers['MACBOOK'] = 2
computers['FUJITSU'] = 15
computers['ALIENWARE'] = 5
print(computers)
sum = 0
for k, v in computers.items():
    sum = sum + v
print('the total number of computers is', sum, 'computers')

price = {
    'HP' : 600,
    'DELL' : 650,
    'MACBOOK' : 12000,
    'ASUS' : 400,
    'ACER' : 350,
    'TOSHIBA' : 600,
    'FUJITSU' : 900,
    'ALIENWARE' : 1000,
}
print(price)
# # print(price['ASUS'])
# comp_price = input('enter a type of computer: ').upper()
# print('the price of that computer is:', price[comp_price])

# comp = input('enter a type of computer: ').upper()
# number = int(input('enter the number of computers you wanna buy: '))
# price_comp = price[comp]*number
# print('the total price is', price_comp)

# comp = input('eneter a computer type: ').upper()
# number = int(input('enter the number of computers you wanna buy: '))

#Sep
# comp_number = input('enter a computer type and the number: ').upper()
# a = comp_number.split(':')
# comp = a[0]
# number = int(a[1])
# computers[comp] = computers[comp] - number
# print('the maintain', comp, 'computer is', computers[comp])
# print(computers)

total_price = 0
for a,b in zip(computers.values(), price.values()):
    c = a * b
    print(c)
    total_price += c
print('the total price is', total_price)