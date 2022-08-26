import msilib

# 三元运算符或三目运算符
# 语法:语句 1 if 条件表达式 else 语句 2
# 条件表达式为True执行语句 1 为False执行语句 2 并返回执行结果

print('我是你爸爸') if True else print('我是你妈妈')
print('我是你爸爸') if False else print('我是你妈妈')
a = 10
b = 20
c = 30
print('a比b大') if a > b else print('b比a大')
# 以下显然不是求最大值正确的求法
max = a if a > b else b
print(max)
max = max if max > c else c
print(max)
max = a if a > b and a > c else b if b > c else c  # 不推荐
print(max)
# 运算符的优先级
# 与的优先级比或的高 表格越靠下的运算符优先级越高 上网查找运算符的优先级 同样优先级从左到右依次
# 为了提高运算符优先级套括号
# 关系运算符可以连着使用 1<5>6
# 比较运算符比较返回bool值
result = 1 < 2 < 3  # 相当于 1 < 2 and 2 < 3
print(result)
result = 1 < 5 > 3  # 相当于 1 < 5 and 3 < 5
print(result)
