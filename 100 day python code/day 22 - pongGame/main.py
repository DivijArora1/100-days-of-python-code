from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.tracer(0)  # Turtle animation is turned off
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with the wall
    # bouncing the ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # detect collisiom with the  paddle
    #       20px ball + 20px paddle    paddle top k lie
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -360:
        ball.bounce_x()
    # detect when right paddle misses the ball
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()
    # detect when left paddle misses the ball
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
