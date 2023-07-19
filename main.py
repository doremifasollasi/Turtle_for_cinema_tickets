# The first step in using a Turtle module is to import its classes and functions. 
# This can be done using the command import turtle or from turtle import *.
# Import the necessary classes and functions from the turtle and turtle.Screen modules.
from turtle import Turtle, Screen


# Constants for screen, title, and font sizes
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
HALL_HEADER = 150
FONT_SIZE = 20

# Number of rows and columns of seats in the hall
ROW = 5
COLUMN = 5

# Create a Turtle screen with the specified parameters
main_screen = Screen()
main_screen.bgcolor("indigo")
main_screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
main_screen.setworldcoordinates(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
main_screen.title("Cinema")

# To create a turtle object in the Turtle window, you need to create an instance of the Turtle class. 
# After creating a turtle object, you can use methods to move it, draw it, and control its properties, 
# such as feather color, feather size, movement speed, and more.
main_turtle = Turtle()
main_turtle.hideturtle()
main_turtle.speed(0)
main_turtle.penup()

