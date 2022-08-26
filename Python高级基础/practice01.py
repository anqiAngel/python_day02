import socket


# 练习 1 定义一个函数,可以用来求任意三个数的乘积
# 练习 2 定义一个函数,可以根据不同的用户名显示不同的欢迎信息
def f1(a, b, c):
    return a * b * c


def f2(name):
    print(f"欢迎{name}光临!")


if __name__ == '__main__':
    value = f1(1, 2, 3)
    print(value)
    name = input('请输入一个人名:')
    f2(name)
