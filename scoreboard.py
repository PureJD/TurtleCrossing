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

    def countdown_3(self):
        self.clear()
        self.write(f'3', align="center", font=("Courier", 20, "normal"))
        
    
    def countdown_2(self):
        self.clear()
        self.write(f'2', align="center", font=("Courier", 20, "normal"))
        

    def countdown_1(self):
        self.clear()
        self.write(f'1', align="center", font=("Courier", 20, "normal"))
        
    
    def countdown_go(self):
        self.clear()
        self.write(f'GO!', align="center", font=("Courier", 20, "normal"))
        
        
    
        

