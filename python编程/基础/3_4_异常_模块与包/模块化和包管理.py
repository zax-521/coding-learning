"""
    模块的生命周期：
        1.加载阶段
        2.初始化阶段
        3.读缓存阶段
        4.销毁阶段
"""
# def func(x):
#     if x > 0:
#         func(x - 1)
#         print(x)
# func(3)
count = 0
def hanoi(n, a, b, c):
    global count
    if n > 0:
        hanoi(n - 1, a, c, b)
        count += 1
        print(f"从{a}移动到{b}")
        hanoi(n - 1, c, b, a)
    print(count)


hanoi(3, "A", "B", "C")
