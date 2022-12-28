'''import another_module
print(another_module.another_variable)

from turtle import Turtle, Screen

timmy = Turtle()#class
print(timmy)
timmy.shape("turtle") # take the shape of the turtle
timmy.color("coral")
timmy.forward(100)

my_screen = Screen() #object(screen) created
print(my_screen.canvheight)#height of screen 
my_screen.exitonclick() #the screen will continue untill we click on the screen to stop the turtle
#check turtle graphics documents in python docs'''


#python pakages
# pip install PrettyTable

from prettytable import PrettyTable #class
table = PrettyTable() #obj created
table.add_column("Pokemon", ["Pikachu","Squirtle","charmander"])
table.add_column("Type", ["Electric","Water","Fire"])
# table.align["Pokemon"] = "l"
table.align = "l"
print(table)












