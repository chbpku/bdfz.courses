import turtle

t = turtle.Turtle()

t.color('red')
t.begin_fill()
for i in range(5):
    t.forward(20)
    t.left(72)
    t.forward(20)
    t.right(144)
t.end_fill()

t.penup()
t.forward(60)
t.right(30)
t.pendown()

t.color('green')
t.begin_fill()
for i in range(5):
    t.forward(30)
    t.left(72)
    t.forward(30)
    t.right(144)
t.end_fill()

t.penup()
t.forward(80)
t.left(50)
t.pendown()

t.color('blue')
t.begin_fill()
for i in range(5):
    t.forward(40)
    t.left(72)
    t.forward(40)
    t.right(144)
t.end_fill()

t.hideturtle()
turtle.done()
