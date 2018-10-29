from microbit import *
import neopixel
from random import randint

# 创建一个彩灯对象
np = neopixel.NeoPixel(pin16, 12)
while True:
    # 循环每个灯珠
    for pixel_id in range(len(np)):
        red = randint(0, 60)
        green = randint(0, 60)
        blue = randint(0, 60)
        # 设置随机颜色RGB
        np[pixel_id] = (red, green, blue)
        # 显示彩灯
        np.show()
        sleep(100)
    # 清除彩灯
    np.clear()
