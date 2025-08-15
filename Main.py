from turtle import Screen , Turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

#Screen
screen = Screen()
screen.setup(width=800 , height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
screen.tracer(0)

#Middle line
dashed_line = Turtle()
dashed_line.color("white")
dashed_line.hideturtle()
dashed_line.penup()
dashed_line.goto(0 , -300)
dashed_line.setheading(90)

for _ in range(500):
    dashed_line.pendown()
    dashed_line.fd(10)
    dashed_line.penup()
    dashed_line.fd(10)


#Paddles
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
screen.onkey(fun=r_paddle.up , key= "Up")
screen.onkey(fun= r_paddle.down, key="Down" )
screen.onkey(fun=l_paddle.up , key="w" )
screen.onkey(fun=l_paddle.down, key="s" )

#Ball
ball = Ball()


#scoreboard things
r_score = 0
l_score = 0

r_scoreboard = Scoreboard(r_score , (100 , 250))
l_scoreboard = Scoreboard(l_score , (-100 , 250))



is_game_on = True
while is_game_on:

    time.sleep(0.02)
    screen.update()
    ball.move()
    ball.collision()


    #Right paddle collision
    if ball.xcor() > 320 and r_paddle.distance(ball) < 50:
        ball.bounce()

    # Left paddle collision
    if ball.xcor() < -320 and l_paddle.distance(ball) < 50:
        ball.bounce()

    #right paddle misses
    if ball.xcor() > 400:
        l_scoreboard.increase_score()
        ball.reset_position()
        r_paddle.reset_position((350,0))

    if ball.xcor() < -400:
        r_scoreboard.increase_score()
        ball.reset_position()
        l_paddle.reset_position((-350, 0))

screen.exitonclick()
