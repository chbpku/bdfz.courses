import pgzrun
import random

# 捡宝物的小游戏
# 宝物角色
# 玩家角色（5种表情）
# 背景：草原（1000*606像素）
# 1, 创建一系列精灵
# 名称
names = ["peach", "cherryf", "apple", "orange", "lemon", "grape", "banana",
         "egg", "donut", "taco", "pizza", "burger", "fries", "leg", "dango",
         "cake", "cookie", "ice", "candy",
         "cherry", "bouquet", "leaf4", "sunflower", "tulip", "rose",
         "tiger", "cat", "bear"]

# 保存正在下落的宝物
things = []

# 玩家、位置和得分
player = Actor("face_sweat")
player.center = 500, 580
player.score = 0

# 2, 设定窗口
WIDTH = 1000
HEIGHT = 606


# 3, 每次需要刷新窗口的时候，会自动调用draw函数
def draw():
    # 清除窗口，设置背景
    screen.clear()
    screen.blit("backimg", (0, 0))

    # 画上宝物和玩家
    for t in things:
        t.draw()
    player.draw()

    # 画上分数
    screen.draw.text("SCORE:%d" % player.score, (400, 10))


# 4，每一帧都会自动调用update函数
def update():
    # 平均每秒随机生成一个宝物加入到things列表里
    if random.randrange(60) == 0:
        # 随机生成宝物，和随机的顶部位置
        t = Actor(random.choice(names))
        t.center = random.randrange(1000), 0
        things.append(t)
    # 每个宝物下降，判断是不是碰到玩家
    for t in things:
        # 下降4个像素，可以调节速度
        t.y += 4
        # 如果调出底线了，就删除，玩家扣分
        if t.y >= 606:
            things.remove(t)
            player.score -= 4
            # 玩家换一个表情
            set_player_sad()
        # 判断是否被玩家接到了
        elif t.colliderect(player):
            # 碰到玩家了，被吃掉，玩家加分
            things.remove(t)
            player.score += 1
            # 玩家换一个表情
            set_player_happy()


# 5, 鼠标移动玩家
def on_mouse_move(pos):
    player.x = pos[0]


# 换成欢乐的表情
def set_player_happy():
    player.image = "face_cool"
    sounds.exp.play()
    # 设置定时器，1秒后恢复
    clock.schedule_unique(set_player_normal, 1.0)

# 换成悲伤表情
def set_player_sad():
    player.image="face_cry"
    sounds.blip.play()
    # 设置定时器，1秒后恢复
    clock.schedule_unique(set_player_normal, 1.0)
    
# 换回正常表情
def set_player_normal():
    player.image = "face_sweat"


pgzrun.go()
