import socket


# Python 执行时是按照自上到下一行一行的顺序执行的
# 通过流程控制语句可以改变程序的执行顺序,也可以让指定的程序反复执行多次
# if 判断语句 分支语句 for while do while循环语句
# if 执行顺序 条件表达式 True执行 False不执行
# 默认情况下 if只会控制紧随其后的那条语句
# 代码块一组代码 同一代码块中的代码要么都执行,要么都不执行
# Python中 Tab、空格不能混用

# print('请输入一个整数:')
# a = int(input())
# if a == 1:
#     print('我是你爸爸')
#     print('拜拜')
# else:
#     print('我是你妈妈')
# num = 18
# if 10 < num < 20:
#     print('num比10大比20小')

def f1(x):
    return x ** 2


# lambda表达式简化简单函数和数学函数的书写
f = lambda x: x ** 2

if __name__ == '__main__':
    print(f1(5))
    print(f(10))
