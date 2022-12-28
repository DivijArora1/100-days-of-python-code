from turtle import Turtle,Screen
import random 

is_race_on = False
screen = Screen()
screen.setup(width= 500, height=400)
user_bet = screen.textinput(title="Make your bet" , prompt="which turtle will win the race ? Enter a color: ")
colors = [ "red","orange" , "yellow", "green", "blue" , "purple" ]
y_positions = [-90,-50,-10,30,70,110]
all_turtles = []

for turtle_index in range(0,6): #0,1,2,3,4,5
    tim = Turtle(shape = "turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x= -230, y=y_positions[turtle_index])
    all_turtles.append(tim)

if user_bet:
    is_race_on= True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor() #note we have not chose .color() as it receives two argument .color(pencolor, filledcolor)
            if winning_color == user_bet:
                print(f"You have won! The Winning color is {winning_color} ")
            else:
                print(f"You have lost! The winning color is {winning_color}")    
                
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()