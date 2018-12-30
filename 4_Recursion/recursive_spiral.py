"""
Use the turtle module to draw a spiral recursively.
"""


import turtle


my_turtle = turtle.Turtle()
window = turtle.Screen()

def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - 5)

draw_spiral(my_turtle, 100)
window.exitonclick()
