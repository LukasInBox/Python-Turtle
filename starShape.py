# Libraries and Pre-sets
import turtle # Importing Turtle Library
node = turtle.Turtle() # Giving turtle a name of "node"
node.color("red") # Setting up a colour for "node"
node.speed(10) # Change the speed of node movement

# Loop created for 100 times, which will re-draw the shape of a star by having 2 movements being repeated
for i in range(100):
    node.forward(200)
    node.left(168.5)

# Documentation at - https://docs.python.org/3.3/library/turtle.html