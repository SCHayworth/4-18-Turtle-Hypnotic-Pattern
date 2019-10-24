# Program 4-18 Turtle: Hypnotic Pattern
# Shaun Hayworth
# CIS 2
# 10-24-2019
# Original source code and revision history can be found at https://github.com/SCHayworth/4-18-Turtle-Hypnotic-Pattern

# Draws a rectangular spiral pattern using the turtle graphics library

# Import the turtle graphics library
import turtle

# Initialize ITERATIONS constant at 30
# Sets the mumber of times the loop should execute.
ITERATIONS = 30

# Set the length of the first line to 5 pixels
line_length = 5

# Set the initial direction of the turtle to up
turtle.left(90)

# Draw the pattern using a loop
for x in range(ITERATIONS):
    turtle.forward(line_length)     # Draws a line equal to the line_length value
    turtle.left(90)                 # Rotates the turtle left 90 degrees
    line_length +=5                 # Adds 5 pixels to line_length

# Keeps the turtle display window open if program is not run in IDLE
turtle.done()
