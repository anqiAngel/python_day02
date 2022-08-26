import hashlib
# ==和is的区别
# ==是比值
# is比对象地址 is更严格一点
a = 10
b = 10
# ==是比值
print(a == b)
print(a is b)

print(id(a))
print(id(b))
