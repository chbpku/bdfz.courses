import random

menu = ["coffee", "tea", "cola", "milk", "water"]
print("Menu:", menu)
name = input("Your name please:")
drink = random.choice(menu)
print("Hello", name, "! Enjoy your", drink)
