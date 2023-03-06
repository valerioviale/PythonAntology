"""This code is using the turtle module to draw a blue hexagon.

 The first line imports all the functions from the turtle module.

The second line sets the color of the turtle to blue using the color() function.

The next six lines draw the hexagon by moving the turtle forward 100 units and turning it left 60 degrees, repeating this process six times. This creates a six-sided figure with equal sides and angles of 120 degrees.

Finally, the code uses the bye() function to close the turtle window and terminate the program. """

from turtle import *

color('blue')

forward(100)
left(60)
forward(100)
left(60)
forward(100)
left(60)
forward(100)
left(60)
forward(100)
left(60)
forward(100)
left(60)

bye()
