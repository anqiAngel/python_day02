import socket

# i = 0
# j = 0
# 外层循环控制高度
# 内层循环控制宽度
# while i < 6:
#     while j < i:
#         print('*' * i)
#         j += 1
#     i += 1
# 练习1 打印99乘法表
# i = 0
# print(" ", "99乘法表",end="")
# while i < 10:
#     j = 0
#     while j < i:
#         j += 1
#         # end=""不进行换行
#         print(" ", j, "*", i, "=", i*j, end="")
#     print()
#     i += 1
# 练习2 打印1-10所有质数
i = 1
while i < 11:
    j = 2
    flag = True
    while j < i:
        if i % j == 0:
            flag = False
        j += 1
    if flag:
        print(i)
    i += 1
