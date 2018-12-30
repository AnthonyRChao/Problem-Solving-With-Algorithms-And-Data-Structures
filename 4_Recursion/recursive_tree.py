"""
Use the turtle module to draw a tree recursively.
"""


import turtle
from random import randrange


def tree(branch_len, thickness, t):
    if branch_len > 5:
        branch_angle = randrange(15, 45)
        branch_decrement = randrange(10,20)
        t.pensize(thickness)
        t.forward(branch_len)
        t.right(branch_angle)
        tree(branch_len - branch_decrement, thickness - 2, t)
        t.left(branch_angle * 2)
        tree(branch_len - branch_decrement, thickness - 2, t)
        t.right(branch_angle)
        t.backward(branch_len)


def main():
    t = turtle.Turtle()
    window = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    tree(75, 10, t)
    window.exitonclick()


main()
