import matplotlib.pyplot as plt

# Styling
plt.style.use("seaborn-v0_8")

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Blues)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Value Squared", fontsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style="plain")

# Set size of tick labels.
ax.tick_params(axis="both", labelsize=10)

# Uncomment the line below to save the plot to a file.
# plt.savefig("squares_plot.png", bbox_inches="tight")

plt.show()
