import turtle, random
import shapefile # 需要安装shapefile模块，读取

turtle.tracer(0)  # 海龟加速，无动画

# 打开文件，读取地图文件信息
layer = shapefile.Reader('Africa.shp')
print("名称：", layer.shapeName)
print("外边界坐标：", layer.bbox)
print("对象个数：", layer.numRecords)

# 设置地图的外框，水平方向600像素，垂直方向按照bbox的比例
w = 600
h = int(w * (layer.bbox[3] - layer.bbox[1]) / (layer.bbox[2] - layer.bbox[0]))

print("地图的宽高：", w, h)
turtle.setup(w + 20, h + 30)

# 将海龟坐标系设置为与地图坐标相同
#turtle.setworldcoordinates(layer.bbox[0], layer.bbox[1], layer.bbox[2], layer.bbox[3])
turtle.setworldcoordinates(*layer.bbox)

map_pen = turtle.Turtle()
colors = ['yellow', 'red', 'green', 'blue', 'gray', 'pink', 'orange', 'cyan']

# 循环迭代地图中的每个对象
for f in layer.shapeRecords():
    # 画一个对象，可能包含多个多边形
    new_polygon = True  # 对象中的某个多边形开始
    start = None  # 多边形的开始顶点
    map_pen.penup()
    for xy in f.shape.points:
        map_pen.goto(xy)
        if new_polygon:
            start = xy
            map_pen.pendown()
            map_pen.fillcolor(random.choice(colors))
            map_pen.begin_fill()
            new_polygon = False
        elif xy == start:
            map_pen.end_fill()
            map_pen.penup()
            new_polygon = True
    turtle.update()

map_pen.hideturtle()
turtle.update()
turtle.done()
