import csv
from datetime import datetime
open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)
print(type(header_row))

##The enumerate() function returns both of the inex of each item and
#  the value of each item through a list

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
dates = []

#this is an example
'''
mydate = '2018-07-01'
converted_date = datetime.strptime(mydate,'%Y-%m-%d')

print(converted_date)

'''

for row in csv_file:
    highs.append(int(row[5]))
    converted_date = datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(converted_date)

#print(highs)

#plot on a chart

import matplotlib.pyplot as plt

fig=plt.figure()

plt.plot(dates, highs, c="red")

fig.autofmt_xdate()

plt.title("Daily High Temperatures July 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12)


plt.show()

