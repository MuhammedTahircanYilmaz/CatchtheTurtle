from random import randint
import turtle


def turtle_movement():
    global randx, randy
    randx = int(randint(-225, 225))
    randy = int(randint(-225, 225))
    the_escapee.goto(randx, randy)


def count_down():
    global game_over, game_length
    if game_length >= 0:
        countdown_timer.clear()
        countdown_timer.write(f"Time Left: {game_length}", font=style)
        game_length -= 1
        game_screen.ontimer(count_down, 1000)
        turtle_movement()

    else:
        game_over = True
        countdown_timer.clear()
        countdown_timer.write("Game Over", font=style)
        the_escapee.hideturtle()


def score_up(x, y):
    global points, randx, randy

    if (abs(randx - x) < 50) and (abs(randy - y) < 50) and not game_over:
        points += 1
        score_turtle.clear()
        score_turtle.write(f"Score : {points}", font=style)
        turtle_movement()


if __name__ == '__main__':
    game_over = False
    game_length = 10
    points = 0
    randx = 0
    randy = 0

    game_screen = turtle.Screen()
    game_screen.title("Catch the Turtle!")
    game_screen.bgcolor("light blue")

    the_escapee = turtle.Turtle()
    score_turtle = turtle.Turtle()
    countdown_timer = turtle.Turtle()

    # the escapee
    the_escapee.shapesize(1.5)
    the_escapee.penup()
    the_escapee.hideturtle()
    the_escapee.setposition((randint(-225, 225)), (randint(-225, 225)))
    the_escapee.shape("turtle")
    the_escapee.color("green")
    the_escapee.showturtle()
    the_escapee.speed('fastest')

    # score
    score_turtle.hideturtle()
    score_turtle.color("black")
    style = ('Courier', 20, 'italic')
    score_turtle.penup()
    score_turtle.goto(-25, 285)
    score_turtle.write(f"Score: {points}", font=style)

    # countdown
    countdown_timer.hideturtle()
    countdown_timer.penup()
    countdown_timer.goto(-92, 250)
    countdown_timer.write("Time Left: ", font=style)

    count_down()
    the_escapee.onclick(score_up)
    game_screen.update()
    turtle.mainloop()
