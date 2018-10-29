from microbit import *

display.show(Image.HAPPY)
sleep(1000)
a = Image('00000:22222:44444:77777:99999')
display.show(a)
s = [Image.YES, Image.NO, Image.SMILE, Image.DUCK, Image.CHESSBOARD]
for i in s:
    display.show(i)
    sleep(500)
s2 = []
for n in range(6):
    s2.append(a.shift_up(n))
display.show(s2,delay=200,wait=True,loop=True)
