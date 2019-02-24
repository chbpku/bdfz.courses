n = int(input("Please input line number:"))
for i in range(n):
    line = " " * (n - 1 - i) + "@" * (2 * i + 1)
    print(line)
