import matplotlib.pyplot as plt

# Styling
plt.style.use("ggplot")

# Data
X = [1, 2, 3, 4, 5]  # x-values
Y = [1, 4, 9, 16, 25]  # y-values

# Initialize the plot and plot the data
fig, ax = plt.subplots()
ax.plot(X, Y, linewidth=3)  # all the magic happens here

# Customize the plot
ax.set_title("Square Numbers", fontsize=24)  # title
ax.set_xlabel("Value", fontsize=14)  # x-axis label
ax.set_ylabel("Value Squared", fontsize=14)  # y-axis label
ax.tick_params(axis="both", labelsize=14)  # tick labels size

# Display the plot
plt.show()
