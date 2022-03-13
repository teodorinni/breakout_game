from turtle import Turtle


class Block(Turtle):

    def __init__(self, x_coord, y_coord, color):
        super().__init__()
        self.penup()
        self.shape("square")
        self.resizemode("user")
        self.speed("fastest")
        self.turtlesize(stretch_wid=1.5, stretch_len=1.5)
        self.color(color)
        self.goto(x=x_coord, y=y_coord)