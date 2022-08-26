import socket

# 创建一个 int对象
a = int(10)
print(a, type(a))
# 创建一个 str对象
b = str('你好')
print(b)


# 定义一个简单的类
# 使用class关键字来定义类,语法和函数很想
# 语法 class 类名([该类继承的父类]):
# 代码块(包括一些属性和一些方法)
class MyClass():
    pass


print(MyClass)
# 使用MyClass创建一个对象
# mc就是通过MyClass类创建的对象
mc = MyClass()  # 使用类来创建对象,就像调用函数一样
# 检查是不是实例
print(isinstance(mc, MyClass))
print(mc)
