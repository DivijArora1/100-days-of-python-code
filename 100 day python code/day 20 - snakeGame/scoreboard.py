from turtle import Turtle
ALIGNMENT = "center"
FONT =("Arial",23,"normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(0,270)
        self.update_scoareboard()

    def update_scoareboard(self):
        self.write(f"Score : {self.score} ",move=False,align="center", font=("Arial",24,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER YOU ARE DEAD ",move=False,align="center", font=("Arial",24,"normal"))

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoareboard()

