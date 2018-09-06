__doc__ = '''绘制色相圆盘

逐像素根据相对圆心坐标计算颜色
'''

from PIL import Image
from colorsys import hls_to_rgb
from math import atan2, pi

W = 500  # 图像长宽
R = 250  # 圆盘半径
D = 50  # 渐隐边缘占

# 新建空白透明图像
img = Image.new('RGBA', (W, W), (0, 0, 0, 0))

# 逐像素处理
for x in range(W):
    for y in range(W):
        dx, dy = x - W / 2, y - W / 2  # 相对圆心坐标
        hue = atan2(dx, dy) / (2 * pi)  # 角度对应色相
        satur = (dx**2 + dy**2)**0.5 / R  # 距离对应饱和度

        # 仅在饱和度不大于1（距离圆心小于R）时绘制
        if satur <= 1:
            # 计算RGBA（0-1）
            r, g, b = hls_to_rgb(hue, 0.5, satur)
            a = min(1, D - satur * D)

            # 转换为整数表达模式
            r, g, b, a = tuple(map(int, (r * 255, g * 255, b * 255, a * 255)))
            # 设置像素
            img.putpixel((x, y), (r, g, b, a))

# 输出图像
img.save('plate.png')