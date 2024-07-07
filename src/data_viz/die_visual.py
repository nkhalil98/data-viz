import plotly.express as px

from die import Die

# Data
die = Die()
rolls = [die.roll() for _ in range(10_000)]
possible_values = range(1, die.num_sides + 1)  # 1 to 6 for a D6
frequencies = [rolls.count(value) for value in possible_values]

# Plot the data
fig = px.bar(
    x=possible_values,
    y=frequencies,
    labels={"x": "Value", "y": "Frequency"},
    title=f"Results of rolling one {die.name} 10,000 times",
)
fig.update_layout(xaxis_dtick=1)

# Uncomment the line below to save the plot to a file
# fig.write_html("d6_visual.png")

fig.show()
