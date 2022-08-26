import socket

# 布尔值 boolean python中为 bool 主要用于逻辑判断 真或假 true 或 false 实际上也是整型 True为 1、False为 0
a = False
b = True
print(a)
print(b)
# 运算就将 bool 转换为整数值
print(a + b)
# 布尔值实际上也属于整型 ，Ture相当于1，False相当于0
print(1 + False)
print(1 + True)
# None(空值)专门表示不存在
b = None
print(b)
# 类型检查
a = 123
b = '123'
# b = 'abc'
# 正确的值才能转字符串。不是整数值不能转
b = int(b)
print(a)
print(b, type(b))
c = type(a)
d = type(b)
print(c)
print(d)
