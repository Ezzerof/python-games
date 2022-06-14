from turtle import Turtle
import random
colors = ["white", "red", "cyan", "yellow", "pink", "orange", "indigo", "green", "purple"]
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(1, 1)
        self.color("cyan")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(random.choice(colors))
        random_x = random.randint(-380,380)
        random_y = random.randint(-380,380)
        self.goto(random_x, random_y)