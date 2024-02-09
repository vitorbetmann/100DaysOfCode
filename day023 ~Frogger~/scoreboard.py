import turtle

FONT_FAMILY = "Courier"
FONT_SIZE = 20
FONT_TYPE = "bold"
FONT = (FONT_FAMILY, FONT_SIZE, FONT_TYPE)
ALIGN = "center"


class Scoreboard(turtle.Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level_num = 0
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.next_level()

    def next_level(self):
        self.level_num += 1
        self.clear()
        self.goto(-self.screen_width * 0.8 / 2, self.screen_height * 0.8 / 2)
        self.write(arg=f"level: {self.level_num}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)
