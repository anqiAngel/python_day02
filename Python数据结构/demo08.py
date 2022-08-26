import future

# 元组 tuple
# 元组是一个不可变的序列 导致序列改变的方法都不可以使用
# 它的操作方法与列表基本一致
# 一般希望数据不改变时用元组，改变时用列表
# 创建元组
# 使用小括号来创建元组

my_tuple = ()
print(type(my_tuple))
my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))
# 不支持改变
# 用索引取值
print(my_tuple[0])
# 当元组不是空元组时括号可以省略 元组中至少有一个,
my_tuple = 1, 2, 3

# 元组解包解构(解包) 将元组值依次赋给 a,b,c
a, b, c = my_tuple
print(my_tuple)
print(a)
print(b)
print(c)
# 交换 a,b 的值
a = 100
b = 200
a, b = b, a
print(a, b)

# 在对一个元组解包时,变量的数量必须和元组中的元素数量一致
# 可以在一个变量前面加一个 * 获取所有剩余变量返回一个列表 不能写多个带星号的变量
# 任何序列都可以解包
my_tuple = 10, 20, 30, 40
a, b, *c = my_tuple
a, *b, c = my_tuple
print(c)
print(b)
