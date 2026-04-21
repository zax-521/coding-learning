"""
try-except 异常捕捉模式
1.基础概念和异常结构
    概念：当代码报错时给出的错误提示称为异常
        IndexError: list index out of range
        异常名称：IndexError     异常详细信息：list index out of range

    结构：try:
            需要执行的代码
        except:
            当发生异常时，会触发此处的代码片段的执行操作

2.指定异常捕捉(单/双)
单：
try:
    pass
except IndexError:单指定异常捕捉
    pass
双：
try:
    pass
except (IndexError,NameError):捕捉双指定异常
    pass
3.捕捉异常详情
num = [1, 2, 3]
try:
    n = num[4]
    print(n)
except IndexError as e:
    print(f"捕捉异常详情:{e}")

4.else无异常时执行
try:
    pass
except Exception:
    print("出现异常时执行")
else:
    print("无异常时执行")

5.finally有无异常都执行
try:
    pass
except Exception:
    print("出现异常时执行")
else:
    print("无异常时执行")
finally:
    print("无论是否有异常时都执行，一般用来释放空间")

6.raise主动抛出异常
password:str = input("输入密码，密码长度为(6-13):")
try:
    if password <= 6 or password >= 13:
        raise ValueError("重新输入，密码长度不对")
    else:
        print("无误")
except ValueError:
    print("")

7.自定义异常 Exception
"""
# num = [1, 2, 3]
# try:
#     print(num[2])
#     # raise IndexError("主动抛出异常")
# except IndexError as e:
#     print(f"当有e异常时输出异常详情{e}")
# else:
#     print(f"当没有raise时，没有IndexError异常时输出")
# finally:
#     print("无论是否发生错误都会执行")

# class My_exception(Exception):
#     def __init__(self, *args: object) -> None:
#         print(f"args:{args}")
#     super().__init__("自定义异常")

# password : str = input("输入密码，密码长度为(6-13):")
# print(len(password))
# try:
#     if len(password) < 6 or len(password) > 13:
#         raise ValueError("重新输入，密码长度不对")
#     else:
#         print("设置成功")
# except ValueError as e:
#     print(f"[ValueError]:{e}")

# name : str = input("输入一个name，其中1 < name.size < 9:")
# try:
#     if len(name) <= 1 or len(name) >= 9:
#         raise ValueError("在设置name时，name的长度应该在合法范围之内")
#     else:
#         print("设置成功")
# except ValueError as e:
#     print(f"[ValueError]:{e}")