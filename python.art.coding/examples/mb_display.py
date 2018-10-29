from microbit import *

display.show('HELLO')
sleep(1000)
display.scroll('WORLD')
sleep(1000)
display.clear()
for i in range(5):
    display.set_pixel(i, i, 9)
    sleep(200)
display.clear()
display.scroll('BYE!')
