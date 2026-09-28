import csv

"""
First implimentation using the csv library to read a csv file (trying out Data analysis with python for the first time).
"""
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temprature = []
    for row in data:
        if row[1] != "temp":
            temprature.append(int(row[1]))
    print(temprature)