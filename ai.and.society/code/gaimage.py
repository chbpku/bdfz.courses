#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw
import os
import gc
import random as r
import minpy.numpy as np


class Color(object):
    '''
    定义颜色的类，这个类包含r,g,b,a表示颜色属性
    '''

    def __init__(self):
        self.r = r.randrange(256)
        self.g = r.randrange(256)
        self.b = r.randrange(256)
        self.a = r.randint(95, 115)


def mutate_or_not(rate):
    '''
    生成随机数，判断是否需要变异
    '''
    return True if rate > r.random() else False


class Triangle(object):
    '''
    定义三角形的类
    属性：
            ax,ay,bx,by,cx,cy：表示每个三角形三个顶点的坐标
            color 			 : 表示三角形的颜色
            img_t			 : 三角形绘制成的图，用于合成图片
    方法：
            mutate_from(self, parent):      从父代三角形变异
            draw_it(self, size=(256, 256)): 绘制三角形
    '''

    max_mutate_rate = 0.08
    mid_mutate_rate = 0.3
    min_mutate_rate = 0.8

    def __init__(self, size=(255, 255)):
        self.ax = r.randint(0, size[0])
        self.ay = r.randint(0, size[1])
        self.bx = r.randint(0, size[0])
        self.by = r.randint(0, size[1])
        self.cx = r.randint(0, size[0])
        self.cy = r.randint(0, size[1])
        self.color = Color()
        self.img_t = None

    def mutate_from(self, parent):
        if mutate_or_not(self.max_mutate_rate):
            self.ax = r.randint(0, 255)
            self.ay = r.randint(0, 255)
        if mutate_or_not(self.mid_mutate_rate):
            self.ax = min(max(0, parent.ax + r.randint(-15, 15)), 255)
            self.ay = min(max(0, parent.ay + r.randint(-15, 15)), 255)
        if mutate_or_not(self.min_mutate_rate):
            self.ax = min(max(0, parent.ax + r.randint(-3, 3)), 255)
            self.ay = min(max(0, parent.ay + r.randint(-3, 3)), 255)

        if mutate_or_not(self.max_mutate_rate):
            self.bx = r.randint(0, 255)
            self.by = r.randint(0, 255)
        if mutate_or_not(self.mid_mutate_rate):
            self.bx = min(max(0, parent.bx + r.randint(-15, 15)), 255)
            self.by = min(max(0, parent.by + r.randint(-15, 15)), 255)
        if mutate_or_not(self.min_mutate_rate):
            self.bx = min(max(0, parent.bx + r.randint(-3, 3)), 255)
            self.by = min(max(0, parent.by + r.randint(-3, 3)), 255)

        if mutate_or_not(self.max_mutate_rate):
            self.cx = r.randint(0, 255)
            self.cy = r.randint(0, 255)
        if mutate_or_not(self.mid_mutate_rate):
            self.cx = min(max(0, parent.cx + r.randint(-15, 15)), 255)
            self.cy = min(max(0, parent.cy + r.randint(-15, 15)), 255)
        if mutate_or_not(self.min_mutate_rate):
            self.cx = min(max(0, parent.cx + r.randint(-3, 3)), 255)
            self.cy = min(max(0, parent.cy + r.randint(-3, 3)), 255)
        # color
        if mutate_or_not(self.max_mutate_rate):
            self.color.r = r.randint(0, 255)
        if mutate_or_not(self.mid_mutate_rate):
            self.color.r = min(max(0, parent.color.r + r.randint(-30, 30)), 255)
        if mutate_or_not(self.min_mutate_rate):
            self.color.r = min(max(0, parent.color.r + r.randint(-10, 10)), 255)

        if mutate_or_not(self.max_mutate_rate):
            self.color.g = r.randint(0, 255)
        if mutate_or_not(self.mid_mutate_rate):
            self.color.g = min(max(0, parent.color.g + r.randint(-30, 30)), 255)
        if mutate_or_not(self.min_mutate_rate):
            self.color.g = min(max(0, parent.color.g + r.randint(-10, 10)), 255)

        if mutate_or_not(self.max_mutate_rate):
            self.color.b = r.randint(0, 255)
        if mutate_or_not(self.mid_mutate_rate):
            self.color.b = min(max(0, parent.color.b + r.randint(-30, 30)), 255)
        if mutate_or_not(self.min_mutate_rate):
            self.color.b = min(max(0, parent.color.b + r.randint(-10, 10)), 255)
        # alpha
        if mutate_or_not(self.mid_mutate_rate):
            self.color.a = r.randint(95, 115)
        # if mutate_or_not(self.mid_mutate_rate):
        #     self.color.a = min(max(0, parent.color.a + r.randint(-30, 30)), 255)
        # if mutate_or_not(self.min_mutate_rate):
        #     self.color.a = min(max(0, parent.color.a + r.randint(-10, 10)), 255)

    def draw_it(self, size=(256, 256)):
        self.img_t = Image.new('RGBA', size)
        draw = ImageDraw.Draw(self.img_t)
        draw.polygon([(self.ax, self.ay),
                      (self.bx, self.by),
                      (self.cx, self.cy)],
                     fill=(self.color.r, self.color.g, self.color.b, self.color.a))
        return self.img_t


