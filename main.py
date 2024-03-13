import turtle
from brick import Brick
from level import Level
from life import Lives
import time

# Screen
screen = turtle.Screen()
screen.title("Breakout_Clone")
screen.bgcolor("black")
screen.setup(width=600, height=800)
screen.tracer(0)  # Screen updates off

#LVL and Lives
level = Level()
level.update_level()
lives = Lives()
lives.update_lives()

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=.5, stretch_len=5)
paddle.penup()
paddle.goto(0, -350)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 100)
ball.dx = 3
ball.dy = -3

brick = Brick()
brick.create_lvl()

# Functions to move the paddle left and right
def move_paddle_left():
    x = paddle.xcor()
    if x > -240:
        paddle.setx(x - 40)

def move_paddle_right():
    x = paddle.xcor()
    if x < 240:
        paddle.setx(x + 40)

# Keyboard bindings
screen.listen()
screen.onkeypress(move_paddle_left, "Left")
screen.onkeypress(move_paddle_right, "Right")

# Main game loop
game_on = True
while game_on:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for collisions with walls
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1
    if ball.ycor() > 390:
        ball.dy *= -1
    # if ball.ycor() < -390:
    #     ball.goto(0, 0)
    #     ball.dy *= -1

    # Check for collisions with paddle
    if (ball.ycor() < -340) and (paddle.xcor() - 55 < ball.xcor() < paddle.xcor() + 55):
        ball.dy *= -1

    # Check for collisions with bricks
    for _ in brick.bricks:
        if _.distance(ball) < 35:
            _.goto(1000, 1000)  # Move brick off screen
            brick.bricks.remove(_)
            brick.hideturtle()
            ball.dy *= -1

    # Check for game over
    if ball.ycor() < -360:
        paddle.goto(0, -350)
        ball.goto(0, 100)
        ball.dx = 3
        ball.dy = -3
        lives.decrease_lives()
        lives.update_lives()

    if lives.lives == 0:
        game_on = False
        lives.game_over()

    if len(brick.bricks) == 0:
        paddle.goto(0, -350)
        ball.goto(0, 100)
        ball.dx = 3
        ball.dy = -3
        level.increase_level()
        level.update_level()
        if level.level == 2:
            brick.create_lvl2()
        if level.level == 3:
            brick.create_lvl3()
        if level.level == 4:
            brick.create_lvl4()
        if level.level == 5:
            brick.create_lvl5()
        if level.level == 6:
            game_on = False
            level.game_over()
        time.sleep(1)

# Keep the window open
screen.mainloop()