"""
    1.堆：一种特殊的完全二叉树结构
        大根堆：一棵完全二叉树，满足任意一个节点都比其孩子节点大"""
        #         9
        #       /   \
        #      8     7
        #     / \   / \
        #    6   5 0  1
        #  / \  /
        # 2  4 3
        # 小根堆：一棵完全二叉树，满足任意一个节点都比其孩子节点小
        #         1
        #       /   \
        #      2     6
        #     / \   / \
        #    3   5 7  9
        #  / \  /
        # 4  6 8
"""
    2.堆的向下调整
    3.构造堆
    4.堆排序的过程：
        1.建立堆
        2.得到堆顶元素，为最大元素
        3.去掉堆顶，将堆最后一个元素放到堆顶，此时可通过一次调整重新使堆有序
        4.堆顶元素为第二大元素
        5.重复步骤3，直到堆变空
    5. 放回堆排序里
        1.树高 = log₂n (写复杂度时直接写：O(log n))
        2.一次 sift：O(log n)
        3.建堆：O(n)
        4.堆排序：O(n log n)
    6.堆的内置模块 (heapq)
    7.堆排序的 topk 问题
        问题：现在有n个数，设计算法得到前k大的数。(k<n)
        解题思路：
            排序后切片：O(n log n)
            排序LowB三人组：O(k n)
            堆排序思路：O(n log k)
"""

# def dui(lis):
#     for i in lis:
#         len(lis) - i - 1 // 2
# print(8 // 2)
# print(7 // 2)

# 堆的向下调整
# def sift(li, low, high):
#     """
#     :param li:列表
#     :param low: 堆的根节点位置
#     :param high: 堆的最后一个元素的位置
#     :return:
#     """
#     i = low # i 最开始只指向根节点
#     j = 2 * i + 1 # j最开始是左孩子
#     tmp = li[low] # 把堆顶存起来
#     while j <= high: # 只要j还有数
#         if j + 1 <= high and li[j] < li[j + 1]: # 如果右孩子有并且比左孩子大
#             j = j + 1 # j 指向右孩子
#         if li[j] > tmp: # 如果孩子比堆顶大
#             li[i] = li[j]
#             i = j # 往下看一层
#             j = 2 * j + 1
#         else: # 如果tmp比孩子大，把tmp放在i的位置
#             # li[i] = tmp # 把tmp放到某一级的堆顶
#             break
#     # else:
#     #     li[i] = tmp # 当已经到叶子节点这一层时，把tmp放到叶子节点上
#     li[i] = tmp # 前面两个li[i] = tmp 可以简写在这一行
#
# # 堆排序
# def heap_sort(li):
#     n = len(li)
#     # 构造堆
#     for i in range((n - 2) // 2, -1, -1):
#         # i 表示建堆的时候调整的部分的根的下标
#         sift(li, i, n - 1)
#
#     print(li)
#     # 堆排序
#     for i in range(n - 1, -1, -1):
#         # i 指向当前堆的最后一个元素
#         li[0], li[i] = li[i], li[0]
#         sift(li, 0, i - 1) # i - 1是新的high
#
# lst = [2,3,4,1,9,5,7,8,6]
# heap_sort(lst)
# print(lst)

# 堆的内置模块
import heapq # q -> queue 优先队列
import random

lst1 = [i for i in range(1, 20)]
random.shuffle(lst1)
print(lst1)

# 建堆
heapq.heapify(lst1)
print(lst1)
for i in range(len(lst1)):
    print(heapq.heappop(lst1), end=",")
