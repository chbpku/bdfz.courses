import pgzrun

# 绘制窗口背景为暗红色

# 窗口的宽和高设置
WIDTH = 300
HEIGHT = 300


# 每次需要刷新窗口的时候，会自动调用draw函数
def draw():
    screen.fill((128, 0, 0))


pgzrun.go()
