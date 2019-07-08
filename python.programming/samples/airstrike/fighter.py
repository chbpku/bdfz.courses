import pygame
import random

maxs = 6


# 创建一个pygame Sprite类的子类：战斗机
class FighterClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("fighter.png")
        self.rect = self.image.get_rect()
        self.rect.center = [320, 540]  # 飞机的初始位置，320代表在初始位置在窗口中心

    def fire(self, type):  # 发射炮弹
        global shells
        shell = ShellClass(
            type + ".png", [self.rect.centerx, self.rect.centery - 20], type)
        shells.add(shell)

    def fly(self, x, y):  # 飞机在左右、上下方向移动，并且保证都不出界
        self.rect.centerx = x
        if self.rect.centerx < 20:
            self.rect.centerx = 20
        if self.rect.centerx > 620:
            self.rect.centerx = 620
        self.rect.centery = y
        if self.rect.centery < 20:
            self.rect.centery = 20
        if self.rect.centery > 620:
            self.rect.centery = 620


# 创建一个pygame Sprite类的子类：障碍物，包含三种
class ObstacleClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, type):
        pygame.sprite.Sprite.__init__(self)
        self.image_file = image_file
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.type = type
        if type == "p1":  # 障碍物P1的生命值是1000
            self.life = 1000
        elif type == "p2":
            self.life = 2000
        elif type == "p3":
            self.life = 100000000
        self.passed = False

    def update(self):  # 障碍物自上而下移动
        global speed
        self.rect.centery += speed[1]
        if self.rect.centery > 672 or self.life <= 0:  # 如果障碍物已移出屏幕
            self.kill()  # 删掉障碍物


class ShellClass(ObstacleClass):
    def __init__(self, image_file, location, type):
        ObstacleClass.__init__(self, image_file, location, type)
        self.direction = 0
        if type == "shell1":
            self.direction = 1

    def update(self):  # 炮弹自下而上移动
        global speed
        self.rect.centerx += self.direction * speed[1] * 0.8
        self.rect.centery -= speed[1]
        if self.rect.centery < -32 or self.rect.centerx < - \
                32 or self.rect.centerx > 672:  # 如果炮弹已移出屏幕
            self.kill()  # 删掉炮弹


# 创建障碍物地图，即在一个场景中，创建多个障碍物
def create_map():
    global obstacles
    locations = []
    for i in range(7):  # 每屏7个障碍物（p1和p2）
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        location = [col * 64 + 20, row * 64 + 20 - 640]  # 障碍物的位置(x,y)
        # 确保没有将同样两个障碍物放在同一位置，并且每个位置障碍物的种类是随机的
        if not (location in locations):
            locations.append(location)
            type = random.choice(["p1", "p2"])
            if type == "p1":
                img = "p1.png"
            elif type == "p2":
                img = "p2.png"
            obstacle = ObstacleClass(img, location, type)
            obstacles.add(obstacle)

    for i in range(1):  # 每屏1个障碍物（p3）
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        location = [col * 64 + 20, row * 64 + 20 - 640]  # 生成障碍物的位置
        # 确保没有将同样两个障碍物放在同一位置，并且每个位置障碍物的种类是随机的
        if not (location in locations):
            locations.append(location)
            type = random.choice(["p3"])
            if type == "p3":
                img = "p3.png"
            obstacle = ObstacleClass(img, location, type)
            obstacles.add(obstacle)


def animate():  # 重绘屏幕
    screen.fill([255, 255, 255])

    obstacles.draw(screen)
    shells.draw(screen)
    screen.blit(fighter.image, fighter.rect)  # 在屏幕上添加图像
    screen.blit(score_text, [10, 10])  # 在屏幕上添加得分文本
    pygame.display.flip()


# 初始化
pygame.init()
pygame.mixer.init()  # 初始化声音模块
bomb = pygame.mixer.Sound("BOMB.WAV")  # 创建声音对象
screen = pygame.display.set_mode([640, 640])  # 设定屏幕大小
clock = pygame.time.Clock()  # 定义系统时钟
fighter = FighterClass()  # 定义战斗机fighter
speed = [0, maxs]  # 定义障碍物下落的速度
obstacles = pygame.sprite.Group()  # 创建障碍物精灵组
shells = pygame.sprite.Group()  # 创建炮弹精灵组
map_position = 0
points = 0
create_map()  # 定义障碍物地图
font = pygame.font.Font(None, 50)  # 创建pygame的Font类对象，用来显示分数
c = 0
running = True

# 主循环
while running:
    c = c + 1
    clock.tick(60)  # 循环每秒运行60次
    maxs = 6 + (points / 600)
    if maxs < 6:
        maxs = 6
    for event in pygame.event.get():  # 检查按键事件
        if event.type == pygame.QUIT:  # 如果关闭游戏窗口，就同时退出程序
            running = False
        elif event.type == pygame.MOUSEMOTION:  # 鼠标移动
            x = event.pos[0]
            y = event.pos[1]
            fighter.fly(x, y)
        elif event.type == pygame.KEYDOWN:  # 按下键盘上的q键时，退出游戏
            if event.key == pygame.K_q:
                running = False
    if c == 8:  # 发射炮弹的频率
        fighter.fire("shell")
        c = 0
    speed = [0, maxs]
    map_position += speed[1]  # 记录地图已经往上滚动了多少
    if map_position >= 640:  # 如果整个屏幕已经滚动完，创建一个新的含有障碍物的场景
        create_map()
        map_position = 0
    # 碰撞检测
    hit = pygame.sprite.spritecollide(
        fighter, obstacles, False)  # 检测碰撞，确定碰撞保障时的图像
    if hit:
        if not hit[0].passed:  # 战斗机碰到障碍物，游戏结束
            if hit[0].type == "p1":
                running = False
            elif hit[0].type == "p2":
                running = False
            elif hit[0].type == "p3":
                running = False
            # 显示碰撞后的图像
            fighter.image = pygame.image.load("fighter.png")
            animate()
            pygame.time.delay(300)
            # 继续工作
            fighter.image = pygame.image.load("fighter.png")
            speed = [0, 6]
            hit[0].passed = True  # 已经碰到障碍物
            hit[0].kill()  # 移除障碍物
    hit = pygame.sprite.groupcollide(
        shells,
        obstacles,
        dokilla=False,
        dokillb=False)  # 碰撞检测，计算得分
    if hit:
        for shell in hit:
            for enemy in hit[shell]:
                enemy.life -= 1000
                if enemy.type == "p1":
                    points = points + 10
                    bomb.play()
                elif enemy.type == "p2":
                    points = points + 20
                    bomb.play()
                elif enemy.type == "p3":
                    bomb.play()
            if shell.type == "shell":
                shell.kill()

    obstacles.update()
    shells.update()
    score_text = font.render("Score: " + str(points),
                             1, (0, 0, 0))  # 创建分数文本，用来渲染font对象
    animate()
pygame.quit()
print("Score: " + str(points))  # 游戏结束时，显示最终得分
