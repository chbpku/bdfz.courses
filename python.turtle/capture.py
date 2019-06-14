import turtle, time
from random import random

turtle.tracer(0)

N = 500  # 总数
SIZEP = 300  # 池塘范围
SIZEC = 100  # 捕捉范围
RAND_SPEED = 50  # 随机游走速度
FONT = ('SYSTEM', 20, 'bold')
inner = lambda pos: all(-SIZEC <= x <= SIZEC for x in pos)

tt = turtle.Pen()
t_dot = turtle.Pen()
t_text = turtle.Pen()
for tur in tt, t_dot, t_text:
    tur.hideturtle()
    tur.penup()

t_text.goto(-300, -300)
t_text.color('blue')

# 生成初始池塘
pool = [[-SIZEP + SIZEP * random() * 2 for _ in 'xx'] for i in range(N)]
released = [inner(x) for x in pool]
n_released = sum(released)
for x in SIZEC, SIZEP:
    tt.goto(-x, x)
    tt.pendown()
    tt.goto(-x, -x)
    tt.goto(x, -x)
    tt.goto(x, x)
    tt.goto(-x, x)
    tt.penup()
turtle.update()

welldone = False
while not welldone:
    n_catched, n_marked = 0, 0
    t_dot.clear()
    for ind, pos in enumerate(pool):
        # 随机游走
        for i in 0, 1:
            pos[i] += (random() - 0.5) * RAND_SPEED
            if pos[i] > SIZEP:
                pos[i] -= SIZEP * 2
            elif pos[i] < -SIZEP:
                pos[i] += SIZEP * 2
        # 重捕+确定颜色
        if inner(pos):
            n_catched += 1
            if released[ind]:
                n_marked += 1
                t_dot.color('red')
            else:
                t_dot.color('blue')
        else:
            t_dot.color('red' if released[ind] else 'black')
        # 绘制
        t_dot.goto(pos)
        t_dot.dot()

    # 估算
    formula = '%d * %d / %d' % (n_catched, n_released, n_marked)
    if n_marked:
        n_calc = int(eval(formula))
        if 0.95 <= abs(n_calc / N) < 1.05:
            welldone = True
    else:
        n_calc = 'Too Many'
    t_text.clear()
    t_text.write(
        'Actual: %d\nEstimated: %s = %s' % (N, n_calc, formula), font=FONT)

    turtle.update()
    time.sleep(0.05)

turtle.done()
