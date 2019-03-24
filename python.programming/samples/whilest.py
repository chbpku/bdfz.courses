# 当n等于多少的时候，n阶乘超过10亿？
n = np = 1
while np < 10**9:  # 不超过10亿就继续循环
    n = n + 1
    np = n * np
print(n, "阶乘超过10亿，等于", np)

# =======================================

# 第一个能同时整除2/3/4/5/6的整数是哪个？
n = 1
while not (n % 2 == 0 and n % 3 == 0 \
           and n % 4 == 0 and n % 5 == 0 \
           and n % 6 == 0):
    n = n + 1
print("第一个能同时整除2/3/4/5/6的整数是", n)

# =======================================

# 摇几次骰子能摇到6？
import random
n = 1
while random.randint(1, 6) != 6:
    n = n + 1
print("摇了", n, "次骰子得到6")

import random
n = 1
if random.randint(1, 6) != 6:
    n = n + 1
print("摇了", n, "次骰子得到6")

# =======================================

# 当n等于多少的时候，n阶乘超过10亿？
np = 1
for n in range(1, 100):
    np = np * n
    if np > 10**9:
        break
print(n, "阶乘超过10亿，等于", np)

# =======================================

for i in range(1, 100):  # 从1到99的报数游戏
    # 包含数字7，或者能被7整除
    if ('7' in str(i)) or (i % 7 == 0):  
        print("过！", end = ', ')
        continue
    print(i, end = ', ')



