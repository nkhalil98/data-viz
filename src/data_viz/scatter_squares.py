import matplotlib.pyplot as plt
import numpy as np

# Styling
plt.style.use("seaborn-v0_8")

# Data
X = np.arange(1, 1001)
Y = X**2

# Initialize the plot and plot the data
fig, ax = plt.subplots()
ax.scatter(X, Y, s=10, c=Y, cmap=plt.cm.Blues)  # all the magic happens here

# Customize the plot
ax.set_title("Square Numbers", fontsize=24)  # title
ax.set_xlabel("Value", fontsize=14)  # x-axis label
ax.set_ylabel("Value Squared", fontsize=14)  # y-axis label
ax.axis([0, 1100, 0, 1_100_000])  # axis range
ax.ticklabel_format(style="plain")  # disable scientific notation
ax.tick_params(axis="both", labelsize=10)  # tick labels size

# Uncomment the line below to save the plot to a file (optional)
# plt.savefig("squares_plot.png", bbox_inches="tight")

# Display the plot
plt.show()
