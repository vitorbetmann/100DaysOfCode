# import colorgram
#
# colors = colorgram.extract('image.jpg', 25)
#
# rgb_colors = []
# for i in range(25):
#     r = colors[i].rgb.r
#     g = colors[i].rgb.g
#     b = colors[i].rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle
import random

turtle.colormode(255)
screen = turtle.Screen()
tim = turtle.Turtle()
tim.penup()
tim.setposition(-250, -250)
tim.speed("fastest")

color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53),
              (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48),
              (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155),
              (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]


def random_color(color_list):
    new_color = random.choice(color_list)
    return new_color


for i in range(10):
    for j in range(10):
        tim.dot(20, random_color(color_list))
        tim.forward(50)
    tim.setposition(-250, tim.ycor() + 50)

screen.exitonclick()
