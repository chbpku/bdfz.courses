import turtle


def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def golden_spiral(n):
    if n > 2:
        t.circle(fibonacci(n), 90)
        golden_spiral(n - 1)


t = turtle.Turtle()

golden_spiral(12)

t.hideturtle()
turtle.done()
