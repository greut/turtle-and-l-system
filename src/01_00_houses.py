import math
import turtle

SQRT2 = math.sqrt(2)

def house(length):
    """
    Draw a nice house where the base is length long and put the turtle
    back to its original position at the end.
    """
    inside = SQRT2 * length
    roof = inside / 2.

    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)

    # roof
    turtle.left(45)
    turtle.forward(roof)
    turtle.left(90)
    turtle.forward(roof)
    turtle.left(45)

    # interior
    turtle.forward(length)
    turtle.left(135)
    turtle.forward(inside)
    turtle.left(135)
    turtle.forward(length)
    turtle.left(135)
    turtle.forward(inside)

    # back into position
    turtle.left(45)
    turtle.backward(length)


turtle.shape("turtle")

house(100)
turtle.penup()
turtle.forward(120)
turtle.pendown()

house(80)

turtle.exitonclick()
