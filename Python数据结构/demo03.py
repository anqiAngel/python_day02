import html

# 创建列表
my_list = ['孙悟空', '猪八戒', '沙和尚', '沙和尚', '白骨精']
# + 和 *
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# + 按顺序合并
print(list1 + list2)
print(list2 + list1)
# * 复制列表
print(list1 * 2)
print(list2 * 2)
# in 和 not in 判断指定元素是否在或不在列表中,并返回 True 或 False
# in 在就返回True 不在就返回False
print('孙悟空' in my_list)
print('牛魔王' in my_list)
# len()获取列表的长度即元素的个数
# min()获取列表中的最小值
# max()获取列表中的最大值
print(min(list1), max(list1))
# 两个(method) 方法和函数基本上是一样,只不过方法必须通过 对象.方法()的形式的调用
# xxx.print() 方法实际上就是和对象关系紧密的函数
# s.index() 获取列表索引
# index() 的第二个参数为起始位置,第三个参数为结束位置不包括结束位
# s.count(value) 指定元素出现了几次
print(my_list.count('白骨精'))
print(my_list.index('白骨精'))


