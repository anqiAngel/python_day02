print('异常出现前')
l = []
try:
    # print(c)
    print(l[10])
    print(10 / 0)
except NameError:
    # 如果except后不跟任何的内容,则此时它会捕获到所有的内容
    # 如果在except后跟着一个异常的类型,那么此时他只会捕获该类型的异常
    # 只写except: 相当于异常名处写了一个Exception Exception是所有异常的父类,所以如果except后跟的是Exception,他也会捕获到所有的异常
    # 可以在异常类后边跟着一个 as xx 此时xx就是异常对象
    print('出现NameError异常')
except ZeroDivisionError:
    print('出现ZeroDivisionError异常')
except Exception as e:
    print('未知异常')
    print(e)
    print(type(e))
finally:
    print('无论是否异常该子句都会执行')
print('异常出现后')
