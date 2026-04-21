# def partition(li, left, right):
#     tmp = li[left]
#     while left < right:
#         while left < right and li[right] >= tmp:
#             right -= 1
#         li[left] = li[right]
#         while left < right and li[left] <= tmp:
#             left += 1
#         li[right] = li[left]
#     li[left] = tmp
#     return left
#
# def quick_sort(li, left, right):
#     if left < right:
#         p = partition(li, left, right)
#         quick_sort(li, left, p - 1)
#         quick_sort(li, p + 1, right)

# import random

def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp: # 从右边找比tmp小的数
            right -= 1 # 往左走一步
        li[left] = li[right] # 把右边的值写到左边空位上
        while left < right and li[left] <= tmp: # 从左边找比tmp大的数
            left += 1 # 往右走一步
        li[right] = li[left] # 把左边的值写到右边空位上
    li[left] = tmp # 把tmp归为
    return left

def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)

lst = [5, 7, 4, 6, 3, 1, 2, 9, 8]
quick_sort(lst, 0, len(lst) - 1)
print(lst)