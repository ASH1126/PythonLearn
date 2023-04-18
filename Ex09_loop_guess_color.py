import random

color = ["red", "blue", "white", "green"]

print(color)

while True:
    color = color[random.randint(0, len(color) - 1)]
    guess = input("Tebak warna: ")

    while True:
        if color == guess:
            break
        else:
            guess = input("Nope. Again: ")

    print("Benar !", color)

    play_again = input("Play Again? Type 'no' to quit. ")

    if play_again.lower() == "no":
        break

print("Thank for playing")
