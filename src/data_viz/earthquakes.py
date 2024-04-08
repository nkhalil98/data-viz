import json
from pathlib import Path

import plotly.express as px

path = Path(__file__).parent / "assets" / "eq_data_1_day_m1.geojson"


def format_json(path: Path, new_path: Path, indent: int = 4) -> str:
    contents = path.read_text(encoding="utf-8")
    data = json.loads(contents)
    formatted_data = json.dumps(data, indent=indent)
    new_path.write_text(formatted_data, encoding="utf-8")


# Get the earthquake data
contents = path.read_text(encoding="utf-8")
data = json.loads(contents)
earthquake_data = data["features"]


# Extract the earthquake magnitudes and their locations
magnitudes, longitudes, latitudes, titles = [], [], [], []
for earthquake in earthquake_data:
    magnitude = earthquake["properties"]["mag"]
    title = earthquake["properties"]["title"]
    longitude = earthquake["geometry"]["coordinates"][0]
    latitude = earthquake["geometry"]["coordinates"][1]
    magnitudes.append(magnitude)
    titles.append(title)
    longitudes.append(longitude)
    latitudes.append(latitude)


# Plot the earthquake magnitudes
fig = px.scatter_geo(
    lat=latitudes,
    lon=longitudes,
    size=magnitudes,
    color=magnitudes,
    color_continuous_scale="Viridis",
    labels={"color": "Magnitude"},
    projection="natural earth",
    title="Global Earthquakes",
    hover_name=titles,
)
fig.show()
