import json
from pathlib import Path

import plotly.express as px


EARTHQUAKES_DATA_DIR = Path(__file__).parent / "assets" / "eq_data_1_day_m1.geojson"

contents = EARTHQUAKES_DATA_DIR.read_text(encoding="utf-8")
data = json.loads(contents)
data_title = data["metadata"]["title"]
earthquake_data = data["features"]

# extract earthquake locations and magnitudes
magnitudes, longitudes, latitudes, titles = [], [], [], []
for earthquake in earthquake_data:
    magnitudes.append(earthquake["properties"]["mag"])
    titles.append(earthquake["properties"]["title"])
    longitudes.append(earthquake["geometry"]["coordinates"][0])
    latitudes.append(earthquake["geometry"]["coordinates"][1])

fig = px.scatter_geo(
    lat=latitudes,
    lon=longitudes,
    size=magnitudes,
    color=magnitudes,
    color_continuous_scale="Viridis",
    labels={"color": "Magnitude"},
    projection="natural earth",
    title=data_title,
    hover_name=titles,
)

fig.show()


def format_json(path: Path, new_path: Path, indent: int = 4) -> str:
    """Format JSON data and save it to a new file."""
    contents = path.read_text(encoding="utf-8")
    data = json.loads(contents)
    formatted_data = json.dumps(data, indent=indent)
    new_path.write_text(formatted_data, encoding="utf-8")
