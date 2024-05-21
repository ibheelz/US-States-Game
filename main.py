import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv('50_states.csv')
states = (data['state'])

correct = 0
answer = screen.textinput(title=f"{correct}/50 States Correct", prompt="What's another state's name?")


turtle.mainloop() 
