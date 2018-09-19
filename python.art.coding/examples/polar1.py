# Archimedean spiral
# 阿基米德螺线
# r=a+b*theta

import turtle
import cmath

t = turtle.Turtle()
a, b = 0, 5
for angle in range(0, 3600, 5):
    theta = angle / 360 * 2 * cmath.pi
    r = a + b * theta
    c = cmath.rect(r, theta)
    t.goto(c.real, c.imag)
t.hideturtle()
turtle.done()
