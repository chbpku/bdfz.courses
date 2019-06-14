import turtle
from math import pi, sin, cos

R = 300  # 曲线最大距中心距离
K = 7 / 3  # 玫瑰曲线参数
LOOP = 2  # 参数范围(n个圆周)
SEP = 700  # 细分程度

rose = turtle.Pen()
rose.pencolor('red')
rose.pensize(7)
rose.speed('fastest')

for i in range(SEP * LOOP):
    theta = pi * 2 * i / SEP
    # 玫瑰曲线公式
    r = R * sin(theta * K)
    # 极坐标转换为平面直角坐标
    x, y = r * sin(theta), r * cos(theta)
    # 海龟连接曲线
    rose.goto(x, y)

rose.hideturtle()
turtle.done()
