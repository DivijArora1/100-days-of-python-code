import turtle
import pandas
screen = turtle.Screen()

screen.title('US States Game')
image = "day 25/states game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("day 25/states game/50_states.csv")
all_states = data["state"].to_list()

guessed_states = []
while len(guessed_states) <50:

    answer_state = screen.textinput(title =  f"{len(guessed_states)}/50" ,prompt="What's another sate's name").title()
    # print(answer_state)


    #if answer state is one in all the states of the 50 states    
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)    
        new_data = pandas.DataFrame(missing_states)    
        new_data.to_csv("day 25/states game/states_to_learn.csv")
        break  
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        # t.write(answer_state)
        t.write(state_data.state.item())#this item method grabs the first element of the data ie will not read the junk



#states _to_learn.csv


screen.exitonclick()

 
