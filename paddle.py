from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.resizemode("user")
        self.color("blue")
        self.turtlesize(stretch_wid=0.5, stretch_len=10)
        self.speed("fastest")
        self.goto(0, -260)

    def move_left(self):
        current_x = self.xcor()
        current_y = self.ycor()
        if current_x > -400:
            new_x = current_x - 20
            self.goto(new_x, current_y)

    def move_right(self):
        current_x = self.xcor()
        current_y = self.ycor()
        if current_x < 400:
            new_x = current_x + 20
            self.goto(new_x, current_y)
