from turtle import Turtle

class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.bricks = []

        # Add bricks to the screen
    def create_lvl(self):
        for y in range(200,400,50):
            for x in range(-50,50,65):
                brick = Turtle()
                brick.shape("square")
                brick.shapesize(stretch_wid=1, stretch_len=3)
                brick.color("blue")
                brick.penup()
                brick.goto(x, y)
                self.bricks.append(brick)



    def create_lvl2(self):
        for y in range(200,400,50):
            for x in range(-200,200,65):
                brick = Turtle()
                brick.shape("square")
                brick.shapesize(stretch_wid=1, stretch_len=3)
                brick.color("red")
                brick.penup()
                brick.goto(x, y)
                self.bricks.append(brick)

    def create_lvl3(self):
        for y in range(200, 300, 65):
            for x in range(-250, -100, 65):
                brick = Turtle()
                brick.shape("square")
                brick.shapesize(stretch_wid=1, stretch_len=3)
                brick.color("green")
                brick.penup()
                brick.goto(x, y)
                self.bricks.append(brick)

        for y in range(200, 300, 65):
            for x in range(100, 280, 65):
                brick = Turtle()
                brick.shape("square")
                brick.shapesize(stretch_wid=1, stretch_len=3)
                brick.color("green")
                brick.penup()
                brick.goto(x, y)
                self.bricks.append(brick)

    def create_lvl4(self):
        for y in range(0, 350, 65):
            for x in range(-250, -150, 65):
                brick = Turtle()
                brick.shape("square")
                brick.shapesize(stretch_wid=1, stretch_len=3)
                brick.color("yellow")
                brick.penup()
                brick.goto(x, y)
                self.bricks.append(brick)

        for y in range(0, 350, 65):
            for x in range(180, 300, 65):
                brick = Turtle()
                brick.shape("square")
                brick.shapesize(stretch_wid=1, stretch_len=3)
                brick.color("yellow")
                brick.penup()
                brick.goto(x, y)
                self.bricks.append(brick)

    def create_lvl5(self):
        for y in range(150, 350, 50):
            for x in range(-250, -150, 50):
                brick = Turtle()
                brick.shape("square")
                brick.shapesize(stretch_wid=1, stretch_len=2)
                brick.color("orange")
                brick.penup()
                brick.goto(x, y)
                self.bricks.append(brick)

        for y in range(150, 350, 50):
            for x in range(180, 280, 50):
                brick = Turtle()
                brick.shape("square")
                brick.shapesize(stretch_wid=1, stretch_len=2)
                brick.color("orange")
                brick.penup()
                brick.goto(x, y)
                self.bricks.append(brick)

        for y in range(150, 400, 50):
            for x in range(-50, 100, 50):
                brick = Turtle()
                brick.shape("square")
                brick.shapesize(stretch_wid=1, stretch_len=2)
                brick.color("orange")
                brick.penup()
                brick.goto(x, y)
                self.bricks.append(brick)