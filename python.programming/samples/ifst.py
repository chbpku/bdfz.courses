# 计算x1和x2之间的距离
x1 = int(input("x1="))
x2 = int(input("x2="))
if x1 > x2:
    d = x1 - x2
else:
    d = x2 - x1
print("distance=", d)

# 判断偶数
n = int(input("n="))
print("Your number is", n)
if n % 2 == 0:
    print("It's a even number!")

# 判断年龄
age = int(input("age="))
print("年龄：", age)
if 0 <= age <= 6:
    print("童年")
elif 7 <= age <= 17:
    print("少年")
elif 18 <= age <= 40:
    print("青年")
elif 41 <= age <= 65:
    print("中年")
else:
    print("老年")

# 获取输入一行用空格隔开的整数
numbers = input("some numbers:").split()
numbers = list(map(int, numbers))
print(numbers)

# 简写
numbers = list(map(int, input().split()))

