# Know Your India Game

import turtle
import pandas

screen = turtle.Screen()
screen.title("Know Your India")
image = "india_map.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

data = pandas.read_csv("India_States&UTs.csv")
india_states = data["state"].to_list()

score = 0
correct_guesses = []
game_on = True
while len(correct_guesses) < len(india_states):
    answer_state = screen.textinput(title=f"{score} out of 36", prompt="Enter a state").title()

    if answer_state == "Exit":
        missing_state = []
        for state in india_states:
            if state not in correct_guesses:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break

    elif answer_state in correct_guesses:
        pass

    elif answer_state in india_states:
        new_x = data[data["state"] == answer_state]["x"].iloc[0]
        new_y = data[data["state"] == answer_state]["y"].iloc[0]
        writer.goto(new_x, new_y)
        writer.write(answer_state)
        score += 1
        correct_guesses.append(answer_state)

