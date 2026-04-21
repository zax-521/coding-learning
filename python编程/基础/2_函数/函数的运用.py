"""
    一、函数的嵌套：函数可以嵌套函数
        1.函数可以作为返回值进行返回
        2.函数可以作为参数进行互相传递
        3.函数名称可以当成一个变量进行赋值操作，函数名称实际上就是一个变量名，都表示一个内存地址


    二、变量的作用域：变量的访问权限，即全局变量与局部变量
        global：在局部变量中，引入全局变量
        nonlocal：在局部中，引入外层的局部变量，如果外一层没有，将继续向外层引入，但不包括全局

    三、闭包：本质上是，内存函数对外层函数的局部变量的使用，此时内层函数被称为闭包函数
        1.可以让一个变量常驻于内存
        2.可以避免全局变量被修改

    四、装饰器：本质上是一个闭包
        作用：在不改变原有函数调用的情况下，给函数增添新功能。(即可以在函数前后添加新功能，且不修改原代码)
        例如：在用户登录的地方，添加日志
        通用装饰器的写法：
            def wrapper(fn): wrapper：装饰器，fn：目标函数
                def inner(*args, **kwargs): 这里的 *, ** 表示接收所有参数，打包成元组和字典
                    在目标函数执行之前
                    ret = fn(*args, **kwargs) 执行目标函数 这里的 *, ** 表示把args元组和kwargs字典，打散成位置参数和关键字参数，并传递进去
                    在目标函数执行之后
                    return ret
                return inner  记住这里不要加()不然返回的就是inner()执行后的结果
            @wrapper
            def target():
                pass
            target() # --> inner()

        一个函数可以被多个装饰器：
            @wrapper1
            @wrapper2
            def target():
                print("我是目标")
            输出的规律和规则： wrapper1 wrapper2 target wrapper2 wrapper1

    五、迭代器：
        迭代器的本身特性：1.迭代器本身也是可迭代的
                       2.只能向前不能反复，只能一直向下获取
                       3.特别省内存
                       4.惰性机制：只有用道德时候才计算或生成值
        for 变量 in 可迭代:
            pass
        iterable：可迭代的东西     str, list, tuple, dict, set, open()
        可迭代的数据类型都会提供一个叫迭代器的东西。这个迭代器可以帮我们把数据类型中的所有数据逐一的拿到
        获取迭代器的两种方案：
                        1. iter() 内置函数可以直接拿到迭代器
                        2.__iter__() 特殊用法
        从迭代器中获取数据：
                        1. next() 内置函数 每次只取一个
                        2. __next__() 特殊方法
        模拟for循环的工作原理：
            for循环里面一定是要使用迭代器，所以所有不可迭代的东西都不能使用for循环，且里面一定有next()或__next__()出现
            s = "数据内容"
            it = s.__iter__()
            while 1:
                try:
                    data = it.__next__()
                    print(data) # for循环的循环体
                except StopIteration:
                    break
        总结：迭代器统一了所有不同数据类型的遍历工作

    六、生成器（generator）：本质就是一个迭代器，即特殊的迭代器
            创建生成器的两种方案：1.生成器函数：
                                    1)生成器函数中有一个关键字 yield
                                    2)生成器执行的时候，并不会执行函数，且得到的是生成器
                                    3)只要函数中出现了yield，那么它就是一个生成器函数
                                    4)yield的作用：1.返回数据；2.可以分段的执行函数中的内容，通过__next__()可以执行到下一个yield的位子
                                    5)优势：用的好了，可以很大程度上节省内存
                              2.生成器表达式：(数据 for循环 if判断)

    七、推导式：简化代码
            1.列表推导式：[数据 for循环 if判断]
            2.集合推导式：{数据 for循环 if判断}
            3.字典推导式：{k:v for循环 if判断}
        注：没有元组推导式    (数据 for循环 if判断) --> 这个是生成器表达式

    八、匿名函数（lambda表达式）
        语法：变量 = lambda 参数1, 参数2, ..., 参数n : 返回值

    九、python内置函数_下 zip, locals, globals, sorted, filter, map
        1.zip：可以把多个可迭代的内容进行合并
        2.locals：函数会以字典的类型返回当前位置的全部局部变量，只返回当前位置的局部变量
        3.globals：函数会以字典的类型全部全部全局变量，即不管写哪都会返回全部的全局变量
        4.sorted：排序 sorted(要排序的可迭代数据, key = 排序函数(一般直接写lambda表达式), reverse(是否翻转) = True/False)
        5.filter：筛选 filter(筛选的条件, 要排序的可迭代对象)
        6.map：映射 map(处理规则, 要处理的可迭代对象) 批量将函数应用到可迭代对象的每个元素上，返回迭代器

    十、递归：函数自己调用自己
        def fun():
            fun()

        print(sys.getrecursionlimit())  获取当前python解释器允许的最大递归深度
        sys.setrecursionlimit(2000)  修改递归深度限制
        注：1.递归如果没有任何东西拦截的话，它默认是一个死循环
           2.python默认是有递归深度的限制的，默认的最大递归深度是1000（小于1000）
"""

