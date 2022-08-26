# 特殊方法,也称魔术方法
# 主要是在特定的时间 完成特定的功能
# 特殊方法都是使用__开头和结尾的
# 特殊方法一般不需要我们手动调用,需要在一些特殊情况下自动执行
# 当我们打印一个对象时,实际上打印的是对象中的特殊方法__str__()的返回值
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__()这个特殊方法会在尝试将对象转换为字符串的时候调用
    # 它的作用可以用来指定对象转换为字符串的结果
    def __str__(self):
        return 'Person [name=%s,age=%s]' % (self.name, self.age)

    # __repr__()这个特殊方法会在对当前对象使用repr()函数时调用
    # 它的作用是指定对象在 '交互模式' IDLE中直接输出效果
    def __repr__(self):
        return 'hello'

    # __gt__会在对象做大于比较的时候,该方法的返回值将会作为比较的结果
    # 他需要两个参数,一个self表示当前对象,other表示和当前对象比较的对象
    # self > other

    # __len__()获取对象的长度
    # __bool__() 可以通过bool来指定对象转换为布尔值的情况
    def __gt__(self, other):
        return self.age > other.age

    def __bool__(self):
        return False


p1 = Person('孙悟空', 18)
p2 = Person('猪八戒', 28)

print(p1)
print(p2)
print(p1 > p2)
print(p2 > p1)
print(bool(p1))
