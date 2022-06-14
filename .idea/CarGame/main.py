import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=800)
screen.tracer(0)

turtle = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.move,'Up')



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.movement()

# Car collision with turtle
    for car in cars.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False

# Making the finish line
    if turtle.ycor() > 280:
        cars.lvl_up()
        turtle.reset()
        scoreboard.next_level()
