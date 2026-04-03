from turtle import *

diameter = 40

pop_diameter = 100

def draw_ballon():
    color("red")
    dot(diameter)

def inflate_ballon():
    global diameter
    diameter = diameter + 10
    draw_ballon()

    if diameter >= pop_diameter:
        clear()
        diameter = 40
        write("POP!") 

draw_ballon()
onkey(inflate_ballon,"Up")
listen()

done()