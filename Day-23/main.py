# Turtle Crossing Game

from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
import time

# Setup the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

# Create Objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# The up key can be used to move the turtle upwards
screen.listen()
screen.onkey(player.up, "Up")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # If the player collides with any car - the game ends
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            is_game_on = False

    # If the player reaches the finish line then the game levels up
    if player.ycor() > 280:
        player.go_at_start()
        scoreboard.increase_level()
        car_manager.increase_speed()

screen.exitonclick()