class Canvas(object):
    '''
    定义每一张图片的类
    属性：
            mutate_rate	 : 变异概率
            size		 : 图片大小
            target_pixels: 目标图片像素值
    方法：
            add_triangles(self, num=1)      : 在图片类中生成num个三角形
            mutate_from_parent(self, parent): 从父代图片对象进行变异
            calc_match_rate(self)			: 计算环境适应度
            draw_it(self, i)				: 保存图片
    '''

    mutate_rate = 0.01
    size = (256, 256)
    target_pixels = []

    def __init__(self):
        self.triangles = []
        self.match_rate = 0
        self.img = None

    def add_triangles(self, num=1):
        for i in range(0, num):
            triangle = Triangle()
            self.triangles.append(triangle)

    def mutate_from_parent(self, parent):
        flag = False
        for triangle in parent.triangles:
            t = triangle
            if mutate_or_not(self.mutate_rate):
                flag = True
                a = Triangle()
                a.mutate_from(t)
                self.triangles.append(a)
                continue
            self.triangles.append(t)
        if not flag:
            self.triangles.pop()
            t = parent.triangles[r.randint(0, len(parent.triangles) - 1)]
            a = Triangle()
            a.mutate_from(t)
            self.triangles.append(a)

    def calc_match_rate(self):
        if self.match_rate > 0:
            return self.match_rate
        self.match_rate = 0
        self.img = Image.new('RGBA', self.size)
        draw = ImageDraw.Draw(self.img)
        draw.polygon([(0, 0), (0, 255), (255, 255), (255, 0)], fill=(255, 255, 255, 255))
        for triangle in self.triangles:
            self.img = Image.alpha_composite(self.img, triangle.img_t or triangle.draw_it(self.size))
            # 与下方代码功能相同，此版本便于理解但效率低
        # pixels = [self.img.getpixel((x, y)) for x in range(0, self.size[0], 2) for y in range(0, self.size[1], 2)]
        # for i in range(0, min(len(pixels), len(self.target_pixels))):
        #     delta_red   = pixels[i][0] - self.target_pixels[i][0]
        #     delta_green = pixels[i][1] - self.target_pixels[i][1]
        #     delta_blue  = pixels[i][2] - self.target_pixels[i][2]
        #     self.match_rate += delta_red   * delta_red   + \
        #                        delta_green * delta_green + \
        #                        delta_blue  * delta_blue
        arrs = [np.array(x) for x in list(self.img.split())]  # 分解为RGBA四通道
        for i in range(3):  # 对RGB通道三个矩阵分别与目标图片相应通道作差取平方加和评估相似度
            self.match_rate += np.sum(np.square(arrs[i] - self.target_pixels[i]))[0]

    def draw_it(self, i):
        # self.img.save(os.path.join(PATH, "%s_%d_%d_%d.png" % (PREFIX, len(self.triangles), i, self.match_rate)))
        self.img.save(os.path.join(PATH, "a%04d.png" % (i)))


def main():
    global LOOP, PREFIX, PATH, TARGET, TRIANGLE_NUM
    # 声明全局变量
    img = Image.open(TARGET).resize((256, 256)).convert('RGBA')
    size = (256, 256)
    Canvas.target_pixels = [np.array(x) for x in list(img.split())]
    # 生成一系列的图片作为父本，选择其中最好的一个进行遗传
    parentList = []
    for i in range(20):
        # print('正在生成第%d个初代个体' % (i))
        parentList.append(Canvas())
        parentList[i].add_triangles(TRIANGLE_NUM)
        parentList[i].calc_match_rate()
    parent = sorted(parentList, key=lambda x: x.match_rate)[0]
    del parentList
    gc.collect()
    # 进入遗传算法的循环
    i = 0
    while i < 30000:
        childList = []
        # 每一代从父代中变异出10个个体
        for j in range(10):
            childList.append(Canvas())
            childList[j].mutate_from_parent(parent)
            childList[j].calc_match_rate()
        child = sorted(childList, key=lambda x: x.match_rate)[0]
        # 选择其中适应度最好的一个个体
        del childList
        gc.collect()
        parent.calc_match_rate()
        print('%10d parent rate %11d \t child1 rate %11d' % (i, parent.match_rate, child.match_rate))
        parent = parent if parent.match_rate < child.match_rate else child
        # 如果子代比父代更适应环境，那么子代成为新的父代
        # 否则保持原样
        child = None
        if i % LOOP == 0:
            # 每隔LOOP代保存一次图片
            parent.draw_it(i)
            # print(parent.match_rate)
        i += 1


'''
定义全局变量，获取待处理的图片名
'''
#NAME = input('请输入原图片文件名：')
NAME = "firefox.jpeg"
LOOP = 100
PREFIX = NAME.split('/')[-1].split('.')[0]  # 取文件名
PATH = os.path.abspath('.')  # 取当前路径
PATH = os.path.join(PATH, 'results')
TARGET = NAME  # 源图片文件名
TRIANGLE_NUM = 256  # 三角形个数

if __name__ == '__main__':
    # print('开始进行遗传算法')
    main()
