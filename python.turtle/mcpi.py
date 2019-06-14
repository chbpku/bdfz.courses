import turtle, random

turtle.tracer(0)

R = 250  # 随机范围
FONT = ('SYSTEM', 20, 'normal')

label = turtle.Turtle()
label.hideturtle()
label.penup()
label.goto(-250, -R - 30)

t = label.clone()
t.goto(0, -R)
t.pendown()
t.circle(R)
for i in range(4):
    t.forward(R)
    t.left(90)
    t.forward(R)
t.penup()

m, n = 0, 0
while True:
    m += 1
    x = R * random.uniform(-1, 1)
    y = R * random.uniform(-1, 1)
    t.goto(x, y)
    if x ** 2 + y ** 2 <= R ** 2:
        n += 1
        t.dot(3, 'red')
    else:
        t.dot(3, 'black')

    # 计算pi
    pi = n / m * 4

    # 显示文字
    label.clear()
    label.write(f'pi~={pi:.6f} ({n:6}:{m:6})', font=FONT)

    # 刷新屏幕
    turtle.update()
