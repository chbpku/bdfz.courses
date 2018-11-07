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
pass

# 2, 设定窗口1000,606
pass


# 3, 每次需要刷新窗口的时候，会自动调用draw函数
def draw():
    # 清除窗口，设置背景
    pass

    # 画上宝物和玩家
    pass

    # 画上分数
    pass


# 4，每一帧都会自动调用update函数
def update():
    # 平均每秒随机生成一个宝物加入到things列表里
    if random.randrange(60) == 0:
        # 随机生成宝物，和随机的顶部位置
        pass
    # 每个宝物下降，判断是不是碰到玩家
    for t in things:
        # 下降4个像素，可以调节速度
        pass
        # 如果调出底线了，就删除，玩家扣分
        if t.y:
            pass
        # 判断是否被玩家接到了
        elif t.colliderect(player):
            # 碰到玩家了，被吃掉，玩家加分
            pass
            # 玩家换一个表情
            set_player_happy()


# 5, 鼠标移动玩家
def on_mouse_move(pos):
    pass


# 换成欢乐的表情
def set_player_happy():
    pass
    # 设置定时器，1秒后恢复
    pass


# 换成悲伤表情
def set_player_sad():
    pass
    # 设置定时器，1秒后恢复
    pass


# 换回正常表情
def set_player_normal():
    pass


pgzrun.go()
