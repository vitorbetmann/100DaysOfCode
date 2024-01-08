import turtle
import random

screen = turtle.Screen()
width = 500
height = 400
screen.setup(width, height)
game_prompt = "Which turtle will win the race? (Enter a color):"
user_bet = screen.textinput(title="Make your bet", prompt=game_prompt).lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


starting_x = -width / 2 + 20
ending_x = -starting_x
starting_y = -height / 2 + 40
y_shift = height / len(colors)
for color in colors:
    new_turtle = turtle.Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(starting_x, starting_y)
    all_turtles.append(new_turtle)
    starting_y += y_shift


is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)
        if turtle.xcor() > ending_x:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You won! The {winning_color} turtle is the winner")
            else:
                print(f"You lost! The {winning_color} turtle is the winner")
            break

screen.exitonclick()
