import turtle


def star(size, color):
    t.color(color)
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.left(72)
        t.forward(size)
        t.right(144)
    t.end_fill()


t = turtle.Turtle()

star(20, 'red')
t.penup()
t.forward(60)
t.right(30)
t.pendown()
star(30, 'green')
t.penup()
t.forward(80)
t.left(50)
t.pendown()
star(40, 'blue')

t.hideturtle()
turtle.done()
