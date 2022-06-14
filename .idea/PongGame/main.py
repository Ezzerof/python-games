import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = t.Screen()
screen.setup(800,600)
screen.bgcolor('black')
screen.title('Muc-Pong')
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on == True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.movement()

    #Detecting collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detecting right wall collision
    if ball.xcor() > 380:
        ball.reset_possition()
        scoreboard.l_point()

     # Detecting left wall collision
    if ball.xcor() < -380:
        ball.reset_possition()
        scoreboard.r_point()

    # Detecting collision with paddles
    if ball.distance(r_paddle) < 55 and ball.xcor() > 325 or ball.distance(l_paddle) < 55 and ball.xcor() < -325:
        ball.bounce_x()
