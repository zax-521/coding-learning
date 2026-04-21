"""
    继承：就是子类继承父类的所有公共属性和公共方法，
        且子类可以再父类的基础上扩展新的属性和方法，页可以重写父类的方法
    多继承：1.子类的优先级大于父类
          2.先继承大于后继承
          3.广度 > 深度
    super()函数一同与按照MRO顺序调用父类方法
    MRO列表：会指明继承的优先级，是多继承的核心，通过__mro__可以查看方法查询顺序
"""
# 单继承
# class Animal(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self, food):
#         print(f"{self.name}吃{food}")
#
# class Dog(Animal):
#     def __init__(self, name, age, type_a):
#         self.type_a = type_a
#         super().__init__(name, age)
#
#     def drink(self, wator):
#         print(f"{self.name}喝{wator}")
#
# class Cat(Animal):
#     def __init__(self, name, age, type_a):
#         self.type_a = type_a
#         super().__init__(name, age)
#
#     # 对父类的重写
#     def eat(self, food):
#         print(f"{self.name}是{self.type_a}只吃{food}")
#
# dog = Dog("小狗", 3, "边牧")
# dog.eat("狗粮")
# dog.drink("水")
# cat = Cat("小黄", 3, "加菲猫")
# cat.eat("千层披萨")
# dog.eat("高级狗粮")

# 多继承

# class School:
#     def __init__(self, name_s, address):
#         self.name_s = name_s
#         self.address = address
#
# class Teacher(School):
#     def __init__(self, name, address, name_t, age_t):
#         School.__init__(self, name, address)
#         self.name_t = name_t
#         self.age_t = age_t
#
# class Grade(School):
#     def __init__(self, name, address, grade):
#         School.__init__(self, name, address)
#         self.grade = grade
#
# class Student(Grade, Teacher):
#     def __init__(self, name_s, address, grade, name_t, age_t, name, age):
#         Grade.__init__(self, name_s, address, grade)
#         Teacher.__init__(self, name_s, address, name_t, age_t)
#         self.name = name
#         self.age = age
#
#
#
# stu = Student('大专', 'M市', '二年级', '高老师', '35', '小白', '19')
# mro_list = Student.__mro__
# print(mro_list)
# print(stu.name_s, stu.address, stu.grade, stu.name_t, stu.age_t, stu.name, stu.age)
