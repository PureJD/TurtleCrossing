from turtle import Turtle
STARTING_POS = (0, -380)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('green')
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.setpos(STARTING_POS)
    
    def move_up(self): 
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    def move_down(self): 
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
    def move_left(self): 
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())
    def move_right(self): 
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())



