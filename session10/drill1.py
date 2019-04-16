person = {
    "name" : "Felix",
    "nickname" : "Pewdiepie", 
    "job" : "youtuber",
}
print(person)

find_key = input("enter a string to find if it's in the dictionary: ")
if find_key in person:
    print("key", find_key, "do exists in this dictionary")
else:
    print("key", find_key, "doesn't exists in this dictionary")