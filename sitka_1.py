import csv
from datetime import datetime
open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)
print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
dates = []
lows = []

#this is an example
'''
mydate = '2018-07-01'
converted_date = datetime.strptime(mydate,'%Y-%m-%d')

print(converted_date)

'''

for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    converted_date = datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(converted_date)

#print(highs)

import matplotlib.pyplot as plt

fig=plt.figure()

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c ="blue")


plt.show()

