# 异常 程序在运行过程当中,不可避免的会出现一些错误,比如:
# 1.使用了没有赋值过的变量
# 2.使用了不存在的索引
# 除0等等
# 这些程序的报错。我们称其为异常。
# 程序运行过程中,一旦出现异常将会导致程序立即停止,异常以后的代码全部都不会执行

# 处理异常
# 程序运行时出现异常,目的并不是让我们的程序直接终止!
# Python是希望在出现异常时,我们可以编写代码对异常进行处理!

# 代码中有可能出现异常的地方,我们要进行处理
# 可能出现异常的语句要试一下
# try语句
# 语法 try: 代码块(可能出现错误的语句)
# except 异常类型 as 异常名:代码块(出现错误以后的处理方式)
# except 异常类型 as 异常名:代码块(出现错误以后的处理方式)
# except 异常类型 as 异常名:代码块(出现错误以后的处理方式)
# else: 代码块(没有错误时要执行的语句)
# finally: 无论如何必须执行的代码
# try必须有 else有没有都行
# expect和finally至少有一个

print('异常处理')
try:
    # try中放置的是有可能出错的语句
    print(10 / 2)
except:
    # 出现错误以后的处理方式
    print('语句出错了')
else:
    print('没有错误')


# 可以将可能出错的代码放入到try语句中,这样如果代码没有错误,则会正常执行
# 如果出现错误,则会执行expect子句中的代码,这样我们就可以通过代码来处理异常
# 避免因为一个异常导致整个程序的终止

# 异常的传播(抛出异常)
# 当在函数中出现异常时,如果在函数中对异常进行了处理,则异常不会再继续传播
# 如果函数中没有对异常进行处理,则异常会继续向函数调用处传播
# 如果函数调用处处理了异常,则不传播,如果没有处理则继续向调用处传播
# 直到传递到全局作用域(主模块)如果,则程序终止,并且显示异常信息
# 当程序运行过程中出现异常以后,所有的异常信息会被保存到一个异常对象中,而异常传播时,实际上就是异常对象抛给了调用处
# 比如: ZeroDivisionError表示除 0 异常  NameError类的对象专门用来处理变量相关异常 ...
# 在Python中为我们提供了多种异常

def fn():
    print('Hello fn')
    print(10 / 0)


def fn2():
    print('Hello fn2')
    fn()


def fn3():
    print('Hello fn3')
    fn2()


fn3()
