from pathlib import Path
import csv

import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# extract high temperatures
highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)

# plot the high temperatures
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(highs, color='red')

# format plot
ax.set_title("Daily high temperatures, July 2021", fontsize = 24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show() 