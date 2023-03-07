from turtle import *
import time
width(5)

left(180)
color("blue")
# Start of for loop.
for i in range(40): # Code below is repeated 40 times
    # Code to be repeated 
    forward(30) # Indentation indcates code is inside the loop
    left(11.25) # Still inside the for loop

right(180)
color("red")
# Start of for loop.
for i in range(40): # Code below is repeated 40 times
    # Code to be repeated 
    forward(30) # Indentation indcates code is inside the loop
    left(11.25) # Still inside the for loop

left(180)
color("green")
# Start of for loop.
for i in range(40): # Code below is repeated 40 times
    # Code to be repeated 
    forward(30) # Indentation indcates code is inside the loop
    left(11.25) # Still inside the for loop

left(180)
color("fuchsia")
# Start of for loop.
for i in range(40): # Code below is repeated 40 times
    # Code to be repeated 
    forward(30) # Indentation indcates code is inside the loop
    left(11.25) # Still inside the for loop

# No more indentation! Marks the end of the for-loop.
time.sleep(5)
hideturtle()
bye()
