from turtle import *
from random import *

width = window_width()
height = window_height()
move_distance = 20

screen = Screen()
screen.setup(width=1.0, height=1.0)

speed(0)
bgcolor("#D2691E")
hideturtle()

penup()
goto(width/2,height)
color("blue")
begin_fill()
pendown()
goto(width,height)
goto(width,-height)
goto(width/2,-height)
goto(width/2,height)
end_fill()

penup()
showturtle()
goto(-width/2, 0)
shape("turtle")
color("green")

def move_up():
    setheading(90)
    forward(move_distance)
    check_goal()

def move_down():
    setheading(270)
    forward(move_distance)
    check_goal()

def move_left():
    setheading(180)
    forward(move_distance)
    check_goal()

def move_right():
    setheading(0)
    forward(move_distance)
    check_goal()

def check_goal():
    if xcor() > (width/2):
        hideturtle()
        color("White")
        write ("You Win!")
        onkey(None,"Up")
        onkey(None,"Down")
        onkey(None,"Right")
        onkey(None,"Left")

onkey(move_up,"Up")
onkey(move_down,"Down")
onkey(move_right,"Right")
onkey(move_left,"Left")

listen()
done()