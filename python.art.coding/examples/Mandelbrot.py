__doc__='''曼德勃罗集显示程序

根据坐标变换及迭代公式逐像素计算收敛性并显示为平滑彩色
支持鼠标左右键控制缩放
'''

from tkinter import Tk, Canvas
from PIL import Image, ImageTk, ImageDraw
from math import log2
from colorsys import hls_to_rgb

# 设置初始边界、显示画布宽高
X1, X2, Y1, Y2 = -2, 1, -1.5, 1.5  # 初始显示范围
WIDTH, HEIGHT = 300, 300  # 窗口宽高
MAX_ITER = 100  # 最大迭代次数


class Mandelbrot:
    '''封装迭代算法及相应着色方法'''

    @staticmethod
    def get_color(x, y):
        a, b = 0, 0
        for i in range(MAX_ITER):
            # Mandelbrot集迭代公式
            a, b = a * a - b * b + x, 2 * a * b + y

            # 若模大于2则发散
            l = a * a + b * b
            if l > 4:  # sqrt(l)>2
                return Mandelbrot.color_renderer(i + 1, l)

        # 迭代收敛
        return (0, 0, 0)

    @staticmethod
    def color_renderer(iter, l2):
        # 迭代数量连续化公式
        iter += 1 - log2(log2(l2) / 2)

        # 映射RGB值
        grad = iter / MAX_ITER
        r, g, b = hls_to_rgb((2 + grad) / 3, grad, 1)
        return int(255 * r), int(255 * g), int(255 * b)


class App(Tk):
    '''显示窗口
    支持左键放大、右键重置缩放'''

    # 初始化窗口
    def __init__(self):
        '''初始化函数'''
        # 创建窗口
        super().__init__()
        self.title('曼德勃罗集')
        self['highlightthickness'] = 0
        self.geometry('%dx%d' % (WIDTH, HEIGHT))
        self.resizable(0, 0)

        # 初始XY边界
        self.xmin, self.xmax, self.ymin, self.ymax = X1, X2, Y1, Y2

        # 创建画布
        self.cv = Canvas(self, width=WIDTH, height=HEIGHT)
        self.cv.pack()

        # 绑定左右键事件
        self.accept_input = True
        self.cv.bind('<Button-1>', self.scale_up)
        self.cv.bind('<Button-3>', self.scale_reset)

        # 渲染初始图像并记录
        self.update()
        self.scale = 1
        self.render_image()
        self.img_cover = self.img_mset

    # 点阵->坐标映射
    def get_x(self, i):
        '''线性映射横坐标'''
        return self.xmin + (self.xmax - self.xmin) * i / WIDTH

    def get_y(self, j):
        '''线性映射纵坐标'''
        return self.ymin + (self.ymax - self.ymin) * j / HEIGHT

    # 渲染图像
    def render_image(self):
        '''根据当前XY边界渲染图片'''
        # 阻止无效输入
        self.accept_input = False
        self.title('曼德勃罗集 (计算中)')

        # 创建空白图像
        self.img_mset = Image.new('RGB', (WIDTH, HEIGHT))

        # 逐像素计算对应颜色
        for i in range(WIDTH):
            x = self.get_x(i)
            for j in range(HEIGHT):
                y = self.get_y(j)
                self.img_mset.putpixel((i, j), Mandelbrot.get_color(x, y))

        # 重绘图片
        self.img_mset = ImageTk.PhotoImage(self.img_mset)
        self.cv.delete('all')
        self.cv.create_image(0, 0, anchor='nw', image=self.img_mset)

        # 启用输入
        self.accept_input = True
        self.title('曼德勃罗集 (x%d)' % self.scale)

    # 用户输入事件
    def scale_up(self, e):
        '''左键事件，以点击处为中心放大3倍'''
        if not self.accept_input:
            return

        # 计算缩放后区域
        new_x, new_y = self.get_x(e.x), self.get_y(e.y)
        new_width = (self.xmax - self.xmin) / 6
        new_height = (self.ymax - self.ymin) / 6
        self.xmin, self.xmax = new_x - new_width, new_x + new_width
        self.ymin, self.ymax = new_y - new_height, new_y + new_height

        # 重绘图像
        self.scale *= 3
        self.render_image()

    def scale_reset(self, e):
        '''右键事件，返回初始界面'''
        if not self.accept_input:
            return

        # 重置缩放倍数
        self.scale = 1
        self.title('曼德勃罗集 (x1)')

        # 重置渲染边界
        self.xmin, self.xmax, self.ymin, self.ymax = X1, X2, Y1, Y2
        self.cv.delete('all')
        self.cv.create_image(0, 0, anchor='nw', image=self.img_cover)


# 运行窗口
App().mainloop()