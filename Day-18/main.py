# The Hirst Painting Project
import random
import turtle as t

# Extract from a photo from importing colorgram
colors = [(246, 243, 238), (207, 163, 103), (241, 246, 242), (154, 76, 43), (223, 200, 136), (50, 92, 126), (175, 148, 38), (130, 161, 186), (141, 38, 19), (200, 95, 71), (50, 121, 94), (11, 94, 68), (146, 175, 147), (71, 49, 39), (160, 145, 159), (83, 74, 75), (55, 48, 52), (20, 81, 90), (30, 65, 78), (231, 177, 162), (183, 203, 172), (41, 66, 91), (14, 73, 59), (99, 142, 131), (66, 62, 64), (177, 191, 210), (107, 128, 154), (69, 63, 56)]

# Create an object
turt = t.Turtle()

t.colormode(255)

# Pen line and turtle must not be visible
turt.penup()
turt.hideturtle()
turt.speed(0)

# Direct it to the initial point to start
turt.setheading(225)
turt.forward(300)
turt.setheading(0)

# For 10 rows of 10 columns
for _ in range(10):
    for _ in range(10):
        dot_color = random.choice(colors)
        turt.dot(20, dot_color)
        turt.forward(50)
    turt.left(90)
    turt.forward(50)
    turt.left(90)
    turt.forward(500)
    turt.setheading(0)

# Screen must exit on click
screen = t.Screen()
screen.exitonclick()

