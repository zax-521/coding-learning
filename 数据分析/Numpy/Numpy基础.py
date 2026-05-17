"""
    1.Numpy简介
        1.Numpy重要功能：
            1.高性能科学计算和数据分析基础包
            2.ndarray，多维数组，具有矢量运算能力，快速、节省空间
            3.矩阵运算，无需循环，可完成类似Matlab中的矢量运算
            4.用于读写磁盘数据的工具以及用于操作内存映射文件的工具

    2.Numpy属性：Numpy的数组类被称作ndarray，通常被称作数组
        Numpy数组是一个多维的数组对象(矩阵)，成为ndarray
        注：ndarray的下标从0开始，且数组内的所有元素必须是相同类型
        1.ndarray对象属性有：
            1.ndarray.ndim
            2.ndarray.shape
            3.ndarray.size
            4.ndarray.dtype
            5.ndarray.itemsize
            6.数组的维度：这是一个指示数组在每个维度上大小的整数元组。
                例：一个n排m列的矩阵，它的shape属性将是(2,3)，
                    这个元组的长度显然是秩，即维度或者ndim属性。

    3.创建ndarray：
        1.np.array()：创建ndarry对象，即将python列表转换成ndarray对象
        2.np.arange(起始, 结束, 步长, dtype=类型)：类似python的range()，创建一个一维ndarray数组(包左不包右)
        3.np.random()：创建随机数矩阵
            1.np.random.rand(3, 4)：(包左不包右)
                生成指定维度大小(3行4列)的随机多维浮点型数据(二维)，
                    rand固定区间0.0 ~ 1.0

            2.np.random.randint(-1(起始值), 5(结束值), size = (3(行), 4(列)))：(包左不包右)
                生成指定维度大小(3行4列)的随机多维整型数据(二维)，
                    randint()可指定区间(-1, 5)

            3.np.random.uniform(-1, 5, size = (3, 4))：(包左不包右)
                生成指定维度大小(3行4列)的随机多维浮点型数据(二维)，
                    uniform()可指定区间(-1, 5)产生-1到5之间均匀分布的样本值

            4.np.random.randn()：返回具有标准正态分布(即均值为 0、标准差为 1，X ~ N(0, 1))的序列

            5.np.random.seed()：固定随机数结果，保证可复现
                例： np.random.seed(42)          # 42 可以是任意整数
                    arr = np.random.rand(3)     # 每次运行结果一样

            6.np.random.normal(loc=均值, scale=标准差, size=数量)：生成正太分布随机数
                1.均值（loc）：分布的中心
                2.标准差（scale）：数据越分散越大
                3.68% 数据落在 [均值 ± 标准差]
                4.95% 数据落在 [均值 ± 2×标准差]

        4.ndarray的数据类型：
            1.dtype参数，指定数组的数据类型，类型名+位数，如float64，int32
            2.astype方法，转换数组的数据类型
                例：将数据类型int64转换为float64
                    arr = np.arange(0, 10, 2, dtype=np.int64)
                    new_arr = arr.astype(np.float64)
                    print(arr.dtype)
                    print(new_arr.dtype)

        5.等比/等差数列：
            1.等比数列：np.logspace(开始点(幂指数), 结束点(幂指数), 生成数量, base=底数, dtype=np.数据类型)
                注：开始点和结束点是默认是10的幂，默认数据类型为float64
                例：1.从 10^0=1 到 10^2=100，生成5个数
                    arr = np.logspace(0, 2, 5) # 10^0 到 10^2
                    print(arr)
                   2.从 2^0 到 2^4，生成5个数
                    arr1 = np.logspace(0, 4, 5, base=2) # 2^0 到 2^4
                    print(arr1)

            2.等差数列：np.linspace(起点, 终点, 生成数量, endpoint=False, retstep=True, dtype=np.数据类型)
                endpoint：bool类型，是否包含结束值
                retstep：bool类型，是否返回步长，True是，False否，默认为False
                dtype：默认为float
                例：arr, step = linspace(0, 100, 5, retstep=True))
                   print(f"等差数列：{arr}，步长：{step}")

    4.Numpy内置函数：
        1.常用函数：
            1.np.ceil()：向上取整，参数是number或array
            2.np.floor()：向下取整，参数是number或array
            3.np.rint()：四舍五入，参数是number或array
            4.np.isnan()：判断元素是否为 NaN(Not a Number)，参数是number或array
            5.np.multiply()：元素相乘，参数是number或array
            6.np.divide()：元素相除，参数是number或array
            7.np.abs：元素的绝对值，参数是number或array
            8.np.where(condition(条件), x, y)：三元运算符，x if condition(条件) else y

        2.统计函数：参数都为 number 或 array
            1.np.sum()：所有元素的和
            2.np.mean()：所有元素的平均值
            3.np.max()：所有元素的和最大值
            4.np.min()：所有元素的最小值
            5.np.std()：所有元素的标准差
            6.np.var()：所有元素的方差
            7.np.argmax()：最大值的下标索引值
            8.np.argmin()：最小值的下标索引值
            9.np.cumsum()：返回一个一维数组，每个元素都是之前所有元素的累加和
            10.np.cumprod()：返回一个一维数组，每个元素都是之前所有元素的累乘积
            ***注***：多维数组默认统计全部维度，axis参数可以按指定轴心统计，值为0则按列统计，值为1则按行统计

        3.去重函数：
            1.np.unique()：找到唯一值并返回排序结果，类似于python的set集合
            注：去重返回新副本

        4。排序函数：
            1.np.sort(arr)：返回排序后的副本
            2.ndarray对象.sort()：直接调用sort，在原数据上进行修改

    5.Numpy运算：
        1.基本运算：数组的算数运算是按照元素的。新的数组被创建并且被结果填充
            即正常的同维度，行乘行，列乘列
        2.矩阵乘法：解释图看 "矩阵乘法.png"，即行乘列
            1. x @ y 或 np.dot(x, y) 或 x.dot(y)
                例：x = np.array([[1, 2, 3], [4, 5, 6]])
                   y = np.array([[6, 23], [-1, 7], [8, 9]])
                   print(x @ y)
                   print(x.dot(y))
                   print(np.dot(x, y))
                注：A(m,n) @ B(p,q) 可乘条件：n == p，结果形状：(m, q)，即A列 == B行，结果为：A行B列
                    例：错误写法：A(2,3) @ B(2,4)  ❌ 因为 3 != 2
                       正确写法：A(2,3) @ B(3,4)  ✅ 结果 (2,4)

    6.布尔索引：用条件筛选数组元素
        例： arr = np.array([10, 20, 30, 40, 50])
            # 单条件
            arr[arr > 30]               # [40, 50]

            # 多条件（必须加括号，用 & 和 |）
            arr[(arr > 20) & (arr < 50)]   # [30, 40]  且
            arr[(arr < 20) | (arr > 40)]   # [10, 50]  或

"""

