import math

# 字符串相关处理
# 格式化字符串 Python3独有的
s = '史安琪'
print(f'我叫{s}')
a = 'HELLO'
# 拼接字符串 两个字符串之间用 + 连接在一起形成新的字符串
print("a = " + a)
# 第一种不常用
# 下面几种常用
# 1.print传参 print(a,b,c) 输出 "a b c"
# 2.在创建字符串时，可以在字符中指定占位符用 %s占位 然后 % 用之后的字符串填充占位，%3s指定字符串字符数为3 不够用空格补全 %3.5s 3—5个字符的字符串
# 3.Python3独有的格式化字符串，可以在字符串前添加一个 f 来创建格式化字符串 {a}用对应变量替换
# %d整数占位符，%f浮点数占位符，%s在字符串中表示任意位字符
# print()方法传参
print("a =", a)
# %s占位用 %后面的字符串补全
d = "hello%3s" % '八戒'
e = "hello%f" % 123.4
b = "hello%s" % '猪八戒'
c = 'hello %s hello %s' % ('史安琪', '呵呵')
# 格式化字符串
f = f'hello{a}{b}'
print(d)
print(b)
print(c)
print(c)
print(e)
print(f)
# 练习用四种方法输出:欢迎史安琪光临!
name = '史安琪'
# 拼串
str1 = '欢迎 ' + name + ' 光临!'
print(str1)
# 多个参数
print('欢迎',name,'光临!')
# 占位符
str3 = '欢迎 %s 光临!' % '史安琪'
print(str3)
# 格式化字符串
str4 = f'欢迎 {name} 光临!'
print(str4)
# 字符串复制直接写乘号 乘几复制几次 20次abc
g = 'abc'
g = g * 20
print(g)
