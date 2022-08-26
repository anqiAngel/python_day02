import socket

# 在Python中函数是一等对象
# 一等对象一般都会具有如下特点:
# 1.运行时创建
# 2.能赋值给变量或作为数据结构中的元素
# 3.能作为参数传递
# 4.能作为返回值返回

# 高阶函数
# 高阶函数至少要符合以下两个特点中的一个
# 1.接收一个或多个函数作为参数
# 2.将函数对象作为返回值返回

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 当我们使用一个函数作为参数时,实际上是将我们指定的代码传入

# 定义一个函数
# 可以将制定列表中的所有偶数,保存到一个新列表中返回
def f(func, lst):
    new_list = []
    for n in lst:
        if func(n):
            new_list.append(n)
    return new_list


def f1(n):
    if n % 2 == 0:
        return True
    return False


print(f(f1, my_list))
