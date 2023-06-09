import matplotlib.pyplot as plt
import time as t

times = []
mistakes = 0

print("Program help faster typing word 'programming' ")
input("Press enter...")

while len(times) < 5:
    start = t.time()
    word = input("Type the word: ")
    end = t.time()
    time_elapsed = end - start

    times.append(time_elapsed)

    if word.lower() != "programming":
        mistakes += 1

print("Your make " + str(mistakes) + " mistake(s).")
print("Now let's see your evalution")
t.sleep(3)

x = [1, 2, 3, 4, 5]
y = times
plt.plot(x, y)

legend = ["1", "2", "3","4","5"]
plt.xticks(x,legend)
plt.ylabel("Time in seconds")
plt.xlabel("Attempts")
plt.title("Your Typing Evalution")

plt.show()
