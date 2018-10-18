from PIL import Image

im = Image.open("images/4.jpg")
print(im.format, im.mode, im.size)
px = list(im.getdata())
print(len(px))
print(px[:900])
im.show()
