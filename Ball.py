from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 5
        self.y_move = 5
        self.move()


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)



    #Detecting collision on top and bottom walls
    def collision(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_move *= -1


    def bounce(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.x_move = 5
        self.y_move = 5
