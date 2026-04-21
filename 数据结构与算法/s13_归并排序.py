"""
归并排序：
    一、基本思想
        分治法：把待排序数组递归拆分成更小的子数组，直到每个子数组只有一个元素（天然有序）。
        合并：将两个有序子数组合并成一个更大的有序数组，层层向上合并，最终得到完整有序数组。
    二、核心步骤
        1.分解：
            找到数组中点 mid，把数组分为左半部分 [left, mid] 和右半部分 [mid+1, right]。
        2.解决：
            递归对左右子数组分别进行归并排序。
        3.合并：
            用双指针遍历两个有序子数组，按大小依次放入临时数组，最后覆盖回原数组。
    三、复杂度分析
        1.时间复杂度
            最好、最坏、平均：O(n log n)
            拆分：log n 层；合并每层 O (n)
        2.空间复杂度
            O(n)（需要临时数组存储合并结果）
            稳定性：稳定排序（相等元素相对位置不变）
    四、特点与适用场景
        1.优点
            效率稳定，始终 O (n log n)，不受数据初始顺序影响。
            稳定排序，适合对稳定性有要求的场景。
            外部排序常用（数据太大无法全部载入内存时）。
        2.缺点
            需要额外 O (n) 空间，空间开销较大。
            常数因子比快速排序大，实际速度通常略慢于快排。
"""

import random

def merge(li, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high + 1] = ltmp

def merge_sort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)

lst = [i for i in range(20)]
random.shuffle(lst)
print(lst)
merge_sort(lst, 0, len(lst) - 1)
print(lst)


# lst = [2, 4, 6, 7, 9, 1, 3, 5, 8, 10]
# print(lst)
# print(len(lst) - 1)
# print((len(lst) - 1) // 2)
# merge(lst, 0, (len(lst) - 1) // 2, len(lst) - 1)
# print(lst)
