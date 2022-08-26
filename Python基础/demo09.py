import html

# 比较运算(关系运算符)用来比较两个值之间的关系，总会返回一个布尔值返回 True 或 False
# 如果关系成立,返回 True,否则返回 False
# >,>=,<,<=,==,!=
# == 比较两个对象的值是否相等，相等返回True，不相等返回False
# != 比较两个对象的值是否值不相等，不相等等返回True，相等返回False
# 比较对象是否相等 is,is not比较的是id CPython中的id是内存地址

result = 10 > 20  # False

result = 30 > 20  # True

result = 2 >= 1   # True

# 在Python中可以对两个字符串进行大于等于或小于等于运算
# 当对字符串进行比较时,实际上比较的是字符串中字符的Unicode编码值 逐个字符进行比较 Unicode编码值
result = '2' > '10'
# 逐位比前一位没比出来再来比后一位 2 > 1 应用:用来将单词按字母进行排序

print("result =", result)
print("\u2505")
