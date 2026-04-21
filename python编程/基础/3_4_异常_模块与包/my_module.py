#__all__ 指定 from...import * 导入的是哪些功能
__all__ = ["_version_module_private", "__version_module_private__"]
#常量(不会发生变化的数据，并非不可修改，只是约定俗成的规矩；常量的名称为全部大写)
name = "人"
VERSION_MODULE = "1.0.0"
#有些方法/函数/变量/类 私有变量：(你不希望被别人使用，但是你却不得不定义这样一个对象)
# 只能通过 import 包名 或 from 包名 import 私有变量导入
# 不能通过 from 包名 import * 导入
_version_module_private = "2.0.0"
__version_module_private__ = "3.0.0"
def func1(a, b):
    return a + b
def func2(a, b):
    return a - b
def func3(a, b):
    return a * b
def func4(a, b):
    return a / b