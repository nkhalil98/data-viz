import csv
import datetime as dt
from pathlib import Path

import matplotlib.pyplot as plt

WEATHER_DATA_DIR = Path(__file__).parent / "assets"


def get_weather_data(path):
    """Extract high & low temperatures and their dates from a CSV file."""
    lines = path.read_text().splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)
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

    return highs, lows, dates


def plot_weather_data(highs, lows, dates, dataset):
    """Plot high & low temperatures."""
    plt.style.use("seaborn-v0_8-pastel")
    fig, ax = plt.subplots()
    ax.plot(dates, highs, color="red", alpha=0.5)
    ax.plot(dates, lows, color="blue", alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor="purple", alpha=0.1)
    dataset = dataset.replace("_", " ").title()
    ax.set_title(f"{dataset} daily high and low temperatures, 2021", fontsize=16)
    ax.set_xlabel("", fontsize=12)
    ax.set_ylabel("Temperature (F)", fontsize=12)
    fig.autofmt_xdate()

    plt.show()


if __name__ == "__main__":
    import argparse

    death_vally_path = WEATHER_DATA_DIR / "death_valley_2021_simple.csv"
    sitka_path = WEATHER_DATA_DIR / "sitka_weather_2021_simple.csv"

    parser = argparse.ArgumentParser()
    parser.add_argument("dataset", type=str, help="The dataset to visualize")
    args = parser.parse_args()
    dataset = args.dataset

    if dataset == "death_valley":
        path = death_vally_path
    elif dataset == "sitka":
        path = sitka_path
    else:
        raise ValueError("Invalid dataset")

    highs, lows, dates = get_weather_data(path)
    plot_weather_data(highs, lows, dates, dataset)
