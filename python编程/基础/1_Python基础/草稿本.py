# s = 'python just use'
# # 将python替换成python2
# s1 = s.replace('python', 'python2')
# print(s1)
# # 最前面的首字母大写
# s = s.capitalize()
# print(s)
# # 首字母大写
# s = s.title()
# print(s)
# # 所有字母变小写
# s = s.lower()
# print(s)
# # 所有字母变大写
# s = s.upper()
# print(s)
# i = 1
# for i in range(0,10):
#     print(i)
# i = 1
# while True :
#     if i == 1:
#         print(i)
#         i = i + 1
#         continue
#     elif i == 2:
#         print(i)
#     break

# lst = ['1one', '1two', '1three', '2one', '2two', '2three']
# for i in range(len(lst)):
#     item = lst[i]
#     if item.startswith('1'):
#         new_name = item.replace('1', '3')
#         lst[i] = new_name
# lst.sort(reverse=True)
# print(lst)

# lst = ['1one', '1two', '1three', '2one', '2two', '2three']
# for item in lst:
#     if item.startswith('1'):
#         lst.remove(item)
# print(lst)

# lst = ['1one', '1two', '1three', '2one', '2two', '2three']
# temp = []
# for item in lst:
#     if item.startswith('1'):
#         temp.append(item)
# for item1 in temp:
#     lst.remove(item1)
#     print(item1)
# print(lst)
#
# s1 = {"one", "two", "three", "4"}
# s2 = {"1", "2", "3", "4"}
# print(s1 | s2)

# wangfeng = {
#         "name" : "汪峰",
#         "age" : 40,
#         "wife" : {
#             "name" : "章子怡",
#             "hobby" : "演戏",
#             "assistant" : {
#                 "name" : "樵夫",
#                 "age" : "25",
#                 "hobby" : "打游戏"}
#             },
#         "children" : [
#             {"name" : "小孩1号", "age" : 13},
#             {"name" : "小孩2号", "age" : 10},
#             {"name" : "小孩3号", "age" : 8}]
#         }
# wangfeng["children"][1]["age"] += 1
# print(wangfeng["children"][1]["age"])


# s = "周杰伦"
# bs = s.encode("gbk")
# bs1 = s.encode("utf-8")
# print(bs1)

# print(10 == 2)

# f = open("../练习文件.txt", mode = "r", encoding = "utf-8")
# content = f.readlines()
# f.close()

import os
import time

with open("名单名.txt", mode ="r", encoding ="utf-8") as f1, \
    open("名单名_副本.txt", mode ="w", encoding ="utf-8") as f2:
    for line in f1:
        if line.startswith("周"):
            line = line.replace("周", "张")
        f2.write(line)
time.sleep(3)
os.remove("名单名.txt")
time.sleep(3)
os.rename("名单名_副本.txt", "名单名.txt")