# def fun1():
#     print(1)
#     def fun2():#fun2为内部函数，即局部作用域
#         print(2)
#     print(fun2)
#     return fun2 #此时将函数当成变量返回出去
# # 调用局部函数
# a = fun1() # 将return的fun2赋值给a,此时a=fun2
# a()# 调用a

# a = 10
# def func():
#     a = 20 #创建一个局部变量，并没有改变全局变量
#     print(a)
# def func2():
#     global a # 将外面的全局变量引入到局部
#     a = 30  #对外面的全局变量进行重新赋值
#     print(a)
# func()
# print(a)
# func2()
# print(a)

# a = 10
# def fun1():
#     a = 20
#     def fun2():
#         nonlocal a
#         a = 30
#         print(a)
#     def fun3():
#         print(a)
#     print(a)
#     return fun2, fun3
# b = fun1()
# print(a)
# for item in b:
#     item()
# print(a)
# fun1()

# def fun1(): # 函数的闭包
#     a = 10
#     def fun2():
#         nonlocal a
#         a += 1
#         return a
#     return fun2
#
# ret = fun1() #单独调动fun1()
# r1 = ret()
# print(r1)
# r2 = ret()
# print(r2)

# def wrapper(stu):
#     def study():
#         print("开启自动学习！！！")
#         stu()
#         print("关闭自动学习！！！")
#     return study
#
# @wrapper # @wrapper 的作用等于 ru = wrapper(ru)
# def ru():
#     print("学习俄语")
#
# @wrapper # @wrapper 的作用等于 py = wrapper(py)
# def py():
#     print("学习Python")
#
# # ru = wrapper(ru) # 让wrapper把ru重新封装一遍，将原先的ru替换成了study(wrapper函数里的返回值)
# ru()
# # py = wrapper(py)# 让wrapper把py重新封装一遍，将原先的ru替换成了study(wrapper函数里的返回值)
# py()

# def guanjia(game):
#     def inner(*args, **kwargs): # 这里的 *, ** 表示接收所有参数，打包成元组和字典
#         print("打开外挂")
#         ret = game(*args, **kwargs) # 这里的 *, ** 表示把args元组和kwargs字典，打散成位置参数和关键字参数，并传递进去
#         print("关闭外挂")
#         return ret
#     return inner
#
# @guanjia
# def print_dnf(username, password):
#     print("开始玩dnf了", username, password)
#     return "一把屠龙刀"
#
# @guanjia
# def print_lol(username, password, hero):
#     print("开始海克斯大乱斗", username, password, hero)
#     return "掉落一把钥匙"
#
# ret = print_dnf("admin", "123456")
# print(ret)
# ret1 = print_lol("admin", "123456", "狐狸")
# print(ret1)

# def wrapper1(fn): # fn = wrapper1.inner
#     def inner(*args, **kwargs):
#         print("进入wrapper1")
#         ret = fn(*args, **kwargs) # fn = wrapper1.inner
#         print("退出wrapper1")
#         return ret
#     return inner
#
# def wrapper2(fn):
#     def inner(*args, **kwargs):
#         print("进入wrapper2")
#         ret = fn(*args, **kwargs) # fn = target
#         print("退出wrapper2")
#         return ret
#     return inner
#
# @wrapper1 # target = wrapper1(wrapper2.inner) --> target：wrapper1.inner
# @wrapper2 # target = wrapper2(target) --> target：wrapper2.inner
# def target():
#   print("我是目标")
#
# target()

# login_flag = True
# def login(ap):
#     def inner(*args, **kwargs):
#         global login_flag
#         if login_flag:
#             print("请进行登录：")
#             while 1:
#                 username = input("账号>>>")
#                 password = input("密码>>>")
#                 if username == "admin" and password == "123456":
#                     print("登录成功")
#                     login_flag = False
#                     break
#                 else:
#                     print("登录失败，用户名或密码错误")
#         ret = ap(*args, **kwargs)
#         return ret
#     return inner
#
# @login
# def add():
#     print("添加员工信息")
#
# @login
# def delete():
#     print("删除员工信息")
#
# @login
# def upd():
#     print("修改员工信息")
#
# @login
# def search():
#     print("搜索员工信息")
#
# add()
# delete()
# upd()
# search()

# it = iter("你在干什么？")
# print(next(it),end="")    # ,end=：默认值为end="\n"，即print自动换 sep=：为分隔符，sep="-"以-分隔
# print(next(it),end="")
# print(next(it),end="")
# print(next(it),end="")
# print(next(it),end="")
# print(next(it),end="")
# print(next(it)) # StopIteration: 迭代已经停止了，不可能再次从迭代器中获取到数据

