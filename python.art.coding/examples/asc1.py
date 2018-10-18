from PIL import Image, ImageFont, ImageDraw

# 绘制文字
words = "Python Art"
# 准备一个字体
font = ImageFont.truetype("Arial", 15)
# 看这段文字绘制后的大小
size = font.getsize(words)
print('大小=', size)
# 新建一个图像，黑白模式，底色白色
im = Image.new('1', size, 'white')
draw = ImageDraw.Draw(im)
# 在图像上绘制文字
draw.text((0, 0), words, font=font)
im.show()
# 循环每个像素，黑色就记为"#"，白色就记为" "
asc = []
for p in list(im.getdata()):
    if p == 0:  # 黑色
        asc.append("#")
    else:
        asc.append(" ")

# 逐行打印出来, size=(列数，行数)
for row in range(size[1]):
    for col in range(size[0]):
        print(asc[row*size[0]+ col], end='')
    print()
