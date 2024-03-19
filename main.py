import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
score = Scoreboard()
cars = CarManager()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_car()
    if player.finish_line():
        player.start_position()
        cars.increse_speed()
        score.add_score()
    for car in cars.all_cars:
         if car.distance(player)<20:
             player.start_position()




screen.exitonclick()