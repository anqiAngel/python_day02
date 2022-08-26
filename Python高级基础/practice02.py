import socket


# 递归练习
# 1.创建一个函数 power 来为任意数字做幂运算 n**i
# 1.递归跳出条件
# 2.递归表达式
def power(n, i):
    if i == 1:
        return n
    else:
        return n * power(n, i - 1)


# 2.创建一个函数,用来检查一个任意的字符串是否是回文字符串,如果是返回True,如果不是返回False
# 回文字符串,字符串从前往后和从后往前念是一样的
# abcba
# 先看两侧是否一样 一样就递归地看中间是否为回文串,不一样就返回False
def hui_wen(s: str) -> bool:
    if len(s) < 2:
        return True
    elif s[0] != s[-1]:
        return False
    return hui_wen(s[1:-1])


if __name__ == '__main__':
    print(power(8, 6))
    print(hui_wen('hello'))
