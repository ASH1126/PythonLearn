import math

radius = float(input("Radius Lingkaran: "))
# **2 --> pangkat 2
area = math.pi * (radius**2)
circumference = 2 * math.pi * radius

print("Luas lingkaran: ", round(area, 2))
print("Keliling lingkaran: ", round(circumference, 2))
