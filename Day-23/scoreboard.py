from turtle import Turtle

# Set the font globally so if it needs to be changed then the whole code need not be scanned
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-350, 250)
        self.print_level()

    # Print the level on the left-upper of the screen
    def print_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    # Increase the level when player reaches finish line
    def increase_level(self):
        self.level += 1
        self.print_level()

    # If player collides then print Game Over in the middle
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=FONT)