import numpy as np

# # 2.ndarray的对象属性
# arr1 = np.arange(15).reshape(3, 5)
# print(arr1)
# print(f"numpy的维度(shape):{arr1.shape}")
# print(f"numpy的轴(ndim):{arr1.ndim}")
# print(f"numpy的元素类型(dtype):{arr1.dtype}")
# print(f"numpy的元素占用字节数(itemSize):{arr1.itemsize}")
# print(f"numpy的元素个数(size):{arr1.size}")
# print(f"type:{type(arr1)}")

# # 3.创建ndarray
# # 3.1 array
# a = np.array([1, 2, 3])
# print(f"数组a元素类型：{a}")
# print(f"数组a类型：{a.dtype}")
#
# b = np.array([1.2, 3.5, 5.1])
# print(f"数组b元素类型：{b}")

# # 3.2 arange
# np_arange = np.arange(10, 20, 5, dtype=int)
# print(f"arange创建np_arange:{np_arange}")
# print(f"arange创建np_arange的元素类型:{np_arange.dtype}")
# print(f"arange创建np_arange的类型:{type(np_arange)}")

# # 3.3 random
# arr1 = np.random.rand(3, 4)
# arr2 = np.random.randint(-1, 5, size = (3, 4))
# arr3 = np.random.uniform(-1, 5, size = (3, 4))
# print(arr1)
# print(type(arr1))
# print("=================================")
# print(arr2)
# print(type(arr2))
# print("=================================")
# print(arr3)
# print(type(arr3))
#
# arr1 = np.arange(15).reshape(3,5)
# arr2 = np.arange(15, 30).reshape(3, 5)
# print("=================arr1=================")
# print(arr1)
# print("=================arr2=================")
# print(arr2)
# print("===============arr1 + arr2============")
# print(arr1 + arr2)
# print("===============arr1 - arr2============")
# print(arr1 - arr2)
# print("===============arr1 * arr2============")
# print(arr1 * arr2)
# print("===============arr1 / arr2=============")
# print(arr1 / arr2)
#
# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.DataFrame(range(15))
# df.plot()
# plt.show()

