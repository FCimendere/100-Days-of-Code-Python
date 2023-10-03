import time
from turtle import Screen
from player_turtles import Player
from car_manager import CarManager
from scoreboard_turtles import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim_player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=tim_player.move_turtle, key="Up")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(tim_player) <20:
            game_is_on = False
            scoreboard.game_over()

    if tim_player.is_at_finist_line():
        tim_player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()









