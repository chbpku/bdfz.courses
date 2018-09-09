import turtle

t = turtle.Turtle()
t.color('red')


def star():
    t.begin_fill()
    for i in range(5):
        t.fd(20)
        t.lt(72)
        t.fd(20)
        t.rt(144)
    t.end_fill()


for i in range(3):
    star()
    t.pu()
    t.fd(80)
    t.pd()
t.hideturtle()
turtle.done()
