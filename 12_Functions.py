def say_hello(person1, person2="Max"):
    print("Hai ! " + person1 + " and " + person2)


def fahr2celsius(fahr):
    celsius = (5 * (fahr - 32)) / 9
    return celsius


say_hello("Anita", "hope")
say_hello("Anita")
print("Celsius: ", round(fahr2celsius(100), 2))
print("Kelvin: ", round(fahr2celsius(100) + 273.5, 2))
