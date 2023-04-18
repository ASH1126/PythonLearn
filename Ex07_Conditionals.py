print("Kalkulasi body mass index.")

weight = float(input("Wight in Kg (ex. 70.5): "))
height = float(input("Hight in Meters (ex. 1.50): "))

bmi = weight / (height**2)

print("BMI: ", round(bmi, 2))

if bmi <= 18.5:
    clasifikasi = "Underweight"
elif bmi > 18.5 and bmi <= 24.9:
    clasifikasi = "Normal weight"
elif bmi > 24.9 and bmi <= 29.9:
    clasifikasi = "Overwight"
else:
    clasifikasi = "Obesity"

print("Klisifikasi: ", clasifikasi)
