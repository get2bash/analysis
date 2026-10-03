import csv
import pandas
import turtle

"""
First implementation using the csv library to read a csv file (trying out Data analysis with python for the first time).
"""
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temprature = []
#     for row in data:
#         if row[1] != "temp":
#             temprature.append(int(row[1]))
#     print(temprature)



"""
Second implementation using pandas, and it's just three lines of code.
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

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
correct_states = []

while len(correct_states) < 50:
    state_answer = screen.textinput(title=f"You have {len(correct_states)}/50", prompt="write the name of a state")
    response = state_answer.title()
    if response == "Exit":
        break
    if response in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == response]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(response)
        correct_states.append(response)
        score += 1

