import pgzrun

# 绘制一个精灵

# 1，创建一个精灵
alien = Actor('alien')
alien.pos = 100, 56

# 2，设定窗口大小
WIDTH = 500
HEIGHT = alien.height + 20


# 3，每次需要刷新窗口的时候，会自动调用draw函数
def draw():
    screen.clear()
    screen.fill((128,0,0))
    alien.draw()


pgzrun.go()
