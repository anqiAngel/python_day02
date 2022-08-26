class Dog:
    """
    表示狗的类
    """

    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    def m1(self):
        print('汪汪叫')

    def m2(self):
        print('我咬你')

    def m3(self):
        print('%s快乐的奔跑着' % self.name)


d = Dog('旺财', 12, 'male', 30)
d.m1()
d.m2()
d.m3()
print(d.name, d.age, d.gender, d.height)

# 对象中的属性可以随意修改不论对错

