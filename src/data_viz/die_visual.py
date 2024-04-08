from collections import Counter

import plotly.express as px

from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
rolls = [die.roll() for _ in range(10_000)]

# Analyze the results.
possible_values = range(1, die.num_sides + 1)
frequencies_dict = Counter(rolls)
frequencies = [0 for _ in possible_values]
for k, v in frequencies_dict.items():
    frequencies[k - 1] = v

# Visualize the results.
fig = px.bar(
    x=possible_values,
    y=frequencies,
    labels={"x": "Value", "y": "Frequency"},
    title="Results of rolling one D6 10,000 times",
)
fig.update_layout(xaxis_dtick=1)

# Uncomment the line below to save the plot to a file.
# fig.write_html("d6_visual.png")

fig.show()
