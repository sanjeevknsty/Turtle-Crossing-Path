COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random
import time

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed= STARTING_MOVE_DISTANCE
    def create_car(self):
        chamce = random.randint(1,3)
        if chamce == 1 :
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(270, random.randint(-250, 250))
            car.setheading(180)
            self.all_cars.append(car)
        self.move_car()

    def move_car(self):
        for i in self.all_cars:
                # time.sleep(0.1)
                i.forward(self.car_speed)
    def increse_speed(self):
        self.car_speed += MOVE_INCREMENT


