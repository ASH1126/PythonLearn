blog_post = ["", "Judul 1", "Judul 2", "", "Judul 3", "Judul 4"]

for post in blog_post:
    if post == "":
        continue
    else:
        print(post)

print("-------------------------------------")

myString = "ini String"

for char in myString:
    print(char)

print("-------------------------------------")

for x in range(0, 10):
    print(x)

print("-------------------------------------")

person = {
    "first_name": "Hope",
    "last_name": "Marsal",
    "birth_year": "1994",
    "country_of_birth": "USA",
}

for key in person:
    print(key, ":", person[key])

print("-------------------------------------")

blog_post = {
    "python": ["Judul 1", "Judul 2", "Judul 3", "Judul 4"],
    "php": ["PHP 1", "PHP 2", "PHP 3", "PHP 4"],
}

for category in blog_post:
    print("Post :", category)
    for post in blog_post[category]:
        print(post)
