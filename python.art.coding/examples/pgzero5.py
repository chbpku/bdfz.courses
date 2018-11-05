import pgzrun

# 用鼠标点击精灵
# 1，创建一个精灵
alien = Actor('alien')
alien.topright = 0, 10

# 2，设定窗口大小
WIDTH = 500
HEIGHT = alien.height + 20


# 3，每次需要刷新窗口的时候，会自动调用draw函数
def draw():
    screen.clear()
    screen.fill((128, 0, 0))
    alien.draw()


# 4，每一帧都会自动调用update函数
def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.left = 0


# 5，当鼠标点击当时候调用这个函数
# 切换外星人形象，播放音效
def on_mouse_down(pos):
    if alien.collidepoint(pos):
        sounds.eep.play()
        alien.image = 'alien_hurt'


pgzrun.go()
