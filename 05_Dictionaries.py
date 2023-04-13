person = {
    "first_name": "Hope",
    "last_name": "Marsal",
    "birth_year": "1994",
    "country_of_birth": "USA",
}

print(person, type(person))
print(person["first_name"])

person["birth_year"] = 1993
print(person)

person["status"] = "Single"
print(person)

person["brother"] = ["Sam", "Luke"]
print(person)

person["brother"].append("Lina")
print(person)

print(person.get("age", "Not found"))

print(person.get("brother", "Not found"))

Key = "first_name"
print(Key, person[Key])
