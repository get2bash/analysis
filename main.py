import csv
import pandas
import turtle

"""
First implimentation using the csv library to read a csv file (trying out Data analysis with python for the first time).
"""
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temprature = []
#     for row in data:
#         if row[1] != "temp":
#             temprature.append(int(row[1]))
#     print(temprature)



"""
Second implimentation using pandas, and it's just three lines of code.
"""
# data = pandas.read_csv("weather_data.csv")
# temprature = data["temp"]



"""
Normal way to look for the mean of a list 
"""
# average = sum(temprature) / len(temprature)



"""
Using pandas you just call the mean method
"""
# average_2 = temprature.mean()



"""
U.S states naming quiz
"""
screen = turtle.Screen()
screen.title("U.S States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_answer = screen.textinput(title="U.S States", prompt="write the name of a state")