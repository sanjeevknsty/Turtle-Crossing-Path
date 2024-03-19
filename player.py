STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.position()
    def position(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)
    def move(self):
        move_y  = self.ycor() + MOVE_DISTANCE
        self.goto(0,move_y)

    def  finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def start_position(self):
        self.clear()
        self.position()


