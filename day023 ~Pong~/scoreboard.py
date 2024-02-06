from turtle import Turtle
SCREEN_HEIGHT = 600
FONT_FAMILY = "Courier"
FONT_SIZE = 80
FONT_TYPE = "normal"
FONT = (FONT_FAMILY, FONT_SIZE, FONT_TYPE)
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, SCREEN_HEIGHT / 3)
        self.write(arg=f"{self.l_score} {self.r_score}", align=ALIGN, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

