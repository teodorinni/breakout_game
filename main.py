import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from block import Block
from score import Score

blocks_list = []

# screen setup
screen = Screen()
screen.setup(width=1000, height=600)
screen.title("Breakout Game")
screen.tracer(0)

ball = Ball()

paddle = Paddle()

# blocks generation
x_start = -475
for n in range(0, 28):
    new_block = Block(x_start, 100, "red")
    x_start += 35
    blocks_list.append(new_block)
x_start = -475
for n in range(0, 28):
    new_block = Block(x_start, 65, "orange")
    x_start += 35
    blocks_list.append(new_block)
x_start = -475
for n in range(0, 28):
    new_block = Block(x_start, 30, "yellow")
    x_start += 35
    blocks_list.append(new_block)
x_start = -475
for n in range(0, 28):
    new_block = Block(x_start, -5, "green")
    x_start += 35
    blocks_list.append(new_block)

score = Score()

screen.listen()
screen.onkeypress(fun=paddle.move_left, key="Left")
screen.onkeypress(fun=paddle.move_right, key="Right")


def game():
    global game_is_on
    ball.move()
    time.sleep(ball.move_speed)
    screen.update()
    # bounces from paddles logic
    if ball.distance(paddle) < 100 and ball.ycor() < -250 and ball.xcor() < paddle.xcor():
        ball.collision_paddle("left")
        ball.move_speed *= 0.85
    elif ball.distance(paddle) < 100 and ball.ycor() < -250 and ball.xcor() >= paddle.xcor():
        ball.collision_paddle("right")
        ball.move_speed *= 0.85
    # out of bounds logic
    elif ball.ycor() <= -280:
        ball.refresh()
        score.lives_spent += 1
        score.refresh()
    # check for collision with blocks
    for block in blocks_list:
        x_ball = ball.xcor()
        y_ball = ball.ycor()
        x_block = block.xcor()
        y_block = block.ycor()
        x_diff = abs(x_ball - x_block)
        y_diff = abs(y_ball - y_block)
        if ball.distance(block) < 25 and x_diff < y_diff:
            ball.collision_block("vertical")
            block.hideturtle()
            blocks_list.remove(block)
        elif ball.distance(block) < 25 and x_diff >= y_diff:
            ball.collision_block("horizontal")
            block.hideturtle()
            blocks_list.remove(block)
    # game end logic
    if len(blocks_list) < 1:
        game_is_on = False
        screen.update()
        score.game_end_check()


game_is_on = True
while game_is_on:
    game()


screen.exitonclick()
