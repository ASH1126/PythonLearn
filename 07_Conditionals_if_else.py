grade1 = float(input("Grade 1: "))
grade2 = float(input("Grade 2: "))
absensi = int(input("Absen: "))
total_class = int(input("Jumlah kelas: "))

avg_grade = (grade1 + grade2) / 2
attendance = (total_class - absensi) / total_class

print("rata2 grade: ", round(avg_grade, 2))
print("rate kehadiran: ", str(round((attendance * 100), 2)) + "%")

if avg_grade >= 6:
    if attendance >= 0.8:
        print("Siswa Approved.")
    else:
        print("Siswa failed, rate kehadiran lower 80%")
elif attendance >= 0.8:
    print("Siswa failed, rata2 grade lower 6.0")
else:
    print("Siswa failed, rata2 grade lower 6.0 and rate kehadiran lower 80%")
