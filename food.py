from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)  # Slightly larger & rounder
        self.color("deep pink")  # Fun vibrant color
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        colors = ["deep pink", "lime", "cyan", "gold", "orchid", "aqua", "red"]
        self.color(random.choice(colors))
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

