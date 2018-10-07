import turtle

t = turtle.Turtle()
t.pencolor('brown')
t.pensize(3)
for i in range(6):
    t.forward(100)
    t.left(60)

t.hideturtle()
turtle.done()
