import turtle

turtle.tracer(0)  # 取消动画加快绘图速度
turtle.bgcolor('sky blue')

R = 500  # 雪花边长
DEPTH = 5  # 雪花层数


# 递归函数绘制Koch分形曲线
def koch(length, depth):
    if depth <= 0:
        snow.forward(length)
        return
    for dr in (60, -120, 60, 0):
        koch(length / 3, depth - 1)
        snow.left(dr)


# 雪花海龟初始化和定位
snow = turtle.Pen()
snow.penup()
snow.goto(R / (3 ** 0.5), 0)
snow.right(150)
snow.pendown()
snow.fillcolor('snow')
snow.begin_fill()
# 三段Koch曲线连接为雪花
for i in range(3):
    koch(R, DEPTH)
    snow.right(120)
snow.end_fill()
snow.hideturtle()

turtle.update()  # 与tracer配合使用
turtle.done()
