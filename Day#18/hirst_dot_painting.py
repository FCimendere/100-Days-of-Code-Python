#Project: The Hirst Painting
"""
PRACTISE: This is a practise for understanding Turtle & the graphical user
"""



import random
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.colormode(255)
screen.setup(600, 600)
color_list = [(250, 248, 245), (242, 250, 247), (251, 243, 247), (239, 244, 248), (219, 154, 107), (133, 171, 195), (214, 130, 148), (223, 70, 89), (24, 119, 153), (239, 209, 102), (124, 179, 151), (38, 122, 86), (23, 166, 201), (215, 86, 77), (141, 84, 60), (148, 70, 92), (234, 163, 178), (177, 186, 214), (241, 165, 150), (169, 150, 74), (42, 167, 131), (162, 211, 176), (4, 91, 111), (153, 207, 218), (22, 56, 78), (28, 90, 60), (236, 216, 7), (50, 58, 88), (98, 126, 178), (71, 75, 45)]
tim.speed("fastest")


def turn_the_line():
    tim.setheading(90)
    tim.forward(40)
    tim.setheading(180)
    tim.setheading(0)
    
    
def draw_circle():
    score = 0
    x_start = -180
    y_start = -180
    while score < 10:
        tim.penup()
        tim.goto(x_start, y_start)
        for _ in range(10):
            tim.shape("circle")
            tim.color(random.choice(color_list))
            tim.stamp()
            tim.fd(40)
        turn_the_line()
        score += 1
        x_start += 0
        y_start += 40
        tim.hideturtle()


draw_circle()
screen.exitonclick()
