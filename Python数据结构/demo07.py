import ctypes

# 遍历列表 就是将列表中的所有元素取出来
role = ['孙悟空', '猪八戒', '沙和尚', '唐僧', '牛魔王', '白骨精']

# i = 0
# while i < len(role) :
#     print(role[i])
#     i += 1
# for遍历序列
# 一般用来遍历序列
# 语法: for 变量 in 序列 : 代码块
# 代码块执行次数 序列中的元素个数
# 循环执行一次将一个元素赋给变量
# for i in role:
#     print(i)

# 生成 0-8 的自然数序列
# r = range(0,9)
# 该函数需要 3个参数 1.起始位置(可以省略,默认是0) 2.结束位置(不包括结束位置) 3.步长(可以省略,默认是 1)
# r = range(10)
# r = range(3,10)
# r = range(0,10,2)
# for循环遍历 range 创建执行指定次数的 for循环、
# 循环10次
# for i in range(10):
#     print(i)
# for i in range(0, 10, 2):
#     print(i)
