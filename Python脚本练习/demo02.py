import os
# 脚本 = 程序
print(os.name)
# 获取cpu的数量
print(os.cpu_count())
# 获取程序运行的目录 返回绝对路径
print(os.getcwd())
# 当前目录下的文件
print(os.listdir())
# 检查读写执行权限
print(os.access('test.txt', os.X_OK))

