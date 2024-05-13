from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-250, 250)
        self.write(f"Level: {self.level}",align="left",font= FONT)

    def update_level(self):
        self.clear()
        self.write(f"Level:{self.level}", align="left", font = FONT)

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="left", font=FONT)