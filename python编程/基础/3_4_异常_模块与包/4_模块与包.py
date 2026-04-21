"""
module：模块
1.module的使用     (from 包名 import 变量/类对象/类/方法/函数)
    1) 导入的方式和重命名
        1. import 模块名,模块名,... == import 模块名 as 别名
            调用：模块名.功能名()        别名.功能名()
            导入模块 导入东西过多，会导致系统开支过大
        2. from 模块名 import 功能名 == from 模块名 import 功能名 as 别名
            调用：功能名()        别名()
            导入模块中的某个功能  极大程度上减少了系统的开支 (推荐使用)
        3. from 模块名 import *
            调用：功能名()
            导入模块中的所有功能  (及不推荐)更会导致系统的开支过大
    2) module的分类
        1.标准类库：math(数学计算)、random(随机数)、os(操作系统)、sys(系统参数)、
            datetime(日期时间)、time(时间访问)、re(正则)、csv(cvs文件操作)
        2.第三方库：需要pip install (numpy(数值)、pandas(数据)、matplotlib(画图)、request(网络)、
            torch/tensorflow(深度学习)、scikit-learn(深度学习)、flask/fastapi(后端))
        3.自定义库

2.自定义模块
    1) 创建和导入自定义模块
       每一个.py文件都是一个自定义模块

    2) __name__：当前文件的被操作情况
        1.当模块直接运行时(自己调用自己)：__main__
        2.当模块被导入时(其他人调用自己)：自己的文件名(不含.py后缀)

    3) 模块的私有变量                        from module import *
        1._var：弱私有（约定俗成，可访问）        默认不导入   注：看 第4)点
        2.__var：名称修饰，访问困难               不导入

    4)注：__all__(控制 import * 时导入哪些功能)== *    (即指定 from...import * 中的 * 导入的是哪些功能)
        如果导入的模块中定义了__all__ = [_var]
        这时 from module import * , 只能导入__all__中的功能

3.包：就是一个文件夹，里面可以存储很多Python模块(py文件)，通过包可以对模块进行归类
    1) 自定义包的使用
        import 包.模块名
        from 包名 import 模块名
        from 包名 import *
        from 包.模块名 import 功能
        from 包.模块名 import *
        注：使用带 * 的导入方法时，需要声明__init__.py文件当中声明__all__变量
        相对路径：从当前文件所在目录开始查找
            from 3_4_异常_模块与包.my_module import func1, func2
        绝对路径：从项目根目录下开始查找
            from 基础.练习.test_module import func3
    2) __init__.py
        作用：1.标识这是一个包，而不是普通文件夹
             2.控制在 import * 时导入的模块列表(__all__变量)
    3) 第三方包的使用：
        1.第三方包的下载语法规范(pip-cmd)
        通过 pip install 第三方包名 进行下载
        然后进行导入
"""
#module的使用
#定义一个无穷大的变量
# import math
# a = math.inf #inf = 无穷大
# from math import inf as i
# a = i
# print(a)
# from math import *
# a = inf
# print(a)

# from math import sin
# from datetime import datetime
# import math
# import numpy as np
# nums = np.array([1, 2, 3])
# print(nums, type(nums))

# 自定义模块
# a = 4
# b = 2
# nums = math.inf
# print(nums)

# import my_module
# print(my_module.VERSION_MODULE)
# ret1 = my_module.func1(a, b)
# print(ret1)
# ret2 = my_module.func2(a, b)
# print(ret2)
# ret3 = my_module.func3(a, b)
# print(ret3)
# ret4 = my_module.func4(a, b)
# print(ret4)
#__name__
# print(__name__)
# print(my_module.__name__)


# from my_module import *
# ret4 = my_module.func4(a, b)
# print(name)
# print(VERSION_MODULE)
# print(_version_module_private) #默认无法通过from my_module import * 导入私有变量












