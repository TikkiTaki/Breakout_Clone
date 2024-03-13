from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Lives(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.lives = 10
        self.hideturtle()
        self.penup()
        self.goto(-150, 370)
        self.update_lives()

    def update_lives(self):
        self.clear()
        self.write(f"Lives: {self.lives}", align="left", font=FONT)

    def decrease_lives(self):
        self.lives -= 1
        self.update_lives()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)

