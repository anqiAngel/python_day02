import hmac
# 字典的基本操作
# 删除,可以使用 del 来删除字典中的键值对 key-value
d = {'name': '孙悟空', 'age': 500, 'sex': '男'}
# del d['name']
# print(d)
# popitem()方法 随机删除字典中的一个键值对,一般都会删除最后一个键值对
# 删除之后,会将删除的键值对作为返回值返回
# d.popitem()
# print(d)
# pop(key[,default])
# 根据 key 删除字典中的 key-value
# 会将被删除的 value 返回
# 如果删除不存在的 key,会抛出异常
# 如果指定了默认值,在删除不存在的key时,不会报错,而是直接返回默认值
# result = d.pop('z', '默认值')
# print(result)

# 清空字典
# d.clear()
# print(d)
# 字典的浅复制
# 浅复制只会简单的复制对象内部的值,内部的可变对象不会被复制
# 复制之后与原对象相互独立修改一个不会影响另一个
# 字典的浅复制
# d1 = d.copy()
# print(d1)
