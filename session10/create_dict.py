person = {
    "name" : "Felix",
    "nickname" : "Pewdiepie", 
    "job" : "youtuber",
}
print(person)
person["age"] = 29
print(person)

new_key = input("enter a new key for Felix: ")
new_value = input("enter new value for that key: ")
person[new_key] = new_value
print("new dictionary:")
print(person)
