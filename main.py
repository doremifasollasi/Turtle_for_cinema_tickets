## The first step in using a Turtle module is to import its classes and functions. 
# This can be done using the command import turtle or from turtle import *.
# Import the necessary classes and functions from the turtle and turtle.Screen modules.
from turtle import Turtle, Screen


## Constants for screen, title, and font sizes
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
HALL_HEADER = 150
FONT_SIZE = 20

## Number of rows and columns of seats in the hall
ROW = 5
COLUMN = 5

## Create a Turtle screen with the specified parameters
main_screen = Screen()
main_screen.bgcolor("indigo")
main_screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
main_screen.setworldcoordinates(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
main_screen.title("Cinema")

## To create a turtle object in the Turtle window, 
# you need to create an instance of the Turtle class. 
# After creating a turtle object, you can use methods to move it, draw it, and control its properties, 
# such as feather color, feather size, movement speed, and more.
main_turtle = Turtle()
main_turtle.hideturtle()
main_turtle.speed(0)
main_turtle.penup()

## Using separate objects allows us to control drawing and text output independently of each other. 
##The corresponding settings (hideturtle(), speed(), penup()) help ensure more efficient use of objects depending on their purpose.

## Create a shell object for text output
# main_turtle is a turtle object that is responsible for drawing graphic objects on the screen using the Turtle module. 
# It will be used to draw pictures, create shapes, lines, etc. In this code, it is also hidden (hideturtle()), 
# the maximum drawing speed is set (speed(0)), and the pen is raised (penup()) to the turtle did not leave a trace when moving to a new position.
main_writer = Turtle()
main_writer.hideturtle()
main_writer.speed(0)
main_writer.penup()
