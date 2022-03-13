from turtle import Turtle
FONT = ("Arial", 12, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.pencolor("black")
        self.hideturtle()
        self.goto(330, 250)
        self.lives_spent = 0
        with open("high_score.txt", "r") as file:
            self.high_score = int(file.read())
        self.write(arg=f"High score: {self.high_score} lives\nLives spent: {self.lives_spent}", move=False, font=FONT)

    def refresh(self):
        self.clear()
        self.write(arg=f"High score: {self.high_score} lives\nLives spent: {self.lives_spent}", move=False, font=FONT)

    def game_end_check(self):
        if self.lives_spent < self.high_score:
            self.high_score = self.lives_spent
            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))
        self.refresh()
