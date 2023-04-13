person = {
    "name": "Hope",
    "last_name": "Marsal",
    "birth_year": "1994",
    "country_of_birth": "USA",
}

key = input("Informasi ? ").lower()

result = person.get(key, "Not Found")

print(result)