# it = "呵呵哒".__iter__()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

# s = "数据内容"
# it = iter(s)
# while 1:
#     try:
#         data = next(it)
#         print(data)
#     except StopIteration:
#         break

# def fun():
#     print("进入一")
#     yield "结束1"
#     print("进入二")
#     yield "结束2"
#     print("进入三")
#     yield "结束3"
#
# ret = fun()
# print(ret.__next__())
# print(ret.__next__())
# print(ret.__next__())

# def fun():
#     lst = []
#     for i in range(100):
#         lst.append(f"衣服{i + 1}")
#         if len(lst) == 10:
#             yield lst
#             lst = [] #下一次拿数据前，清空列表
#
# ret = fun()
# print(ret.__next__())
# print(ret.__next__())
# print(ret.__next__())
# print(ret.__next__())
# print(ret.__next__())
# print(ret.__next__())
# print(ret.__next__())
# print(ret.__next__())
# print(ret.__next__())
# print(ret.__next__())

# lst = []
# for i in range(10):
#     lst.append(i)
# print(lst)
#
# lst1 = [i for i in range(10)]
# print(lst1)

# lst = [i for i in range(1, 10, 2) if i % 2 != 0]
# print(lst)
# lst1 = [i for i in range(10) if i % 2 != 0]
# print(lst1)

# lst = [f"衣服{i+1}" for i in range(50)]
# print(lst)

# lst = ["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yz"]
# lst1 = [item.upper() for item in lst]
# print(lst1)

# s = {i for i in range(10)}
# print(s)

# lst = ["周杰伦", "周深", "蜡笔小新", "哆啦A梦"]
# dic = {lst.index(item):item for item in lst}
# dic1 = {i:lst[i] for i in range(len(lst))}
# print(dic)
# print(dic1)

# gen = (i**2 for i in range(5))
# for item in gen:
#     print(item)
# lst = list(gen) # 将迭代器中的数据存储在列表中
# print(lst) # 迭代器中剩余的数据，当没有数据时显示[]
# s = list("周杰伦") # list里面自带一个for循环，自带__next__()
# print(s)
#
# def fun(a, b):
#     return a + b
#
# fn = lambda a, b : a + b
#
# ret = fun(1, 2)
# ret1 = fn(1, 2)
# print(ret)
# print(ret1)

# lst1 = [1, 2, 3]
# lst2 = [11, 22, 33]
# lst3 = [111, 222, 333]
#
# result = []
# for i in range(len(lst1)):
#     first = lst1[i]
#     second = lst2[i]
#     third = lst3[i]
#     result.append((first, second, third))
# print(result)
#
# result1 = list(zip(lst1, lst2, lst3))
# print(result1)
#
# a = 1
# print(locals())
# def fun():
#     b = 1
#     print(f"fun函数内{locals()}")
# fun()
#
# a = 1
# print(globals())
# def fun():
#     b = 1
#     print(f"fun函数内{globals()}")
# fun()

# lst = ["你们仨", "你们几个人", "你", "你们几个", "你们"]
# s1 = sorted(lst, key = lambda i: len(i))
# print(s1)
# s2 = sorted(lst, key = lambda i: len(i), reverse = True)
# print(s2)

# lst = [
#     {"id": 1, "name": "asds", "age": 18, "salary": 15029},
#     {"id": 2, "name": "sda", "age": 38, "salary": 1531239},
#     {"id": 3, "name": "xcfsd", "age": 67, "salary": 11029},
#     {"id": 4, "name": "badcxcxc", "age": 58, "salary": 5029},
#     {"id": 5, "name": "gdasdd", "age": 8, "salary": 52559},
#     {"id": 6, "name": "daesdsff", "age": 48, "salary": 654859},
#     {"id": 7, "name": "lvzvzx", "age": 12, "salary": 123156},
#     {"id": 8, "name": "ewrwrew", "age": 20, "salary": 589465},
# ]
# s = sorted(lst, key = lambda x: x["age"])
# print(s)
# s1 = sorted(lst, key = lambda x: x["salary"], reverse = True)
# print(s1)

# lst = ["许长歌", "天衍", "离清焰", "许长天", "许歆骆", "冉青墨", "许殷鹤"]
# f = filter(lambda x : x.startswith("许"), lst)
# print(f)
# print(list(f))
# F1 = filter(lambda x : not x.startswith("许"), lst)
# print(F1)
# print(list(F1))

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# s = [item * item for item in lst]
# print(s)
# m = map(lambda x: x * x, s)
# print(m)
# print(list(m))

# import sys
# print(sys.getrecursionlimit()) # 获取当前python解释器允许的最大递归深度
# sys.setrecursionlimit(2000) # 修改递归深度限制