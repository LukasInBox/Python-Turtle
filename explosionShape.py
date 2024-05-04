# Libraries and Pre-sets
import turtle # Importing Turtle Library
import math # Importing Math Library
node = turtle.Turtle() # Giving turtle a name of "node"
node.color("red") # Setting up a colour for "node"
node.speed(10) # Change the speed of node movement

# Loop created for 100 times
node.begin_fill()
for i in range(100):
    node.forward(math.sqrt(i)*10) # Move the 'node' forward by a distance calculated as 10 times the square root of 'i'.
    node.left(170)
node.end_fill()