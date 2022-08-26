import html

# if-elif-else 多个判断条件表达式
# if 条件表达式:
# 代码块
# elif 条件表达式:
# 代码块
# elif 条件表达式:
# 代码块
# ...
# else:
# 代码块
# 执行流程:
# 会自上向下依次对条件表达式进行求值判断
# 如果表达式的结果为 True,则执行当前代码块,然后语句结束
# 如果表达式的结果为 False,则继续向下判断,直到找到 True为止
# else 可以省略

# 获取一个年龄信息
age = int(input("请输入年龄:"))
if age >= 18:
    print("你成年了!")
elif age >= 30:
    print("你该结婚了!")
else:
    print("没事")


