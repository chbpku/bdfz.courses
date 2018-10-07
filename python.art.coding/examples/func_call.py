def my_abs(n):
    if n >= 0:
        return n
    else:
        return -n


# 函数对象
s = my_abs
print("function object:", s)

# 加括号和参数，调用函数
s = my_abs(-10)
print("call function:", s)
