import html
from time import *
# break、continue
# break 可以用来立刻跳出循环语句,包括 else,用来结束没有必要的循环
# continue 可以用来跳过本次次循环
# pass 只是用来占位
# while 后也可以加else:  while的条件为False时else后的代码执行一次
# i = 0
# while i < 5:
#     if i == 2:
#         break
#     print(i)
#     i += 1
# else:
#     print('循环结束')
i = 0
while i < 5:
    i += 1
    if i == 2:
        continue
    print(i)
else:
    print('循环结束')
# 返回值单位秒
print(time())