from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 15


class CarManager:
    def __init__(self):
        self.all_car = []

    def make_car(self):
        """Creates a new car """
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.left(180)
            new_car.color(random.choice(COLORS))
            self.all_car.append(new_car)
            y = random.randint(-250, 250)
            new_car.setposition(300, y)
            self.all_car.append(new_car)

    def move_cars(self):
        """loop through the list and helps to move the car at the speed of 5"""
        for car in self.all_car:
            car.forward(STARTING_MOVE_DISTANCE)

    def speed_up_car(self):
        for car in self.all_car:
            car.forward(MOVE_INCREMENT)
