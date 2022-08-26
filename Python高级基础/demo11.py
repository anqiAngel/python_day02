import numpy

# sort() 方法的参数只能是列表
# 该方法用来对列表中的元素进行排序
# sort()方法默认是直接比较列表中元素的大小
# 在 sort()可以接收一个关键字参数,key
# key需要一个函数作为参数,当设置了函数作为参数 解释器就会用这个函数进行分类
# 每次都会以列表中的一个元素作为参数来调用函数,并且使用函数的返回值来比较元素的大小
my_list = ['bb', 'aaaa', 'c', 'dddddddd', 'ffffff']

# my_list.sort()
# print(my_list)
# 用长度去比较
my_list.sort(key=len)
# 转换为 int型去比较
# my_list.sort(key=int)
# sorted()函数 这个函数和sort()的用法基本一致。但是sorted()可以对任意序列进行排序
# 并且使用sorted()排序不会影响原来的对象,而是返回一个新的对象
print(my_list)
# sorted(my_list, key=int)

