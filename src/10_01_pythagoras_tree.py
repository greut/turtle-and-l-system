import math
import turtle


def pythagoras_tree(size, n):
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)

    turtle.end_fill()
    if n > 0:
        roof = .5 * math.sqrt(2) * size

        turtle.left(90)
        turtle.forward(size)
        turtle.right(45)

        pythagoras_tree(roof, n - 1)

        turtle.forward(roof)
        turtle.right(90)

        pythagoras_tree(roof, n - 1)

        turtle.left(90)
        turtle.backward(roof)
        turtle.left(45)
        turtle.backward(size)
        turtle.right(90)

turtle.speed(0)
turtle.shape("turtle")

turtle.goto(0, -200)
pythagoras_tree(100, 8)

turtle.exitonclick()
