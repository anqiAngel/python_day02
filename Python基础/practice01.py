import math


def f1():
    a = input("请输入账号:")
    b = input("请输入密码:")
    return a, b


if __name__ == '__main__':
    a, b = f1()
    a = int(a)
    b = int(b)
    ID = 123456
    PWD = 111111
    if a == ID and b == PWD:
        print("账号密码正确,登录成功!")
    else:
        print("登录失败!")
