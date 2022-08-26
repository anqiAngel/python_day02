import socket


# 装饰器 对函数进行扩展

# 两个数的和
def f1(a, b):
    return a + b


# 两个数的积
def f2(a, b):
    return a * b


# 对f1进行扩展 但是每次扩展都修改函数 复用性差
def f(a, b):
    print('计算开始')
    result = f1(a, b)
    print('计算结束')
    return result


# 希望函数可以在计算前,打印开始计算,计算结束后打印计算完毕
# 我们可以直接通过修改函数中的代码来完成这个需求,但是会产生以下一些问题
# 1.如果要修改的函数过多,修改起来比较麻烦
# 2.并且不方便以后的维护
# 3.并且这样做会违反我们的开闭原则(OCP)
# 程序的设计,要求开放对程序的扩展,要关闭对程序的修改
# 上边的方式,已经可以在不修改源代码的情况下对原函数进行扩展了
# 但是,这种方式要求我们每扩展一个函数就要动手创建一个新的函数,十分麻烦
# 为了解决这个问题,我们创建一个函数,让这个函数可以自动地帮助我们生产我们想要的函数
# begin_end这种函数就称它为装饰器
# 通过装饰器,可以在不修改原函数的情况下对函数进行扩展
# 再开发中,我们都是通过装饰器来扩展函数的功能
# 定义函数是,可以通过@装饰器,来使用指定的装饰器函数,来装饰当前的函数
# 可以同时为一个函数指定多个装饰器,这样函数将会按照由内到外的装饰器装饰

def begin_end(old):
    def new_function(*args, **kwargs):
        print('计算开始')
        # 调用被扩展的函数
        result = old(*args, **kwargs)
        print('计算结束')
        return result

    return new_function


@begin_end
def say_hello():
    print('大家好~~~')


if __name__ == '__main__':
    print(f(600, 10))
    print(f2(600, 10))
    f = begin_end(f2)
    r = f(123, 456)
    print(r)
    say_hello()
