from turtle import Turtle
from random import randint

COLOURS = ['yellow', 'blue', 'green', 'orange', 'purple']
STARTINGPOSITIONS = [(400,-300), (400, -200), (400, -100), (400, 0), (400, 100), (400, 200), (400, 300)]

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape('square')
        self.speed(0)
        self.penup()
        self.color(COLOURS[randint(0,4)])
        self.setheading(180)
        self.setposition(STARTINGPOSITIONS[randint(0,6)])
        self.speed(randint(1,200))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.showturtle()
        


    

        
