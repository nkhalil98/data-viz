import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk, and plot the points.
rw = RandomWalk()
rw.fill_walk()

# Styling
plt.style.use("seaborn-v0_8-darkgrid")

fig, ax = plt.subplots(figsize=(16, 10), dpi=128)
point_numbers = range(rw.num_points)
ax.scatter(
    rw.x_values,
    rw.y_values,
    s=10,
    c=point_numbers,
    cmap=plt.cm.Blues,
    edgecolors="none",
)
ax.set_aspect("equal")

# Emphasize the first and last points.
ax.scatter(0, 0, c="green", edgecolors="none", s=50)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=50)

# Remove the axes.
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
