from turtle import Turtle , Screen

class Paddle(Turtle):
    # Paddle
    def __init__(self, position):
        super().__init__()
        self.screen = Screen()
        self.shape("square")
        self.goto(position)
        self.penup()
        self.color("white")
        self. shapesize(stretch_len=1, stretch_wid=5)

    # Functions to make paddle move Up and Down
    def up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)

    def reset_position(self , position):
        self.goto(position)
