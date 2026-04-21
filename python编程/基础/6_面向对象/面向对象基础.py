"""
    oop：面向对象编程，将现实世界中的某些事物所具有的属性和动作抽象起来。
        例：
            小狗：
                属性：狗名、狗年龄、狗的种类、狗的颜色
                动作：叫、摇尾巴、吃
            小狗抽象为类
                属性页对应的是属性
                动作：魔法方法
    oop的组成部分：
        1. class 类 (狗这个大类) UserInfo 每个单词大写开头
        2. object 对象 (每一条狗)
        3. attribute 属性
        4. method 方法
    定义类时，__init__方法的作用：__init__是初始化方式，对象创建时自动调用，主要用于设置对象的初始状态(设置对象属性)
            self参数的作用：self是类中定义的方法的第一个参数，表示当前创建的实例对象
"""
class Dog:
    dog_name = "小白"
    dog_age = 3
    dog_color = "棕色"
    dog_type = "藏獒"

    def call(self):
        print("狗在叫")

    def make(self):
        print("狗在摇尾巴")

dog_1 = Dog()
print(f"dog_1 name is {dog_1.dog_name}")
dog_1.call()
dog_2 = Dog()
print(f"dog_2 age is {dog_2.dog_age}")
dog_2.make()
dog_3 = Dog()
print(f"dog_3 color is {dog_3.dog_color} and type is {dog_3.dog_type}")
dog_3.call()
dog_3.make()