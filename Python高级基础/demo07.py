import socket


# 递归 函数自己调用自己
# 求10的阶乘 10!
# 递归的两个要素
# 1.递归出口
# 2.递归表达式
# 递归是解决问题的一种方式,它和循环很像
# 它的整体思想是,将一个大问题分解为一个个的小问题,直到问题无法分解时,再去解决问题

def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n-1)


if __name__ == '__main__':
    print(f(10))
