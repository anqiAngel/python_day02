# 抛出异常
# 可以使用raise语句来抛出异常,raise语句后需要跟一个异常类 或 异常的实例
# 抛出异常的目的,告诉调用者这里调用时出现问题,希望你自己处理一下
# 也可用if ... else ...处理
# 也可以自定义异常类,只需要创建一个类继承Exception即可
class Myerror(Exception):
    pass


def add(a, b):
    if a < 0 or b < 0:
        # raise Exception('两个参数中不能有负数')
        raise Myerror('自定义的异常')
        return a + b


print(add(-100, -200))
