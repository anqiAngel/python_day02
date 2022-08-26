import numpy


# 闭包:只有内部可以看见的数据 外部看不见内部 通过闭包可以创建当前函数可以访问的变量 确保数据安全
# 形成闭包的要件 1.函数嵌套 2.将内部函数对象作为返回值返回 3.内部函数要使用外部函数的变量
# 可以将一些私有的数据藏在这个闭包中
# 将函数做为返回值返回,也是一种高阶函数
# def f():
#     # 函数内部再定义一个函数
#     # 这个函数可以访问到函数内部的变量
#     def inner():
#         print('我是内部函数')
#     return inner
#
#
# r = f()
# r()

# 求多个数的平均值
# nums = [50, 30, 20, 10, 70]
# print(sum(nums)/len(nums))

# 闭包例子 1.函数嵌套 2.将函数对象作为返回值返回 3.内部函数使用外部函数的变量
def make_avg():
    nums = []

    def avg(n):
        # 将n添加到列表中
        nums.append(n)
        # 求平均值
        return sum(nums) / len(nums)

    return avg


avg = make_avg()

print(avg(10))
print(avg(20))
print(avg(30))
