import socket
# 列表对象调用方法
role = ['孙悟空', '猪八戒', '沙和尚', '唐僧', '牛魔王', '白骨精']
# 方法 s.append(x)将x插入到列表最后
# role.append('如来佛祖')
# 方法 s.insert(i, x) 将x插入到指定位置i,i后面的所有元素依次向后移
# role.insert(2, '刘备')
# 方法 s.extend(序列)等价于 s += t
# role1 = ['孙悟空', '猪八戒']
# role.extend(role1)
# 方法 s.clear()清空序列
# role.clear()
# 方法 s.pop(i)删除指定索引元素并返回删除元素,不写 i  s.pop()删除最后一个元素
# print(role.pop(0))

# 方法 s.remove(指定值)删除 当指定值的元素有多个指定值会删除第一个
# role.remove("孙悟空")
# s.reverse() 翻转s
# role.reverse()
# s.sort() 升序排序 s.sort(reverse = True) 降序排序
print(role)