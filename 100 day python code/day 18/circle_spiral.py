import turtle as t
import  random
t.colormode(255)
timmy = t.Turtle()
timmy.speed('fastest')

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colors = (r, g, b)
    return colors

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):    
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)
    
draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()