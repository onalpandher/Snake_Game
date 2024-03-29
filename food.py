from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()          #creating a function to refresh it recall it over when hit

    def refresh(self):
        random_x = random.randint(-280, 280)  # creating random axis for food
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

