from turtle import Turtle,Screen
                   # * this means import all classes
# import turtle as t(alias name)     


timmy = Turtle()
timmy.shape('turtle')
timmy.color('green')


# for _ in range(2):
#     timmy.pencolor("gold1")
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()


# for _ in range(3):
#     timmy.forward(100)
#     timmy.right(120) #degree

# timmy.color('pink')
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90) #degree

# timmy.color('red')
# for _ in range(5):
#     timmy.forward(100)
#     timmy.right(72) 

# timmy.color('orange')
# for _ in range(6):
#     timmy.forward(100)
#     timmy.right(60) 

# timmy.color('yellow')
# for _ in range(7):
#     timmy.forward(100)
#     timmy.right(51.42857) 

# timmy.color('black')
# for _ in range(8):
#     timmy.forward(100)
#     timmy.right(45) 

# timmy.color('grey')
# for _ in range(9):
#     timmy.forward(100)
#     timmy.right(40) 

# timmy.color('blue')
# for _ in range(10):
#     timmy.forward(100)
#     timmy.right(36) 

#####################shortcut
import random

colors = ["red","green","yellow"]
def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shape in range(3,10):
    timmy.color(random.choice(colors))
    draw_shape(shape)

# screen = Screen()
# screen.exitonclick()

# to import heroes module write pip intsall heroes 

# import heroes
# print(heroes.gen())
















