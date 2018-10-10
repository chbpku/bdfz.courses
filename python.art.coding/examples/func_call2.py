import turtle
import random
import math


def polygon(n, size, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(n):
        t.forward(size)
        t.right(360 / n)
    t.end_fill()


def star(size, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.left(72)
        t.forward(size)
        t.right(144)
    t.end_fill()


def flower(size):
    for i in range(5):
        t.forward(2 * size * (1 + math.sin(18 * math.pi / 180)))
        t.right(36)
        polygon(5, size, 'gold')
        t.right(108)
    star(size, 'purple')


t = turtle.Turtle()
t.speed(0)
t.pencolor('white')
for i in range(20):
    t.penup()
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.goto(x, y)
    t.pendown()
    head = random.randint(1, 9)
    t.setheading(head * 40)
    size = random.randint(10, 25)
    flower(size)
t.hideturtle()
turtle.done()
