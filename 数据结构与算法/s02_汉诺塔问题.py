"""
    经典递归问题
"""
# 将所有盘子从a放到c (盘子数量，起点，辅助，终点)
def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n - 1, a, c, b)
        print(f"将第{n}个盘子从{a}放到{c}")
        hanoi(n - 1,b, a, c)
hanoi(4, "A", "B", "C")

# 将所有盘子从a放到b (盘子数量，起点，终点，辅助)
def hanoi1(n, a, b, c):
    if n > 0:
        hanoi1(n - 1, a, c, b)
        print(f"将第{n}个盘子从{a}放到{b}")
        hanoi1(n - 1, c, b, a)
hanoi(4, "A", "B", "C")