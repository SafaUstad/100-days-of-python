from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_INCREMENT

    def create_car(self):
        # Create car randomly by getting 1 so it does not create traffic
        random_choice = random.randint(1, 5)
        if random_choice == 1:
            car = Turtle()
            car.shape("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            car.goto(380, random_y)
            self.all_cars.append(car)

    # Move car left to right
    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    # Increase the speed of the car when leveled up
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
