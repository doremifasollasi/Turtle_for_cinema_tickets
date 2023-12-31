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

## To create a turtle object in the Turtle window, you need to create an instance of the Turtle class. 
# After creating a turtle object, you can use methods to move it, draw it, and control its properties, 
# such as feather color, feather size, movement speed, and more.

## Create a turtle object for drawing.
# main_turtle is a turtle object that is responsible for drawing graphic objects on the screen using the Turtle module. 
# It will be used to draw pictures, create shapes, lines, etc. In this code, it is also hidden (hideturtle()), 
# the maximum drawing speed is set (speed(0)), and the pen is raised (penup()) to the turtle did not leave a trace when moving to a new position.
main_turtle = Turtle()
main_turtle.hideturtle()
main_turtle.speed(0)
main_turtle.penup()

# Using separate objects allows us to control drawing and text output independently of each other. 
# The corresponding settings (hideturtle(), speed(), penup()) help ensure more efficient use of objects depending on their purpose.

## Create a turtle object for text output.
# main_writer is another turtle object, but with a different purpose. 
# It is used to display text on the screen. Normally, turtles are used to draw graphic objects, 
# but in this case, using main_writer, we can add text elements to our drawing. 
# It also hides the turtle (hideturtle()), sets the maximum drawing speed (speed(0)), 
# and raises the pen (penup()) so that the turtle doesn't leave a trail when it moves to a new position.
main_writer = Turtle()
main_writer.hideturtle()
main_writer.speed(0)
main_writer.penup()

# Calculate the dimensions of the places and the radius of each place
cell_width = SCREEN_WIDTH / COLUMN
cell_height = (SCREEN_HEIGHT - HALL_HEADER) / ROW

seat_radius = (cell_height * 0.8) / 2

# Initialize the initial coordinates of the places
x = cell_width / 2
y = (cell_height / 2) - seat_radius

# Create a dictionary to save the state of places
seats = {}

# Fill the dictionary with initial values (all spaces are free)
for r in range(ROW):
    for c in range(COLUMN):
        seats[(x, y)] = False
        x += cell_width
    x = cell_width / 2
    y += cell_height

# Function for displaying information about free and reserved seats
def write_free_seats():
    main_screen.tracer(False)
    main_writer.clear()
    main_writer.setposition(10, SCREEN_HEIGHT - (FONT_SIZE * 2))
    main_writer.pendown()
    free_seats = len(seats.values()) - sum(seats.values())
    solid_seats = sum(seats.values())
    main_writer.write(f"Free: {free_seats}  Solid: {solid_seats}", font=("TimesNewRoman", FONT_SIZE, "bold"))
    main_writer.penup()
    main_screen.tracer(True)

# Function for drawing a place
def draw_seat(x, y, color="steel blue"):
    main_turtle.setposition(x, y)
    main_turtle.pendown()
    main_turtle.begin_fill()
    main_turtle.circle(seat_radius)
    main_turtle.fillcolor(color)
    main_turtle.end_fill()
    main_turtle.penup()

# Function for determining the seat by cursor coordinates
def get_seat(x, y):
    for _x, _y in seats:
        distance = ((x - _x)**2 + (y - (_y + seat_radius))**2)**0.5
        if distance <= seat_radius:
            return _x, _y

# A function for booking a seat with a left mouse button click
def book_seat(x, y):
    seat_coord = get_seat(x, y)
    if seat_coord:
        seats[seat_coord] = not seats[seat_coord]  # Change the state of the place when pressed
        color = "tomato" if seats[seat_coord] else "steel blue"
        draw_seat(*seat_coord, color=color)
        write_free_seats()

# The function of canceling seat reservations with the right mouse button
def unbook_seat(x, y):
    seat_coord = get_seat(x, y)
    if seat_coord:
        if seats[seat_coord]:
            seats[seat_coord] = False  # Return the place to a free state
            color = "steel blue"  # Return the color of the place to the original (blue)
            draw_seat(*seat_coord, color=color)
            write_free_seats()

## This is where the final part of the code begins, where we draw the initial locations on the screen, 
# add mouse click handlers, and start the main program loop with main_screen.mainloop().

# These lines disable (False) and enable (True) the drawing animation. When the animation is off, 
# we see instant drawing of all locations, with no delays.
main_screen.tracer(False)

# This is a loop that draws all the seats stored in the seats dictionary. 
# We go through all seat coordinates and draw each seat using the draw_seat(*seat) function. 
# We select each seat coordinate value and pass it as arguments to the draw_seat function. 
# The draw_seat function draws a circle on the seat with the given color.
for seat in seats:
    draw_seat(*seat)
main_screen.tracer(True)

# This function displays the number of free seats and the number of sold seats. 
# We call this function in the initial stage to display the number of free seats at the start of the program.
write_free_seats()

# This line adds a LMB (left mouse button) click handler to the main_screen window. 
# The book_seat function will be called with each LMB click on the screen.
main_screen.onclick(book_seat)

# This line adds a right click handler to the main_screen window. 
# The unbook_seat function will be called on each PCM click on the screen.
main_screen.onscreenclick(unbook_seat, btn=3)  

# This command starts the program's main loop, which waits for and processes events. 
# When we click on a seat with the left or right mouse button, 
# the corresponding book_seat or unbook_seat functions are called, 
# changing the state of the seat and updating the screen display accordingly.
main_screen.mainloop()
