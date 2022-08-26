import socket

# filter()函数 过滤器函数
# filter()可以从序列中过滤出符合条件的元素,保存到一个新的序列,并返回新序列 返回值为列表
# 参数: 1.函数,根据函数来过滤 序列(可迭代的结构) 2.需要过滤的序列(可迭代的结构)
# 返回值: 过滤后的新序列(可迭代的结构)
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def f(i):
    if i % 2 == 0:
        return True
    return False


# f是作为参数传递进filter()函数中
# 而f实际上只有一个作用,就是作为filter()的参数
# filter()调用完毕以后,f就已经没用

print(list(filter(f, l)))

# 匿名函数也叫 lambda函数表达式 一般函数的简化方式(语法糖) 只能写简单的函数
# 语法: lambda 参数列表 : 返回值不用写return
# 匿名函数一般都是作为参数使用,其他地方一般不会使用
f = lambda a, b: a + b
f1 = lambda i: i / 2
# (lambda a, b: a + b)(10, 20)
# 可以将匿名函数对象赋值给变量,一般不会这么做

print(f(1, 2))

# map()
# map()函数可以对迭代对象中的所有元素做指定的操作,然后将其添加到一个新的对象中返回
# 将列表l中元素均+1
r = map(lambda i: i + 1, l)
# 将列表l中均除以2
x = map(f1, l)
print(list(r))
print(list(x))
print(l[2-3])
