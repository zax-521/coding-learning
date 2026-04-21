import random

def radix_sort(li):
    max_val = max(li)
    max_digit = len(str(max_val))
    for digit in range(max_digit):
        buckets = [[] for _ in range(10)]
        for val in li:
            divisor = val // 10 ** digit % 10
            buckets[divisor].append(val)
            print(buckets)
        li.clear()
        for bucket in buckets:
            li.extend(bucket)
        print(li)


