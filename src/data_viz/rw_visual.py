import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Styling
plt.style.use("seaborn-v0_8-darkgrid")

# Random walk data
rw = RandomWalk()
rw.fill_walk()

# Initialize the plot and plot the data
fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
point_numbers = range(rw.n)
ax.scatter(
    rw.X,
    rw.Y,
    s=10,
    c=point_numbers,
    cmap=plt.cm.Blues,
    edgecolors=None,
)

# Emphasize the first and last points
ax.scatter(0, 0, c="green", edgecolors=None, s=50)
ax.scatter(rw.X[-1], rw.Y[-1], c="red", edgecolors=None, s=50)

# Customize the plot
ax.set_aspect("equal")  # equal aspect ratio
ax.get_xaxis().set_visible(False)  # hide x-axis
ax.get_yaxis().set_visible(False)  # hide y-axis

plt.show()
