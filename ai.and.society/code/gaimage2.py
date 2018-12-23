from PIL import Image, ImageDraw
import time
import gc
from random import random, randrange, randint
import numpy as np


# 返回一个随机颜色tuple(R,G,B,A)
def random_color():
    return (randrange(256), randrange(256), randrange(256), randint(95, 115))


# 生成随机坐标的顶点tuple(x,y)
def random_xy(size):
    return randrange(size[0]), randrange(size[1])


# 生成随机数，判断是否需要变异
def mutate_or_not(rate):
    return True if rate > random() else False


# 三角形类
class Triangle:
    def __init__(self, size=(256, 256)):
        # 三角形的顶点vs[0~2]
        self.vs = tuple(random_xy(size) for i in range(3))
        # 三角形的颜色RGBA（包括透明度）
        self.color = random_color()
        # 三角形的绘制图像Image类
        self.img_t = None
        # 整个图片的尺寸
        self.size = size

    # 从parent遗传和变异三角形顶点
    def mutate_vertex(self, parent_v):
        rate = random()
        if rate < 0.08:  # 大突变概率
            return random_xy(self.size)
        elif rate < 0.3:  # 中突变概率
            return (min(max(0, parent_v[0] + randint(-5, 5)), self.size[0]),
                    min(max(0, parent_v[1] + randint(-5, 5)), self.size[1]))
        elif rate < 0.8:  # 小突变概率
            return (min(max(0, parent_v[0] + randint(-2, 2)), self.size[0]),
                    min(max(0, parent_v[1] + randint(-2, 2)), self.size[1]))
        else:  # 没有突变
            return parent_v

    # 从parent遗传和变异三角形的颜色RGBA
    def mutate_color(self, parent_c):
        rate = random()
        if rate < 0.08:  # 大突变概率
            return random_color()
        elif rate < 0.3:  # 中突变概率
            return (min(max(0, parent_c[0] + randint(-30, 30)), 255),
                    min(max(0, parent_c[1] + randint(-30, 30)), 255),
                    min(max(0, parent_c[2] + randint(-30, 30)), 255),
                    min(max(0, parent_c[3] + randint(-30, 30)), 255))
        elif rate < 0.8:  # 小突变概率
            return (min(max(0, parent_c[0] + randint(-10, 10)), 255),
                    min(max(0, parent_c[1] + randint(-10, 10)), 255),
                    min(max(0, parent_c[2] + randint(-10, 10)), 255),
                    min(max(0, parent_c[3] + randint(-10, 10)), 255))
        else:  # 没有突变
            return parent_c

    def mutate_from(self, parent):
        # 从parent遗传和变异
        self.vs = tuple(self.mutate_vertex(parent.vs[i]) for i in range(3))
        self.color = self.mutate_color(parent.color)

    def draw(self):
        self.img_t = Image.new("RGBA", self.size, (255, 255, 255, 0))
        d = ImageDraw.Draw(self.img_t)
        d.polygon(self.vs, fill=self.color)
        return self.img_t


# 三角形组成的图案
class Canvas:
    def __init__(self, size=(256, 256), num_t=256):
        self.triangles = None  # 保存三角形列表
        self.error_rate = 0  # 与原始图像相比的误差值
        self.size = size  # 图案大小
        self.num_t = num_t  # 多少个三角形构成
        self.img = None

    def random_triangles(self):
        self.triangles = tuple(Triangle(self.size) for i in range(self.num_t))

    def mutate_triangle(self, parent_triangle):
        rate = random()
        if rate < 0.08:
            t = Triangle(self.size)
            t.mutate_from(parent_triangle)
            return t
        else:
            return parent_triangle

    def mutate_from(self, father, mother):
        # 从father和mother来遗传和变异
        # 奇数编号基因来自于father，偶数编号基因来自于mother
        self.triangles = tuple(self.mutate_triangle(father.triangles[i]) if i % 2 else
                               self.mutate_triangle(mother.triangles[i])
                               for i in range(self.num_t))

    def calc_error_rate(self, target_pixels):
        # 将所有三角形合成
        self.img = Image.new("RGBA", self.size, (255, 255, 255, 0))
        for t in self.triangles:
            self.img = Image.alpha_composite(self.img, t.img_t or t.draw())
        # 计算误差值
        arrs = tuple(np.array(x) for x in self.img.split())
        for i in range(3):
            self.error_rate += np.sum(np.square(arrs[i] - target_pixels[i]))  # [0]

    def save_png(self, i):
        self.img.save("%d.png" % i)


# 1，打开目标图像
target_file = "firefox64.jpeg"
target_img = Image.open(target_file).convert("RGBA")
target_size = target_img.size
target_pixels = tuple(np.array(x) for x in target_img.split())

# 2，种群的数量，三角形的数量，迭代的代数，每几代保存图像
num_ind = 16
num_t = 128
num_gen = 300000
num_save = 10000

# 3，随机生成初代的种群
start = time.time()
population = []
for i in range(num_ind):
    c = Canvas(target_size, num_t)
    c.random_triangles()
    c.calc_error_rate(target_pixels)
    population.append(c)

for gen in range(num_gen):
    # 4，按照误差值从小到大排序
    population.sort(key=lambda x: x.error_rate)
    if gen % num_save == 0:
        population[0].save_png(gen)
        print("%08d:min error=%010d:%08d" % (gen, population[0].error_rate, int(time.time() - start)), flush=False)
    for i in range(num_ind // 2):
        # 5，从误差值小的前一半，生成新种群
        c = Canvas(target_size, num_t)
        c.mutate_from(population[i], population[randrange(num_ind // 2)])
        c.calc_error_rate(target_pixels)
        population[num_ind // 2 + i] = c
    # gc.collect()
