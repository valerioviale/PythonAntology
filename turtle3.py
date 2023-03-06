#This code is using the turtle module to draw a shape. 
#The shape is a square with progressively smaller squares inside of it. 
#The code starts by importing all functions from the turtle module, 
#and then sets the turtle to face left and move 240 units forward. 
#It then turns left and moves forward 240 units again, repeating this pattern 
#three more times to create a square. The turtle then moves forward 220 units, turns left, 
#and continues to draw smaller squares until it reaches the center. 
#The turtle then moves to the right, turns left, and draws the same pattern of squares 
#in the opposite direction. So at the end we have two squares.
#The code then waits for 40 seconds using the time.sleep() function 
#before closing the window and terminating the program using the bye() function.

from turtle import *
import time
left(360)

forward(240)
left(90)
forward(240)
left(90)
forward(240)
left(90)
forward(220)
left(90)
forward(220)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(180)
left(90)
forward(180)
left(90)
forward(160)
left(90)
forward(160)
left(90)
forward(140)
left(90)
forward(140)
left(90)
forward(120)
left(90)
forward(120)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(80)
left(90)
forward(80)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)

right(225)
forward(200)

left(135)
forward(260)


forward(240)
left(90)
forward(240)
left(90)
forward(240)
left(90)
forward(220)
left(90)
forward(220)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(180)
left(90)
forward(180)
left(90)
forward(160)
left(90)
forward(160)
left(90)
forward(140)
left(90)
forward(140)
left(90)
forward(120)
left(90)
forward(120)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(80)
left(90)
forward(80)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)

right(225)
forward(200)

time.sleep(40)

bye()