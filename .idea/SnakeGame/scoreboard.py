from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,365)
        self.color("white")
        self.penup()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
        self.updating_scoreboard()

    def updating_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))


    def inceaase_food(self):
        self.clear()
        self.score += 1
        self.updating_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game over.", align="center", font=("Arial", 24, "normal"))
