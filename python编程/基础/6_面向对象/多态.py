"""
    多态：就是同一种方法，在不同对象上有不同的实现方式(即一个接口，多种实现)
    python是动态类型语言
    鸭子类型：python通过鸭子类型实现多态，无需强制继承，只需要对象拥有对应的方法即可
        比如说风扇我设置了三个条件：
            1.能吹风 2.要插电 3.有线的
        只要一个物品满足了这三个条件，那么在python中他就是风扇
        比如说吹风机也满足了这三个条件，所以在python中吹风机就是风扇
"""
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def call(self):
        print(f"叫声是")

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def call(self):
        print(f"{self.name}叫声是汪汪汪")
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def call(self):
        print(f"{self.name}叫声是喵喵喵")

def call_function(animal: Animal):
    animal.call()

dog = Dog("小狗", 18)
cat = Cat("小猫", 18)
dog.call()
cat.call()
call_function(dog)
call_function(cat)