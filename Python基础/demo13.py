import socket

# input() 函数
# 括号中可以设置一个字符串参数作为提示
# input() 调用后,程序会立即暂停,卡在那里等待用户输入
# 用户输入完之后,点击回车才会向下继续执行
# 用户输入完成之后点击回车之后,其所输入的内容以字符串形式返回

a = input('请输入一个整数:')  # 返回的是字符串str
print('用户输入的内容', a)
# input() 能暂时阻止程序结束
username = input("请输入用户名:")
if username == "admin":
    print('欢迎管理员光临!')
else:
    print('欢迎用户光临!')
age = int(input("请输入你的年龄:"))
if age >= 18:
    print('你已经成年了')
else:
    print("你还没有成年")
