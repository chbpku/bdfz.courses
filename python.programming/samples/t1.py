# 1. 导入海龟模块
import turtle

# 2. 生成一只海龟，做一些设定
t = turtle.Turtle()
t.pencolor("blue")
t.pensize(3)

# 3. 用海龟作图
t.forward(100)
t.right(60)
t.pensize(5)
t.backward(150)
t.left(90)
t.color("brown")
t.forward(150)

# 4. 结束作图
t.hideturtle()
turtle.done()
