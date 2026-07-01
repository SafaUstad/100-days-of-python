# The Turtle Race Project 
from turtle import Turtle, Screen
import random

screen = Screen()
# Set the screen size according to you
screen.setup(width=500, height=400)

# Take the users bet
user_bet = screen.textinput(title="Make your bet", prompt="Your bet")
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
turtles = []

# Create all turtles in different colors and at the start of the race
y = -100
for i in range(6):
    turt = Turtle(shape="turtle")
    turt.penup()
    turt.color(colors[i])
    turt.goto(-230, y)
    y += 40
    turtles.append(turt)

is_race_on = False

# Don't let the race until the user enters the bet
if user_bet:
    is_race_on = True

# All the turtles move forward until any one reaches the end
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You win! The winner is {winner} turtle")
            else:
                print(f"You lose! The winner is {winner} turtle")

        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)

screen.exitonclick()
