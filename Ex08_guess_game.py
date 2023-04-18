import random

number = random.randint(0, 10)

guess = int(input("saya memikirkan sebuah angka 1 - 10. tebaklah ? "))

while True:
    if guess == number:
        break
    else:
        guess = int(input("Tidak. Cobalagi: "))

print("Benar, kau berhasil", number)
