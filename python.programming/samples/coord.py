# 1. 导入海龟模块
import turtle

# 2. 生成一只海龟，做一些设定
t = turtle.Turtle()
# 设定坐标系：左下角x,y；右上角x,y
turtle.setworldcoordinates(-200, -200, 200, 200)

# 3. 用海龟作图
t.penup()
t.goto(-180, 0)
t.pendown()
t.goto(180, 0)
t.penup()
t.goto(0, -180)
t.pendown()
t.goto(0, 180)
t.goto(0, 0)
t.write("y=0.008*x^2-150", font=("consolas", 20, "normal"))
t.pencolor("blue")
t.pensize(3)
for x in range(-180, 181, 10):
    y = 0.008 * x * x - 150
    t.goto(x, y)

# 4. 结束作图
t.hideturtle()
turtle.done()
