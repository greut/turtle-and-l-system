import math
import turtle


def tree(size, branches=2, angle=90):
 
    turtle.forward(size)

    if (size > 10):
        turtle.left(angle / 2)
        alpha = angle / (branches - 1)

        for b in range(branches):
            tree(size / 2, branches, angle)
            turtle.right(alpha)
        turtle.left(alpha)
        turtle.left(angle / 2)

    turtle.penup()
    turtle.backward(size)
    turtle.pendown()


turtle.speed(0)
turtle.shape("turtle")
turtle.left(90)

tree(100, 2, 90)

turtle.exitonclick()
