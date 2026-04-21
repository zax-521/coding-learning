"""
    一、collections
        1.Count：对可迭代对象进行分类计数处理
        2.defaultdict：高级字典
            (1) 检查key是否存在
            (2) 当key存在时，返回对应value
            (3)当key不存在时，检查创建类型，会根据创建的类型返回不同的结果，且创建一个新的key-value
                list >>> [], int >>> 0, tuple >>> ()
        3.deque：双端队列
            deque和list的区别
        4.namedtuple：命名元组
    二、其他的附加数据结构
        (1) frozenset：不可变集合
        (2) heapq：堆
    三、来自第三包的高级数据结构 (numpy, pandas, ...)
"""
import collections

# names = ["aom", "dom", "dom", "aom", "bom", "bom", "bom", "aom", "com", "com", "dom"]
# res = collections.Counter(names)
# print(res, type(res))
# # print(dir(collections.Counter))
# res1 = collections.Counter.pop(res, "dom")
# print(res1, type(res1))
# print(res, type(res))
adict = {"name": "jom", "age": 18, "details": "详细信息"} # 普通字典
bdict = collections.defaultdict(list) # 创建一个默认类型为list的高级字典
cdict = collections.defaultdict(int) # 创建一个默认类型为int的高级字典
print(adict)
try:
    print(adict["address"])
except KeyError as ke:
    print(f"{KeyError}:{ke}") # 根据不存在的key，去访问value时，普通字典会报错 KeyError:'address'
# 针对高级字典defaultdict而言，当访问不存在的key时，会根据创建的类型返回不同的结果
# list >>> [], int >>> 0, tuple >>> ()
print(bdict)
print(bdict["address"])
print(bdict)
print(cdict)
print(cdict["address"])
print(cdict)
