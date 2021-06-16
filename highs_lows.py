"""
Read a CSV file of daily temperatures and plot on a line graph
"""

import csv
from datetime import date, datetime

from matplotlib import pyplot as plt

filename = 'data/death_valley_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates: list[datetime] = []
    highs: list[int] = []
    lows: list[int] = []
    for row in reader:
        try:
            date: datetime = datetime.strptime(row[2], "%Y-%m-%d")
            high_temp: int = int(row[6])
            low_temp: int = int(row[7])
        except ValueError:
            print(date.date(), 'missing data')
        else:
            dates.append(date)
            highs.append(high_temp)
            lows.append(low_temp)

# Plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', linewidth=1, alpha=0.5)
plt.plot(dates, lows, c='blue', linewidth=1, alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
plt.title('Death Valley daily high and low temperatures, 2018', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
