import random

from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('orange')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed('fastest')

    def move(self):
        self.goto(random.randint(-270, 270), random.randint(-270, 270))



