#Game: Snake
"""
PRACTISE: Instances, State, Higher Order Functions, Animations & Coordinates
PROJECT: This is a highly popular game Snake. 
A snake will appear on the screen and you can control it by using arrow keys. 
The purpose is to catch the food. Do not forget you cannot touch the walls or your own tail.
"""


from turtle import Screen
from snake import Snake
from food import Food
from snake_scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to the snake game!")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor() >280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    #detect colliison with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            score.game_over()


screen.exitonclick()
