import random


def bucket_sort(li, n=100, max_count=100000):
    buckets = [[] for _ in range(n)]
    for val in li:
        ind = int(val // max_count * n)
        if ind == n:
            ind -= 1
        buckets[ind].append(val)

        j = len(buckets[ind]) - 2
        while j >= 0 and buckets[ind][j] > val:
            buckets[ind][j + 1] = buckets[ind][j]
            j -= 1
        buckets[ind][j + 1] = val

    li.clear()
    for bucket in buckets:
        li.extend(bucket)
    return li
#
li = [random.randint(1, 100) for _ in range(1000)]
# # print(li)
print(bucket_sort(li))