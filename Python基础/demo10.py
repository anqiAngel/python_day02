import socket

# 非 not、与 and、或 or  与、或、非
# 对非布尔值 not运算会先将其转换为布尔值,表示空的均为 False  1->True,""->False
# Python中的与运算是短路的与运算,第一个值为 False,之后不再看表达式一定为 False。
# 或反之

a = True
b = not a
c = a and b
d = a or b

print(a)
print(b)
print(c)
print(d)

False and print('你的父亲')  # 不输出
True and print('你的父亲')
False or print('你的父亲')
True or print('你的父亲')  # 不输出

# 非布尔值与或运算
# 当做布尔值运算返回原值
# 与找 False返回第一个 False的原值,或找 True返回第一个 True的原值
print(0 or 1)  # 1
print(0 and 1)  # 0



