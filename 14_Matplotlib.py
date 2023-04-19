import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[1500,1400,1400,1600,1700]

# plt.plot(x,y)
# plt.show()

legend = ["Januari", "Februari", "Maret","April","Mei"]

plt.xticks(x,legend)

# plt.plot(x,y)
# plt.show()

plt.bar(x,y)
plt.ylabel("Sales Mind")
plt.title("Monthly Sales")

plt.show()