import turtle
import random


def polygon(n, size, color):
    t.color(color)
    t.begin_fill()
    for i in range(n):
        t.forward(size)
        t.right(360 / n)
    t.end_fill()


t = turtle.Turtle()
t.speed(0)
colors = ['red', 'green', 'yellow', 'blue', 'brown', 'pink']
for i in range(50):
    t.penup()
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.goto(x, y)
    t.pendown()
    n = random.randint(3, 6)
    size = random.randint(20, 50)
    color = random.choice(colors)
    polygon(n, size, color)

t.hideturtle()
turtle.done()
