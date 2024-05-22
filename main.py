import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pd.read_csv('50_states.csv')
states = data.state.to_list()

guessed_state = []

while len(guessed_state) < 50:
    answer = turtle.textinput(title= f"{len(guessed_state)}/50 States Guessed", prompt= "Guess the state").title()
    if answer == "Exit":
        break
    if answer in states and answer not in guessed_state:
        guessed_state.append(answer)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_info = data[answer == data.state]
        t.goto(int(state_info.x), int(state_info.y))
        t.write(answer)

