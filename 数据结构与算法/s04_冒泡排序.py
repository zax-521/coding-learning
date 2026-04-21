"""
    冒泡排序
        1. 核心思想
            1.从头开始，两两比较相邻元素
            2.大的往后换，每一轮冒出一个最大值
            3.重复直到有序
        2. 复杂度
            1.时间复杂度：
                1.最好情况（有序）：O(n)
                2.最坏 / 平均：O(n²)
            2.空间复杂度：O(1)（原地排序）
        3. 特点
            1.稳定排序
            2.可以加 flag 优化
            3.有序时效率极高
"""
# 冒泡排序
import random

def bubble_sort(li):
    for i in range(len(li) - 1): # 外层循环：控制轮数
        exchange = False # 优化标记
        for j in range(len(li) - i - 1): # 内层循环：两两比较
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        print(li)
        if not exchange: # 一轮无交换 → 已有序
            break # 提前退出

lst = [random.randint(1, 50) for _ in range(10)]
print("=" * 20 + "初始列表"+ "=" * 20)
# lst = [1,324,53,645,78,43,52,4,5]
print(lst)
print("=" * 20 + "开始冒泡排序" + "=" * 20)
bubble_sort(lst)
# print(lst)