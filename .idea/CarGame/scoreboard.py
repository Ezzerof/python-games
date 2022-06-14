from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Black")
        self.hideturtle()
        self.penup()
        self.goto(-300, 350)
        self.level = 1
        self.write(f"Level: {self.level}", align="center",font=FONT)

    def next_level(self):
        self.level +=1
        self.clear()
        self.write(f"Level: {self.level}", align="center",font=FONT)

