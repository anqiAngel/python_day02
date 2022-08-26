import socket


# 封装是面向对象的三大特性之一
# 封装指的是隐藏对象中一些不希望被外部所访问的属性或方法
# 如何隐藏对象中的属性 ?
# 将对象的属性名,修改为一个外部不知道的名字  self.hidden_name = name
# 如何获取(修改)对象中的属性 需要提供一个getter和setter方法
# getter 获取对象中的指定属性(get_属性名)
# setter 用来设置对象的属性 没有返回值
# 确实比较麻烦,但是增加了数据的安全性
# 隐藏了属性名,使调用者无法随意的修改对象中的属性
# 增加了getter和setter方法,很好的控制对象的属性是否是只读的
# 如果希望属性是只读的,则可以直接去掉setter方法
# 如果希望属性不能被外部访问,则可以直接去掉getter方法
# 使用setter方法设置属性,可以增加数据的验证,确保数据的值是正确的
# 使用getter方法获取属性,使用setter方法设置属性
# 可以在读取属性和修改属性的同时做一些其他的处理

class Dog:

    def __init__(self, name, age):
        self.hidden_name = name
        self.hidden_age = age

    def say_hello(self):
        print('大家好,我是 %s' % self.hidden_name)

    # get和set方法
    def get_name(self):
        return self.hidden_name

    def set_name(self, name):
        self.hidden_name = name

    def set_age(self, age):
        if age > 0:
            self.hidden_age = age
