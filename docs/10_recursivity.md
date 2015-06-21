---
title: Recursivity
---

Recursion is a great tool. Try searching for it in Google. _Did you mean?_

In the programming world, it's basically a function that call herself. It's
usually composed of branches: one that stops, the stopping criterion, and one
that continues.

## Recursive multiply operation

For example, we can define the multiply operation by a suite of additions.

```python
def multiplication(a, b):
    """Multiply a by b."""
    if (b <= 1):
        return a
    else:
        return a + multiplication(a, b - 1)
```

Try it, it works until you give a very big number for `b`. The reason is that
Python has a limit for the call stack. Every time we call a function, the
computer has to save the current context, give the function the required
arguments and then jump there. Once a function is done, it jumps back to the
previously saved context. Unfortunately, this has a cost, small though.

## Recursive tree

Let's go back to our little turtle. We will ask it to draw a tree. The very
basic tree is a leaf. A bigger one can be two leaves and one trunk. Then
4 leaves, 2 branches and 1 trunk. Etc. Do you see the pattern?

```
def tree(size, branches=2, angle=90):
    """
    Build a tree where the trunk is of length size and then branches are
    divided by two until it reaches leaves of length 5.

    branches: how many branches are made
    angle: the angle between the first and the last branch
    """


tree(100)
```

Since it can be slow, you can speed up or down your turtle using the `.speed()`
command. `0` is the fastest one.

```python
turtle.speed(0)
```

## Pythagoras tree

We can reuse our house drawing method to build the Pythagoras tree. It starts
by a square and then puts two other square on top of it, just like a roof. As
we saw previously the size of the roof squares has a factor of `.5 * sqrt(2)`.

```python

def pythagoras_tree(size, n):
    """
    Draw a pythagora tree of depth n.
    """
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()

    # todo
```

It draws a nice tree.
