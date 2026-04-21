"""
    堆排序的 topk 问题
        问题：现在有n个数，设计算法得到前k大的数。(k<n)
            取n数中前k数量，建立一个k数量的小根堆，将小根堆里最小的放在堆顶，
            然后再遍历k后面的列表一次与小根堆的堆顶进行比较，如果数大于小根堆堆顶就将其替换，然后再进行向下调整
"""
import heapq
import random


# 小根堆向下调整
def sift(li, low, high):
    i  = low
    j = 2 * i + 1
    tmp = li[i]
    while j <= high:
        if j + 1 <= high and li[j] > li[j + 1]:
            j = j + 1
        if tmp > li[j]:
            li [i] = li[j]
            i = j
            j = 2 * j + 1
        else:
            break
    li[i] = tmp

# 堆排序
def heap_sort(li, k):
    heap = li[0:k]
    # 构造堆
    for i in range((k - 2) // 2, -1, -1):
        sift(heap, i, k - 1)
    print("堆构造\n", heap)

    for i in range(k, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k - 1)

    # 堆排序
    for i in range(k - 1, 0, -1):
        heap[i], heap[0] = heap[0], heap[i]
        sift(heap, 0, i - 1)

    return heap

lst = [i for i in range(100)]
random.shuffle(lst)
print(lst)
# new_lst = lst[0:5]
# print(new_lst)
print(heap_sort(lst, 10))


