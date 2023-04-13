students = ["Hope", "Lizze", "Joe"]
print(students, type(students), len(students))
print(students[0], students[-1], students[:2])

month = ("Januari", "Februari", "Maret")
print(month, type(month), len(month))
print(month[0], month[-1], month[:2])

print(students)
students[0] = "Anita"
print(students)

# print(month)
# month[0] = "November"
print(month)

students.append("Cath")
print(students)

students.insert(0, "Sam")
print(students)

students.pop()
print(students)

students.pop(1)
print(students)

students.remove("Sam")
print(students)

students2 = ["Perce", "Luke"]
print(students2)

print(students + students2)
