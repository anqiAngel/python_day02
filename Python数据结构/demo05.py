from time import *

# 列表练习
role = ['孙悟空', '猪八戒', '沙和尚', '唐僧', '牛魔王', '白骨精']
# 修改
# role[0] = 'sunwukong'
# role[1] = 'zhubajie'
# print(role)
# 删除
# del role[0]
# print(role)
role = ['孙悟空', '猪八戒', '沙和尚', '唐僧', '牛魔王', '白骨精']
# 通过切片修改列表
# 在给切片赋值时只能赋序列 切片是一个片段
# role[0:2] = ['shianqi', 'anqishi']
# print(role)
# 向索引0插入新元素
# role[0:0] = ['史安琪']
# print(role)
# 当设置了步长时,序列中元素的个数必须和切片中元素个数一致
# 通过切片删除元素 删除一段元素
# del role[0:2]
# print(role)
# 隔两个删除
# del role[::2]
# role[1:3] = []
# print(role)
name = '史安琪'
# list()将不可变变量转换为列表
name = list(name)
print(name)