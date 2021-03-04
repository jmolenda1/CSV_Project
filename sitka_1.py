import csv
from datetime import datetime
open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)
print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []

#this is an example
'''
mydate = '2018-07-01'
converted_date = datetime.strptime(mydate,'%Y-%m-%d')

print(converted_date)

'''

for row in csv_file:
    highs.append(int(row[5]))

#print(highs)

import matplotlib.pyplot as plt

fig=plt.figure()

plt.plot(highs, c="red")
plt.title("Daily High Temepratures July 2018", fontsize=16)
plt.xlabel("", fontsize=16)
plt.ylabel("Temeprature (F)", fontsize=16)
plt.tick_params(axis="both", which='major', labelsize=16)


plt.show()

