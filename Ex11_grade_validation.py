data_valid = False
while data_valid == False:
    grade1 = input("Grade 1: ")
    try:
        grade1 = float(grade1)
    except:
        print("Invalid Type")
        continue

    if grade1 < 0 or grade1 > 10:
        print("Grade in 0 to 10")
        continue
    else:
        data_valid = True

data_valid = False
while data_valid == False:
    grade2 = input("Grade 2: ")
    try:
        grade2 = float(grade2)
    except:
        print("Invalid Type")
        continue

    if grade2 < 0 or grade2 > 10:
        print("Grade in 0 to 10")
        continue
    else:
        data_valid = True

data_valid = False
while data_valid == False:
    total_class = input("Jumlah kelas: ")
    try:
        total_class = int(total_class)
    except:
        print("Invalid Type")
        continue

    if total_class <= 0:
        print("Number >= 0")
        continue
    else:
        data_valid = True

data_valid = False
while data_valid == False:
    absensi = input("Absen: ")
    try:
        absensi = int(absensi)
    except:
        print("Invalid Type")
        continue

    if absensi < 0 or absensi > total_class:
        print("Number > 0 dan > class")
        continue
    else:
        data_valid = True

avg_grade = (grade1 + grade2) / 2
attendance = (total_class - absensi) / total_class

print("rata2 grade: ", round(avg_grade, 2))
print("rate kehadiran: ", str(round((attendance * 100), 2)) + "%")

if avg_grade >= 6 and attendance >= 0.8:
    print("Siswa Approved.")
elif avg_grade < 6 and attendance < 0.8:
    print("Siswa failed, rata2 grade lower 6.0 and rate kehadiran lower 80%")
elif attendance >= 0.8:
    print("Siswa failed, rata2 grade lower 6.0")
else:
    print("Siswa failed, rate kehadiran lower 80%")
