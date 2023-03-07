from turtle import *
import time
width(5)

left(180)
color("blue")
# Start of for loop.
for i in range(128): # Code below is repeated 5 times
    # Code to be repeated 
    forward(7) # Indentation indcates code is inside the loop
    left(3.14) # Still inside the for loop

# No more indentation! Marks the end of the for-loop.
time.sleep(5)
hideturtle()
bye()
