import turtle, time

turtle.tracer(0)

FPS = 60  # 每秒60帧
GROUND_Y = -300  # 地面Y坐标
WALL_X = 300  # 右墙X坐标
G = -0.03  # 模拟重力加速度
R = 15  # 球半径
DRAG = 0.9956  # 模拟空气阻力

ball = turtle.Turtle('circle')
ball.shapesize(R / 10)
# 绘制地面和墙
ball.pencolor('blue')
ball.penup()
ball.goto(-500, GROUND_Y)
ball.pendown()
ball.goto(WALL_X, GROUND_Y)
ball.goto(WALL_X, 500)

# 初始化小球的位置和速度
pos_x, pos_y = [-300, -300]  # 小球初始坐标
v_x, v_y = [5, 7.8]  # 初始速度XY

ball.penup()
ball.goto(pos_x, pos_y)
ball.pendown()

while True:
    v_y += G  # 模拟重力加速度
    if pos_x + R > WALL_X and v_x > 0:  # 撞墙
        v_x *= -1
    if pos_y - R < GROUND_Y and v_y < 0:  # 撞地面
        v_y *= -1
    # 模拟运动，修改小球坐标
    pos_x, pos_y = pos_x + v_x, pos_y + v_y
    # 模拟阻力，修改速度
    v_x, v_y = v_x * DRAG, v_y * DRAG
    # 绘制运动轨迹
    ball.goto(pos_x, pos_y)
    turtle.update()
    time.sleep(1 / FPS)
