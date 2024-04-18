from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from cars import Cars
from random import randint


screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor('grey')


player = Player() #Creates the turtle


car = []  #Car object creation and logic, creates the obeject and then places them in a list 
for i in range(10):
    car.append(Cars())

score = Scoreboard() #Initiate the Scoreboard class object 
score.update_scoreboard() #Adds the inital score to the screen





screen.listen()
screen.onkeypress(player.move_up, 'Up')
screen.onkeypress(player.move_down, 'Down')
screen.onkeypress(player.move_left, 'Left')
screen.onkeypress(player.move_right, 'Right')



game_loop = True
while game_loop:

    for i in car:
        if i.xcor() < -380:      #Detects if the car object has exceeded the left side, if so it moves the X cor to the right side
            current_y = i.ycor()
            i.goto(380, current_y)

        if player.ycor() > 380:
            game_loop = False ##############Logic to be called to change level 

        if player.distance(i) < 30: #######collision logic for player 
            game_loop = False


        i.forward(randint(0,50)) #Keeps the cars moving, all logic will be above this statement


screen.exitonclick()

        







