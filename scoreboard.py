from turtle import Turtle




class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color("black")
        self.penup()
        self.hideturtle()
        

    def update_scoreboard(self, current_level):
        self.clear()
        self.goto(-300, 330)
        self.write(f'Level {current_level}', align="center", font=("Courier", 20, "normal"))

  
    def level_up(self, current_level):
        self.clear()
        self.goto(0, 0)
        self.write(f'LEVEL {current_level} COMPLETE!', align="center", font=("Courier", 20, "normal"))

    def lose(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'YOU HAVE BEEN FLATTENED!', align="center", font=("Courier", 20, "normal"))    

    def countdown(self, countdown):
        self.clear()
        self.goto(40, 0)
        self.write(f'{countdown}!', align="center", font=("Courier", 200, "normal"))
        
    
    
        
    
        

