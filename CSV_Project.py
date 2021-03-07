import csv
from datetime import datetime

import matplotlib.pyplot as plt

open_file = "sitka_weather_07-2018_simple.csv"

with open(open_file) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    fix, ax = plt.subplots(2)

    csv_file = csv.reader(open_file, delimiter=",")

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    highs = []
    dates = []
    lows = []

    for row in reader:
        high = int(row[5])
        low = int(row[6])
        converted_date = datetime.strptime(row[2], '%Y-%m-%d')
        highs.append(high)
        lows.append(low)
        dates.append(converted_date)

#print(highs)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(2)

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c ="blue")

fig.autofmt_xdate()

plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)


plt.title("Death Valley, CA US", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)

plt.show()

a = plt.subplots(2)
a[0].plt(dates,highs,c='red')
a[1].plot(dates,lows,c='blue')

plt.show()
