from turtle import Turtle
ALIGNMENT = "center"
FONT =("Arial",23,"normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('day 24\snake_game\data.txt') as data:
            self.high_score = int(data.read())

        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(0,270)
        self.update_scoareboard()

    def update_scoareboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score = {self.high_score} ",move=False,align="center", font=("Arial",24,"normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('day 24\snake_game\data.txt',mode='w') as data:
                data.write(f"{self.high_score}")  
        self.score = 0 #to reset the score after getting high score  
        self.update_scoareboard()  


    def increase_score(self):
        self.score +=1
       
        self.update_scoareboard()







