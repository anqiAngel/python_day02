import matplotlib as plt

# 数据类型 Python 中有整数、浮点数（小数）、复数、布尔值实际是整数 0,1
# 所有的整数都是 int 类型
# 大小无限制，动态类型任意大小
a = 10
b = 20
print(a * b)
# 当数字长度过长时用_分隔提高数字的可读性
c = 123_456_789_112
print(c)
# 二进制 0b开头 binary
# 八进制 0o开头 octal
# 十六进制 0x开头 hex
# 数字输出一定以十进制打印
d = 0b10
e = 0o10
f = 0x10
print(d)
print(e)
print(f)
# 浮点数（小数）
g = 0.1
h = 0.2
# python无法精确表达0.1只能近似值,一般用一些模块moudle来处理
print(g + h)
if g - h < 0.1:
    print('g=h')
