from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0) #Turtle animation is turned off


snake = Snake()
food = Food( )
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()#screen is updated agter turning off animation
    time.sleep(0.1) #0.1 sec delay after each segment moves
    snake.move()

    #detect collison with food -distance method - this compares the distance covered by turtle with the x,y coordinate
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280  or snake.head.ycor() > 280  or snake.head.ycor() < -280 :
          game_is_on = False
          scoreboard.game_over()
    
    #detect collision with tail. if head collides with any segment in the tail
    # for segment in snake.segments:
        # if segment == snake.head:
        #     pass
        # elif snake.head.distance(segment) < 10:
        #     game_is_on = False
        #     scoreboard.game_over()
    #same using slicing    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()


