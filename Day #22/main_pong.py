#Game: Pong
"""
PRACTISE: Instances, State, Higher Order Functions, Animations & Coordinates
PROJECT: This is a highly popular arcade game Pong. 
Two players play the game. The purpose is catch the balls with paddles. 
If ball goes out, other player will take a point. 
"""


from turtle import Turtle, Screen
from paddle import ShapePaddle
from ball_pong import BouncingBall
from scoreboard_pong import Scoreboard
import time


screen = Screen()
screen.tracer(0)

tim = Turtle()
ball = BouncingBall()
score = Scoreboard()
r_paddle = ShapePaddle((350, 0))
l_paddle = ShapePaddle((-350, 0))

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Game: Pong")

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

tim.color("white")
tim.hideturtle()
tim.penup()
tim.goto(0, -280)
tim.setheading(90)
tim.pensize(5)
tim.speed("fastest")

while tim.ycor() < 200:
    tim.pendown()
    tim.forward(20)
    tim.penup()
    tim.forward(20)

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddels
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.ycor() > -320:
        ball.bounce_x()



    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()



screen.exitonclick()