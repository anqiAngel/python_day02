import socket


# 使用getter方法来表示计算的属性
class Rectangle:
    """
        表示矩形的类
    """

    def __init__(self, width, height):
        self.hidden_width = width
        self.hidden_height = height

    # property装饰器,用来将一个get方法,转换为对象的属性
    # 添加 property装饰器以后,我们就可以像调用属性一样使用get方法
    # 直接 r.get方法名
    # 使用 property装饰的方法,必须和属性名是一样的
    # setter方法的装饰器: @属性名.setter
    # getter是必须的有getter才能有setter
    @property
    def get_width(self):
        return self.hidden_width

    def get_height(self):
        return self.hidden_height

    def set_width(self, width):
        self.hidden_width = width

    def set_height(self, height):
        self.hidden_height = height

    def get_area(self):
        return self.hidden_width * self.hidden_height


# 构造器
# t1 = Rectangle(2, 5)
# 调用方法
# print(t1.get_area())

# 可以为对象的属性使用双下划线开头,_xxx
# 双下划线开头的属性,是对象的隐藏属性,隐藏属性只能在类的内部访问,无法通过对象来访问
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.hidden_age = age


p1 = Person('孙悟空', 500)
# p1.__name 通过对象读不到
# 双下划线开头的属性,是对象的隐藏属性,隐藏属性只能在类的内部访问,无法通过对象访问
# 实际是将名字修改为了,__类名__属性名 比如 __name ->__Person__name 相当于自动改名
# 使用__开头的属性,实际上依然可以可以在外部访问,所以不推荐使用 其实用了和没用是一样的
# 一般我们会将一些私有属性(不希望被外部访问的属性)以_开头
# 一般情况下,使用_开头的属性都是私有属性,没有特殊需要不要修改私有属性
