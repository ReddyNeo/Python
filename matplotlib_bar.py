import matplotlib.pyplot as plt

plt.bar([2, 4, 6, 8], [8, 5, 6, 4], label="Bar1", color='k')

plt.bar([8, 7, 7, 9], [4, 9, 3, 6], label="Bar2", color='y')

plt.title("Info")
plt.legend()
plt.xlabel("Bar Number")
plt.ylabel("Bar Height")

plt.show()
