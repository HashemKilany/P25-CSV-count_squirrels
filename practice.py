import csv
import pandas

# with open("weather_data.csv","r") as data:
#     data = csv.reader(data)
#     # for a in data:
#     #     print(a)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)
data = pandas.read_csv("weather_data.csv")
#temp_list = data["temp"].tolist()
# average = sum(temp_list)/ len(temp_list)
# print(average)

# average = data["temp"].mean()
maxi = data.temp.max()
# print(maxi)

# hottest_day = data[data.temp == maxi]
# print(hottest_day)

# monday = data[data.day == "Monday"]
# print(monday.temp+273)
