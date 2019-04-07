from microbit import *
from random import randrange
import radio

display.show(Image.HAPPY)

f = []  # 一个列表，从99999到00000的图像
for i in range(9, -1, -1):
    imgstr = (str(i)*5+":")*5
    f.append(Image(imgstr))

radio.on()

while True:
    if button_a.was_pressed():
        radio.send('flash')  # 按键发送呼叫信息
    r = radio.receive()
    if r == 'flash':
        sleep(randrange(1000)+50)
        display.show(f, delay=100, wait=False)
        if randrange(10) <= 0:  #回应的机会0-9，数字越大，机会越大
            sleep(500)
            radio.send('flash') 
