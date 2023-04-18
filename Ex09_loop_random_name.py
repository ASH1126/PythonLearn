import random

people = []

for x in range(0, 8):
    person = input("Nama: ")
    people.append(person)

index = random.randint(0, 7)
random_person = people[index]

print("Pilih nama: ", random_person)
