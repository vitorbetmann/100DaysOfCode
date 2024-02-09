import turtle
import random


class Car(turtle.Turtle):
    def __init__(self, x_range, y_range):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.penup()
        self.r = random.randint(0, 255) / 255
        self.g = random.randint(0, 255) / 255
        self.b = random.randint(0, 255) / 255
        self.color(self.r, self.g, self.b)
        self.car_speed = 2
        self.reset_position(x_range, y_range)

    def move(self):
        new_x = self.xcor() - self.car_speed
        self.goto(new_x, self.ycor())

    def increase_speed(self):
        self.car_speed += self.car_speed * 0.5

    def reset_position(self, x_range, y_range):
        self.goto(x_range / 2 + random.randint(50, 100), random.randint(-int(y_range / 2), int(y_range / 2)))
