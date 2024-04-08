import csv
import datetime as dt
from pathlib import Path

import matplotlib.pyplot as plt

path = Path(__file__).parent / "assets" / "death_valley_2021_simple.csv"

lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract high & low temperatures and their dates
highs_col_index = header_row.index("TMAX")
lows_col_index = header_row.index("TMIN")
dates_col_index = header_row.index("DATE")
highs, lows, dates = [], [], []
for row in reader:
    date = dt.datetime.strptime(row[dates_col_index], "%Y-%m-%d")
    try:
        high = int(row[highs_col_index])
        low = int(row[lows_col_index])
    except ValueError:
        print(f"Missing data for {row[dates_col_index]}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(date)

# Plot high & low temperatures
plt.style.use("seaborn-v0_8-pastel")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="purple", alpha=0.1)
ax.set_title("Death Valley daily high and low temperatures, 2021", fontsize=20)
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
fig.autofmt_xdate()

plt.show()
