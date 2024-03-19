FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.update_score()
    def update_score(self):
        self.write(f"score = {self.score}",align="center",font=FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.update_score()