# # 3.4 astype
# arr = np.arange(0, 10, 2, dtype=np.int64)
# print(arr)
# print(arr.dtype)
# arr1 = arr.astype(np.float64)
# print(arr1)
# print(arr1.dtype)

# 3.5 1.logspace
# arr = np.logspace(1, 3, 5)
# print(arr)
# print(arr.dtype)
# arr1 = np.logspace(0, 4, 5, base=2, dtype=np.int64)
# print(arr1)
# print(arr1.dtype)

# 3.5 2.linspace
# arr, step = np.linspace(0, 100, 5, retstep=True)
# print(f"等差数列：{arr}，步长：{step}")
# print(arr.dtype)
#
# arr1, step1 = np.linspace(0, 100, 5, retstep=True, dtype=np.int64)
# print(f"等差数列：{arr1}，步长：{step1}")
# print(arr1.dtype)
#
# arr2, step2 = np.linspace(0, 100, 5, retstep=True, dtype=np.int64, endpoint=False)
# print(f"等差数列：{arr2}，步长：{step2}")
# print(arr2.dtype)


# 4. Numpy的内置函数
# # 4.1 常用内置函数
# arr = np.random.randn(2, 3)
# print("==============arr==============")
# print(arr)
# print("============向上取整============")
# print(np.ceil(arr))
# print("============向下取整============")
# print(np.floor(arr))
# print("============四舍五入============")
# print(np.rint(arr))
# print("============判断NaN============")
# print(np.isnan(arr))
# print("=============相乘==============")
# print(np.multiply(arr, arr))
# print("=============相除==============")
# print(np.divide(arr, arr))
# print("============绝对值=============")
# print(np.abs(arr))
# print("===========三元运算符===========")
# print(np.where(arr > 0, 1, -1))

# 4.2 统计函数
# arr1 = np.random.randint(1, 20, size = (3, 4))
# print(arr1)
# print("和",np.sum(arr1))
# print("行求和：",np.sum(arr1, axis=0))
# print("列求和：",np.sum(arr1, axis=1))
# print("平均数",np.mean(arr1))
# print("最大值：",np.max(arr1))
# print("最小值：",np.min(arr1))
# print("最大值下标索引：",np.argmax(arr1))
# print("最小值下标索引：",np.argmin(arr1))
# print("标准差：",np.std(arr1))
# print("方差：",np.var(arr1))
# print("累计和：",np.cumsum(arr1))
# print("累积乘积：",np.cumprod(arr1))

# # 4.3 去重函数
# arr = np.array([[1, 2, 1], [2, 3, 4]])
# print("========arr=========")
# print(arr)
# print("========unique=========")
# print(np.unique(arr))

# # 4.4 排序函数
# arr = np.array([1, 2, 34, 5])
# new_arr = np.sort(arr)
# print("========arr=========")
# print(arr)
# print("========new_arr=========")
# print(new_arr)
# arr.sort()
# print("========arr.sort()=========")
# print(arr)

# 5.Numpy运算
# # 5.1 基本运算
# a = np.array([20, 30, 40, 50])
# b = np.arange(2, 6)
# c = a+b
# d = a-b
# e = a*b
# f = a/b
# print("数组a：",a)
# print("数组b：",b)
# print("数组运算a+b：",c)
# print("数组运算a-b：",d)
# print("数组运算a*b：",e)
# print("数组运算a/b：",f)

# 5.2 矩阵乘法
# x = np.array([[1, 2, 3], [4, 5, 6]])
# y = np.array([[6, 23], [-1, 7], [8, 9]])
# print(x)
# print(y)
# print(x.dot(y))
# print(np.dot(x, y))
