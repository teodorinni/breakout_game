from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("black")
        self.shapesize(0.75)
        self.penup()
        self.goto(0, -150)
        self.setheading(45)
        self.move_speed = 0.0005

    # method for bouncing from the walls
    def bounce(self):
        current_angle = self.heading()
        if self.xcor() >= 480 and current_angle <= 90:
            self.setheading(180 - current_angle)
        elif self.xcor() >= 480 and current_angle > 270:
            self.setheading(540 - current_angle)
        elif self.xcor() <= -480 and current_angle <= 180:
            self.setheading(180 - current_angle)
        elif self.xcor() <= -480 and current_angle > 180:
            self.setheading(540 - current_angle)
        elif self.ycor() >= 290:
            self.setheading(360 - current_angle)

    def move(self):
        self.bounce()
        self.forward(5)

    # method for bouncing from blocks
    def collision_block(self, direction):
        current_angle = self.heading()
        if direction == "vertical":
            self.setheading(360 - current_angle)
        else:
            if current_angle <= 180:
                self.setheading(180 - current_angle)
            else:
                self.setheading(540 - current_angle)

    # method for bouncing from paddle
    def collision_paddle(self, direction):
        current_angle = self.heading()
        if direction == "right":
            self.setheading(random.randint(30, 75))
        else:
            self.setheading(random.randint(105, 150))

    def refresh(self):
        self.goto(0, -150)
        self.setheading(45)
