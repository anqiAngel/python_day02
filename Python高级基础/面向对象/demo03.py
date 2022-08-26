import socket


class Person:

    age = 22

    def __init__(self, name):
        print('类Person初始化!!!')
        # 在实例对象里创建属性
        self.name = name

    def say(self):
        print('大家好,我是%s' % self.name)


# 目前来讲,对于Person类来说name是必须的,并且每一个对象中的name属性基本上都是不同的
# 而我们现在是将name属性在定义为对象以后,手动添加到对象中,这种方式很容易出现错误
# 我们希望,在创建对象是,必须设置name属性
# 在类中可以定义一些特殊方法(魔术方法)
# 特殊方法都是以__开头以__结尾的方法
# 特殊方法不需要我们自己调用,不要尝试去调用特殊方法
# 特殊方法方法会在特殊的时刻自动调用
# 学习特殊方法: 1.特殊方法什么时候调用 2. 调用方法又什么作用

# 创建对象的流程 1.创建一个变量 2.在内存中创建一个新变量 3. __init__(self)方法执行 4.将对象的id赋给变量
# init会在对象创建以后立即开始执行
# init可以用来向新创建的对象中初始化属性


p1 = Person('史安琪')
# p2 = Person()
# p3 = Person()
# p4 = Person()
print(p1.say())
print(p1.name)
