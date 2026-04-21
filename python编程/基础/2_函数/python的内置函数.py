"""
内置函数：直接能拿来用的函数
print
input
"""
# (一)基础数据类型相关
# 一、和数字相关
# 1.数据类型：int bool float complex
# s = "123"  # 转换数据类型
# i = int(s)
# b = bool(s)
# f = float(s)
# complex 复数类型：实部 + 虚部(带j) z = complex(3 + 4j)

# 2.进制转换：bin, oct, hex
# a = 18 #十进制
# print(bin(a)) # 0b表二进制 0b10010
# print(oct(a)) # 0o表八进制 0o22
# print(hex(a)) # 0x表十六进制 0x12
#
# b = 0b10010
# print(int(b)) # 将其他进制转化为十进制

# 3.数学运算：abs, divmod, round, pow, sum, min, max
# a = 10
# b = 3
# print(pow(a,b)) #a的b次方，即：a**b

# 二、和数据结构相关
# 1.序列
# 1)列表和元组：list, tuple 将传入的东西变成列表或元组
# s = {1, 3, 5, 8,}
# lst = list(s) #内部一定会有一个循环，将s遍历挨个放入lst列表
# print(lst)

# 2)相关内置函数：reversed, slice
# reversed 将数据反转 slice切片
# s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = list(reversed(s))
# print(b)
# sl = slice(1, len(s), 2)
# print(b[sl])

# 3)字符串：str, format, bytes, bytearry, memoryview, ord, chr, ascii, repr
# format：格式化
# a = 18
# print(format(a, "08b")) # b：二进制   08b：表示由0补充的八位二进制，超了会正常显示，不够会自动补齐
# print(format(a, "0o")) # o：八进制
# print(format(a, "x")) # x：十六进制
# a = "学" # python的内存中使用的是unicode
# print(ord(a)) # "学"在unicode中的码位是23398
# print(chr(23398)) # 给出编位位置，展示出文字
# i = 0
# while 1:
#     print(chr(i) + " ", end = "")
#     i = i + 1

# 2.数据集合
# 1)字典：dict
# 2)集合：set, frozenset   # frozenset：不可变集合

# 3.相关内置函数：len, sorted, enumerate, all, any, zip, fiter, map
# lst = ["周杰伦", "周深", "伍佰", "邓丽君"]
# for item in enumerate(lst): # 可以直接获取索引，以及其对应的元素
#     print(item)
# for index, item in enumerate(lst, start=1): # start=1 更改索引，让索引从1开始，但元素位置不变
#     print(index, item)
# for i in range(len(lst)):
#     print(i, lst[i])
# s = [1, "", "234"] #True  False
# print(all([1, "说啥", "234"])) #相当于and， t and t and t Ture
# print(all(s)) # t and f and t False
# print(any([0, "", ""])) # 相当于or，f or f or f False
# print(any(s)) # t or f or t Ture

# (二)其他
# 1.字符串类型代码的执行 eval, exec, complie
# 1)eval：执行字符串的代码，并返回最终结果
# 2)exec：执行字符串类型的代码
# 3)complie：将一个字符串编译为字节代码

# 2.输入输出 input, print

# 3.内存相关 hash, id
# 1)hash：计算哈希值
# 2)id：直接获取内存地址
# s = "呵呵"
# print(hash(s)) # 一定是一个数字 --> 想办法转化成内存地址，然后进行数据的存储 --> (字典，集合)哈希表
# print(id(s))

# 4.文件操作相关 open

# 5.模块相关 __import__

# 6.帮助 help 查看类型以及源代码

# 7.查看内存属性 dir 查看当前数据能执行哪些操作 (这是个好东西，可以经常用)
# s = [1, 2, 3, 4, 5, 6, 7]
# print(dir(s))

# 属于面向对象：调用相关 collable



