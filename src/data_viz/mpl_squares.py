import matplotlib.pyplot as plt

# styling
plt.style.use("ggplot")

# data
X = [1, 2, 3, 4, 5]  # x-values
Y = [1, 4, 9, 16, 25]  # y-values
# NOTE: if x-values are not provided, matplotlib will use the index of each
# y-value as the x-value

# initialize the plot and plot the data
fig, ax = plt.subplots()
ax.plot(X, Y, linewidth=3)

# customize the plot
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Value Squared", fontsize=14)
ax.tick_params(axis="both", labelsize=14)

# display the plot
plt.show()
