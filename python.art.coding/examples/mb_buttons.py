from microbit import *

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.scroll('AB')
        break
    elif button_a.is_pressed():
        display.show('A')
    elif button_b.is_pressed():
        display.show('B')
    sleep(100)
