# from turtle import Turtle,Screen
import turtle as t
import  random


timmy = t.Turtle()
timmy.shape('turtle')
timmy.color('green')
timmy.shapesize(1, outline=1)
timmy.speed('fastest')
timmy.width(5)

#random color
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colors = (r,g,b)
    return colors

directions = [0,90,180,270,360]

# colors = ["red","green","yellow","blue","orange","pink","black","grey","black"]

for _ in range(400):
    timmy.setheading(random.choice(directions))
    timmy.forward(30)
    timmy.color(random_color())
  

screen = t.Screen()
screen.exitonclick()