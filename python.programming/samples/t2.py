# 1. 导入海龟模块
import turtle

# 2. 生成一只海龟，做一些设定
t = turtle.Turtle()
t.pencolor("blue")
t.pensize(3)
t.fillcolor("yellow")

# 3. 用海龟作图
t.lt(90)
t.fd(100)
t.rt(90)
t.begin_fill()
t.fd(50)
t.left(120)
t.fd(100)
t.left(120)
t.fd(100)
t.left(120)
t.fd(50)
t.end_fill()

# 4. 结束作图
t.hideturtle()
turtle.done()
