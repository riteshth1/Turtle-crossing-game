import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("light blue")
screen.tracer(0)

user = Player()

screen.listen()
screen.onkey(fun=user.go_up, key="Up")

car = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.make_car()
    car.move_cars()

    # Detect collision of the car with turtle
    for car1 in car.all_car:
        if car1.distance(user) < 20:
            game_is_on = False
            score.game_over()

    # detect if turtle cross finish line and increase difficulty level
    if user.ycor() > 280:
        user.go_to()
        car.speed_up_car()
        score.update_level()



screen.exitonclick()
