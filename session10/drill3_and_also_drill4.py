while True:
    youtuber = {
        "pewdiepie" : "Swedish",
        "mr.beast" : "American",
        "idubbbz" : "American",
        "jacksfilms" : "American",
        "jacksepticeye" : "Irish",
        "joji" : "Japanese",
}
    youtuber_name = input("Enter a youtuber's name: ")
    lower_youtuber_name = youtuber_name.lower()
    print(youtuber.get(lower_youtuber_name))