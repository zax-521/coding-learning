"""
    列表查找：内置列表查找函数index()
        1.顺序查找(线性查找)
        2.二分查找
"""
from a计时器 import cal_time

# 顺序查找
@cal_time
def linear_search(lis : list, val):
    # enumerate() 是 Python 内置函数，核心作用是：遍历可迭代对象（列表、字符串、元组等）时，同时获取「元素的索引」和「元素本身」。
    for ind, v in enumerate(lis):
        if v == val:
            return ind
    else:
        return None

# 二分查找
@cal_time
def binary_search(lis : list, val):
    left = 0
    right = len(lis) - 1
    while left <= right:
        mid = (right + left) // 2
        if lis[mid] == val:
            return mid
        elif lis[mid] < val:
            left = mid - 1
        elif lis[mid] > val:
            right = mid + 1
    else:
        return None

lst = list(range(1, 100000))
print(linear_search(lst, 3787))
print(binary_search(lst, 3787))

