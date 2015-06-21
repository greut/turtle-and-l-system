---
title: Meet the turtle
---

Let's introduce the infamous turtle.

```python
>>> import turtle
>>> turtle.shape("turtle")
```

This turtle is kind special. She has a pen on a belly and will draw while moving
around.

## Home sweet home

To first start will be to draw a little house. Do you remember how to
do this using eight lines without releasing the pen?

```python
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.left(45)
```

We've drawn the floor, on wall and have to the roof now. As our wall are `100`
long, the roof will be, using the [Pythagorean
theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem): square root of `2`
times `50`. In Python, we need the additional `math` library to compute `sqrt`.

```python
>>> import math
>>> math.sqrt(2)
1.4142135623730951
```

Great, let's continue.

```python
>>> turtle.forward(math.sqrt(2) * 50)
>>> turtle.left(90)
>>> turtle.forward(math.sqrt(2) * 50)
>>> turtle.left(45)
```

Great, let's finish the interior now.

```python
>>> turtle.forward(100)
>>> turtle.left(135)
>>> turtle.forward(math.sqrt(2) * 100)
>>> turtle.left(135)
>>> turtle.forward(100)
>>> turtle.left(135)
>>> turtle.forward(math.sqrt(2) * 100)
```

Amazing! To finish it, let's bring back the turtle to it's original position.

```python
>>> turtle.left(45)
>>> turtle.backward(100) # or turtle.forward(-100)
```

We can close it using:

```python
>>> turtle.bye()
```

Congratulations! You've built your first house using the turtle powers.

## More houses

Drawing one house is great. What if we wanted to draw a little street instead?
Many houses with different sizes next to each other. We have to create a
special function for that and maybe put our code in a file. So it's easier to
maintain.

```python
import turtle
turtle.shape("turtle")

# here goes your code

turtle.exitonclick()
```

### An external file via IDLE

From IDLE, do _File > New File_ and from the file, you can run it via _Run > Run
Module_ or simply _F5_.

### A first function

Let's create the `houses.py` file with the following skeleton. Your goal is to
fill this file in.


```python
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

    # TODO

turtle.shape("turtle")

house(100)

turtle.exitonclick()
```

### Many houses

```python
house(100)

turtle.penup()
turtle.forward(120)
turtle.pendown()

house(80)
```
