"""
    递归：函数自己调用自己
        def fun():
            fun()

        print(sys.getrecursionlimit())  获取当前python解释器允许的最大递归深度
        sys.setrecursionlimit(2000)  修改递归深度限制
        注：1.递归如果没有任何东西拦截的话，它默认是一个死循环
           2.递归必须有输出条件
           3.python默认是有递归深度的限制的，默认的最大递归深度是1000（小于1000）
"""
def func(x):
    if x > 0:
        func(x - 1)
        print(x)

def func1(x):
    if x > 0:
        print(x)
        func(x - 1)

func(3)
print("=" * 20)
func1(3)