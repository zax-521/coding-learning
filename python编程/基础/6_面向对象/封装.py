"""
    封装：指将类的属性和方法隐藏在类的内部，不允许外部直接访问或修改，
        仅通过类提供的公共接口(公开方法)来访问和操作内部数据
        私有属性：__属性名  User__user_password
            并不存在真正的私有，只是堆响应的私有属性，进行了后台重命名处理
            可以通过_User__user_password(即 实例对象._类名__私有属性名)
        弱私有：_属性名

    访问器：@property
    修改器：修改对象.setter(self, 传入参数)

"""
class User:
    def __init__(self, user_name, user_password, user_address, user_details):
        # 私有属性：__属性名 弱私有：_属性名
        self._user_name = user_name
        self.__user_password = user_password
        self._user_address = user_address
        self._user_details = user_details

user_1 = User(user_name="admin", user_password="admin123", user_address="J市", user_details="详细信息")

# print(user_1._user_name)
# print(user_1._User__user_password) # type:ignore
# print(user_1._user_address)
# print(user_1._user_details)

# 通过公共方法调用内部的私有属性
class Stu:
    def __init__(self, stu_name):
        self.__stu_name = stu_name
    # 实现私有属性的get方法
    def get_stu_name(self):
        return self.__stu_name
    # 实现私有属性的set方法
    def set_stu_name(self, new_stu_name):
        self.__stu_name = new_stu_name
stu = Stu("小学生")
# 以函数形式访问get_stu_name
print(stu.get_stu_name())
stu.set_stu_name("大学生")
print(stu.get_stu_name())

# 优雅的封装
class NweStu:
    def __init__(self, stu_name):
        self.__stu_name = stu_name
    # 使用@property装饰器，装饰私有属性的get方法，然后可以将他的get方法以属性字段的方式访问
    # 访问器
    @property
    def get_stu_name1(self):
        return self.__stu_name
    # 修改器
    @get_stu_name1.setter
    def set_stu_name1(self, new_stu_name):
        self.__stu_name = new_stu_name

new_stu = NweStu("小孩")
# 以属性字段的方式访问get_stu_name
print(new_stu.get_stu_name1)
new_stu.set_stu_name1 = "大人"
print(new_stu.get_stu_name1)

class People:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    # 内层：内层方法理论上是不允许被访问的
    def __format_people_details(self):
        return f"姓名：{self.__name}，居住地：{self.__address}"

    def __format_people_something(self):
        return "详细消息如下"

    # 表层：表层的方法是允许访问的
    def super_format(self):
        res1 = self.__format_people_details()
        res2 = self.__format_people_something()
        return res2 + "\n" + res1

people = People("老人", "M市")
print(people.super_format())