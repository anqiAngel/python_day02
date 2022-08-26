import numpy
# 水仙花数
# 水仙花数指的是各位的3次方之和为原3位数的数
# 获取一个3位数
# 判断这个数是否为水仙花数
# i = 100
# while i < 1000:
#     a b c 为百、十、个位
#     a = i // 100  # 获取百位数字
#     b = (i // 10) % 10  # 获取十位数字
#     c = i % 10 # 获取个位数字
#     if a ** 3 + b ** 3 + c ** 3 == i:
#         print(i)
#     i += 1
# 判断是否质数
# 质数只能被 1和本身 整除
# 只需判断是否能被2- 本身-1的数整除能就不是质数
num = int(input("请输入一个100以内的整数:"))
i = 2
flag = True
while i < num:
    if num % i == 0:
        flag = False
    i += 1

if flag:
    print("num是质数")
else:
    print('num不是质数')

