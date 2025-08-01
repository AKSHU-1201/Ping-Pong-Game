from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier" , 24 , "normal")
class Scoreboard(Turtle):

    def __init__(self , score , position):
        super().__init__()
        self.penup()
        self.color("white")
        self.score = score
        self.hideturtle()
        self.goto(position)
        self.clear_score()

    def clear_score(self):
        self.clear()
        self.write(arg=f"{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear_score()
