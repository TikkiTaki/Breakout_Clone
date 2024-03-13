from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-290, 370)
        self.update_level()

    def update_level(self):
        self.clear()
        if self.level < 6:
          self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"YOU WIN!", align="center", font=FONT)

