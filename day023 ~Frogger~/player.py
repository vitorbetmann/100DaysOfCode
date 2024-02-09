import turtle


class Player(turtle.Turtle):
    def __init__(self, y_range):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.speed("fastest")
        self.reset_position(y_range)

    def move_up(self):
        new_y = self.ycor() + 10
        self.setheading(90)
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 10
        self.setheading(270)
        self.goto(self.xcor(), new_y)

    def move_right(self):
        new_x = self.xcor() + 10
        self.setheading(0)
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 10
        self.setheading(180)
        self.goto(new_x, self.ycor())

    def reset_position(self, y_range):
        self.setheading(90)
        self.goto(0, int(-y_range / 2))

    def died(self):
        self.shape("circle")
        self.color("red")
