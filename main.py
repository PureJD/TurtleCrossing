from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from cars import Cars
from random import randint
import time


screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor('grey')
screen.tracer(0)

player = Player() #Creates the turtle


car = []  #Car object creation and logic, creates the obeject and then places them in a list 
current_level = 1

def level_generator(current_level): 
    for i in range(current_level * 2):
        car.append(Cars())

score = Scoreboard() #Initiate the Scoreboard class object 
score.update_scoreboard(current_level) #Adds the inital score to the screen

def countdown():
    for i in range(10, 1, -1):
        score.countdown(i)
        screen.update()
        time.sleep(0.02)    
    score.countdown('GO')
    screen.update()
    time.sleep(0.2)



screen.listen()
screen.onkeypress(player.move_up, 'Up')
screen.onkeypress(player.move_down, 'Down')
screen.onkeypress(player.move_left, 'Left')
screen.onkeypress(player.move_right, 'Right')

level_generator(current_level) #inital car creation 

game_loop = True
while game_loop:
    screen.update()
    time.sleep(0.09) #Screen refresh rate. 
    for i in car:
        if i.xcor() < -380:      #Detects if the car object has exceeded the left side, if so it moves the X cor to the right side
            current_y = i.ycor()
            i.goto(380, current_y)

        if player.ycor() > 380:
            score.level_up(current_level)
            screen.update()
            time.sleep(1) 
            countdown() 
            current_level += 1
            score.update_scoreboard(current_level)
            level_generator(current_level)
            player.reset()
            break

            
            
        if player.distance(i) < 25: #######collision logic for player 
            score.lose()
            screen.update()
            time.sleep(2)
            game_loop = False


        i.forward(randint(0,50)) #Keeps the cars moving, all logic will be above this statement


screen.exitonclick()

        







