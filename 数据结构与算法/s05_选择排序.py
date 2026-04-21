"""
选择排序
    1. 核心思想
        把列表分成已排序区间 + 未排序区间
        每一轮找到未排序区间的最小值
        放到已排序区间的末尾
        重复直到有序
    2. 复杂度
        时间复杂度：永远 O (n²)
            无论有序无序，都必须跑完所有循环
        空间复杂度：O(1)（原地排序）
    3. 特点
        不稳定排序
        无法用 flag 优化
        交换次数极少（每轮最多 1 次）

"""

# 最简单的取最小值排序的方法：简单的演示 极其不推荐，即占内存，也耗时间 这里的时间复杂度为O(n^3), 空间复杂度为：O(n)
def select_sort_simple(li):
    new_li = [] # 新列表要占内存，空间复杂度：O(n)
    for i in range(len(li)): # for 循环 也为 O(n)
        min_loc = min(li) # min查找最小值为 O(n)
        new_li.append(min_loc)
        li.remove(min_loc) # remove删除后移动也要 O(n)
    return new_li

# 标准的选择排序
def select_sort(li):
    for i in range(len(li) - 1): # 已排序区间末尾
        min_loc = i # 记录最小值位置
        for j in range(i + 1, len(li)): # 从未排序区间开始找
            if li[j] < li[min_loc]:
                min_loc = j
        # 交换一次
        li[i], li[min_loc] = li[min_loc], li[i]
        print(li)

lst = [1,4,5,2,3,6,7,9,8]
# print(select_sort_simple(lst))
select_sort(lst)


