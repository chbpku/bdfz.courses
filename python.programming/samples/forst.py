s = 0
for i in range(1, 101):
    s = s + i
print("sum:1..100:", s)

a, b, c = 10, -5, 0.5
for x in [-25, 0, 10, 35, 100]:
    y = a * x * x + b * x + c
    print (f"f({x})={y}")

for name in ["Tom", "Jerry", "张三"]:
    print("Hello!", name)

for n in [1, 3, 5, 35, -10]:
    print(f"{n}^2=", n * n)

m = 1
for f in [1.23, 34.5, 10.0, 245.7]:
    m *= f
print("product:", m)

for k in [12, 30, 8, 10, 9]:
    print(f"{k:02d}>", "#"*k)
