person = {
    "name" : "Felix",
    "nickname" : "Pewdiepie", 
    "job" : "youtuber",
}
print(person)

key_to_delete = input("enter a key to delete: ")
del person[key_to_delete]
print(person)