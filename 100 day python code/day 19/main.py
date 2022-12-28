from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_clockwise():
    tim.right(10)

def move_anti_clockwise():
    tim.left(10)
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

screen.onkey(move_forward , "w")#no paranthesis
screen.onkey(move_backward , "s")
screen.onkey(move_anti_clockwise , "a")
screen.onkey(move_clockwise , "d")
screen.onkey(clear_screen , "c")




screen.exitonclick()




 
    
