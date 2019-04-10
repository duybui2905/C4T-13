person = {
    "name" : "Felix",
    "nickname" : "Pewdiepie", 
    "job" : "youtuber",
}
print(person)
update_key = input("enter a key to update: ")
update_value = input("enter the new value of that key: ")

person[update_key] = update_value
print(person)