# 对象 (object) 面向对象 oo
# Python是一门面向对象的语言
# 程序运行时的数据都存储在内存中
# 每个对象就是都是容器 专门存储数据
# 对象是内存中的一块空间
# 每个对象的结构 3种数据 1.id 2.type 3.value
# id通过id()函数查看对象的id,id由解释器分配即内存地址,在CPython中id就是对象的内存地址,对象一旦创建id永远不变
# type用来标识对象所属的类型,比如 int、bool、str、float,类型决定对象有哪些功能。Python强类型一旦创建永远不变
# value对象中具体的数据,值可变
# 对象类型:可变对象、不可变对象
# 变量相当于对象的别名指向对象的指针
# 对象类型的转换 类型转换将一个类型的对象转换为其他类型对象
# 类型转换不是转换对象本身的类型,而是转换对象值的类型 函数:int()、float()、str()、bool()
# int()函数不会对原来的变量产生影响,他是将对象的值转换为指定类型并作为返回值返回
# 合法的整数字符串,直接转换为对应的数字,如果不合法报错
# 如需修改原来的变量重新进行赋值
a = '123'
a = int(a)
b = 123 + a
c = 11.25
c = int(c)
d = 11
d = float(11)
e = False
e = float(e)
print(b)
print(c)
print(d)
print(e)
print('hello' + str(11.25))
# bool 任何对象都可转换为bool值 None->False 0->False 空性就是 False 其他是True
print(bool(11))
print(bool(0))


