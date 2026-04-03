from turtle import *

def move_and_turn(angle):
    forward(50)
    right(angle)

#octogone
for x in range(8):
    move_and_turn(45)

#carré

for x in range(4):
    move_and_turn(90)

#dodecagone

for x in range (12):
    move_and_turn(30)

done()