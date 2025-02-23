import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-v0_8")

X = np.arange(1, 1001)
Y = X**2

fig, ax = plt.subplots()
ax.scatter(X, Y, s=10, c=Y, cmap=plt.cm.Blues)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Value Squared", fontsize=14)
ax.axis([0, 1_100, 0, 1_100_000])  # set the range of each axis
ax.ticklabel_format(style="plain")  # disable scientific notation
ax.tick_params(axis="both", labelsize=10)

# Uncomment the line below to save the plot to a file (optional)
# plt.savefig("squares_plot.png", bbox_inches="tight")

plt.show()
