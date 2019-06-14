import turtle, time
from random import randrange

turtle.tracer(0)
model = turtle.Turtle()
model.hideturtle()
model.penup()

FPS = 30  # 每秒30帧刷新率
FREQ = FPS // 2  # 平均每秒生成2个苹果

# 接苹果的篮子
turtle.addshape('basket', ((-100, 0), (100, 0), (0, -25)))
basket = model.clone()
basket.shape('basket')
basket.setheading(90)
basket.ondrag(basket.goto)  # 把goto函数绑定到鼠标拖动事件上
basket.showturtle()

# 用来显示苹果的印模
mould = model.clone()
mould.color('red')
mould.shape('circle')

# 得分显示牌
board = model.clone()
board.goto(-300, -300)
board.color('blue')

apples = []
score = 0
while True:
    mould.clearstamps()
    if randrange(FREQ) == 0:
        # 生成苹果[x, y, s]加入列表，s是一次下落高度
        apples.append([randrange(-350, 350), 400, 5 + randrange(10)])

    b_x, b_y = basket.pos()
    for apple in apples:
        # 苹果下落，并用印模画出苹果
        apple[1] -= apple[2]
        mould.goto(apple[0], apple[1])
        mould.stamp()
        # 判断苹果的位置
        if abs(apple[0] - b_x) <= 100 and 0 <= apple[1] - b_y <= 25:
            # 篮子碰上了苹果，加分
            score += 10
            apples.remove(apple)
        elif apple[1] < -400:
            # 苹果掉出底线，没接到，减分
            score -= 100
            apples.remove(apple)

    board.clear()
    board.write(f'SCORE: {score}', font=('SYSTEM', 40, 'normal'))
    turtle.update()
    time.sleep(1 / FPS)
