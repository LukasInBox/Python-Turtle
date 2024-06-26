# Libraries and Pre-sets
import turtle # Importing Turtle Library
node = turtle.Turtle() # Giving turtle a name of "node"
node.color("lime") # Setting up a colour for "node"

# Drawing a square
node.begin_fill() # Used to start filling of the shape
node.forward(50)
node.left(90)
node.forward(50)
node.left(90)
node.forward(50)
node.left(90)
node.forward(50)
node.left(90)
node.end_fill() # Ends and fills in the empty part of the shape

# Documentation at - https://docs.python.org/3.3/library/turtle.html