import csv
from datetime import datetime
import matplotlib.pyplot as plt

open_files = ["sitka_weather_2018_simple.csv", "death_valley_2018_simple.csv"]

smallnames = []
i = 0

fig, ax = plt.subplots(2)

for name in open_files:
    open_file = open(name, "r")
    reader = csv.reader(open_file, delimiter=",")
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print("Index", index, "Column Name: ", column_header)

    print(header_row)
    date_index = header_row.index("DATE")
    high_index = header_row.index("TMAX")
    low_index = header_row.index("TMIN")
    name_index = header_row.index("NAME")

    highs = []
    dates = []
    lows = []
    
    for row in reader:
        try: 
            high = int(row[high_index])
            low = int(row[low_index])
            smallname = row[name_index]
            converted_date = datetime.strptime(row[2], '%Y-%m-%d')
        except ValueError:
            print(f"missing data for {converted_date}")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(converted_date)
        smallnames.append(smallname)


    ax[i].fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

    plt.suptitle(
        "Temperature comparison between " + smallnames[0] + " and " + smallnames[-1],
        fontsize=10
    )

    ax[i].set_title(smallname, fontsize=16)
    plt.xlabel("", fontsize=12)
    plt.ylabel("Temperature (F)", fontsize=12)
    plt.tick_params(axis="both", labelsize=12)

    ax[i].plot(dates,highs,c='red')
    ax[i].plot(dates,lows,c='blue')
    fig.autofmt_xdate()
    i += 1

plt.show()
