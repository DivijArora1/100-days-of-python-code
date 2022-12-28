import turtle as turtle_module
import  random

turtle_module.colormode(255)
timmy = turtle_module.Turtle()
color_list = [(250, 246, 241), (250, 244, 247), (242, 249, 246), (242, 245, 249), (207, 155, 102), (57, 107, 128), (162, 82, 43), 
(125, 79, 97), (122, 156, 171), (126, 175, 159), (195, 142, 39), (226, 198, 130), (188, 89, 109), (191, 131, 145), (14, 44, 57), (53, 38, 19), (51, 164, 128), (59, 121, 114), (218, 90, 70), (159, 22, 32), (41, 31, 33), (8, 30, 28), (81, 146, 165), (238, 167, 162), (156, 28, 21), (23, 80, 91), (233, 168, 173), (173, 206, 188), (106, 126, 157), (26, 87, 84), (164, 202, 208), (89, 69, 31), 
(52, 62, 82), (185, 189, 205)]

timmy.hideturtle()
timmy.setheading(220)
timmy.penup()
timmy.forward(400)
timmy.pendown()
timmy.setheading(0)
timmy.speed("fastest")
for _ in range(10):
    for _ in range(10):
        timmy.dot(40, random.choice(color_list))
        timmy.penup()
        timmy.fd(60)
        timmy.pendown()
    timmy.setheading(175)    
    timmy.penup()
    timmy.forward(601)
    timmy.pendown()
    timmy.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()



