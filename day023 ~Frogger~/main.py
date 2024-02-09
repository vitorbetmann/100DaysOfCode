import turtle
import time
from car import Car
import player
import scoreboard

start_time = time.time()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.tracer(0)

player = player.Player(SCREEN_HEIGHT * 0.9)
scoreboard = scoreboard.Scoreboard(SCREEN_WIDTH, SCREEN_HEIGHT)

screen.listen()
screen.onkey(player.move_up, "w")
screen.onkey(player.move_down, "s")
screen.onkey(player.move_right, "d")
screen.onkey(player.move_left, "a")

list_of_cars = []
limit_of_cars = 40

game_is_on = True
player_is_dead = False

while game_is_on:
    if player_is_dead:
        game_is_on = False
        scoreboard.game_over()

    time.sleep(0.01)
    screen.update()
    if len(list_of_cars) < limit_of_cars and time.time() - start_time >= 0.3:
        new_car = Car(SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.8))
        list_of_cars.append(new_car)
        start_time = time.time()

    for car in list_of_cars:
        car.move()
        if player.distance(car) < 15:
            player_is_dead = True
            player.died()
        if car.xcor() < -SCREEN_WIDTH / 2:
            car.reset_position(SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.8))

    if player.ycor() >= SCREEN_HEIGHT * 0.8 / 2:
        scoreboard.next_level()
        player.reset_position(SCREEN_HEIGHT * 0.9)
        for car in list_of_cars:
            car.increase_speed()

screen.exitonclick()
