from random import randint
import turtle
import time
import threading

game_screen = turtle.Screen()
game_screen.title("Catch the Turtle")
game_screen.bgcolor("light blue")

the_escapee = turtle.Turtle()
the_escapee.penup()
the_escapee.hideturtle()
the_escapee.setposition((randint(-250, 250)), (randint(-250, 250)))
the_escapee.shape("turtle")
the_escapee.color("green")
the_escapee.showturtle()
the_escapee.speed('fastest')


def turtle_movement():
    the_escapee.goto((randint(-250, 250)), (randint(-250, 250)))

game_screen.ontimer(turtle_movement, 1000)

the_player = turtle.Turtle()
#the_player.hideturtle()
the_player.speed('fastest')
the_player.penup()



points = 0


def player_movement():
    game_screen.onscreenclick(the_player.goto)



player_movement()


score = turtle.Turtle()
score.hideturtle()
score.color("black")
style = ('Courier', 20, 'italic')
score.penup()
score.goto(-25, 285)
score.write("Score: 0", font=style)


countdown_timer = turtle.Turtle()
countdown_timer.hideturtle()
countdown_timer.penup()
countdown_timer.goto(-92, 250)
countdown_timer.write("Remaining: 59", font=style)

game_length = 15

while game_length >= 0:

    game_length = game_length-1
    countdown_timer.clear()
    countdown_timer.write("Remaining: " + str(game_length), font=style)
    turtle_movement()
    if game_length == 0:
        countdown_timer.clear()
        countdown_timer.write("Game Over!", font=style)
        break

turtle.mainloop()



def the_escapee_caught(the_player):
    return the_player.distance(the_escapee) < 10

def play_game():
    global points

    if the_escapee_caught(the_player):
        points +=1
        score.clear()
        score.write("Score:" + str(points), font=style)
        turtle_movement()


'''
to do 

the start
    the code should start after the detection of the first click

turtle symbol (that moves randomly)
    turtle symbol +
    the movement + 
    
score board(that increases when the player clicks on the turtle symbol)
    the text +
    the detection of clicking on the symbol

timer(that counts down)
    the text
    count down
    
game over
    the text "Game Over!" after the count down reaches zero
'''



