from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.left(90)
        self.penup()
        self.go_to()

    def go_up(self):
        """Moving the turtle forward by Moving Distance 10"""
        self.forward(MOVE_DISTANCE)

    def go_to(self):
        self.goto(STARTING_POSITION)


