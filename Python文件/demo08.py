import os

# os.listdir()获取指定目录的目录结构
# 需要一个路径作为参数,会获取到该路径下的目录结构,默认路径为,当前目录
# 该方法会返回一个列表,目录中的每一个文件(夹)的名字都是列表
print(os.listdir('..'))
# os.getcwd() 获取当前所在的目录
print(os.getcwd())
# os.chdir() 切换当前目录
os.chdir('c:/')
# os.mkdir('aaa') 创建目录 在当前目录下创建一个名字为aaa的目录
# os.rmdir('abc') 删除目录
# os.remove('aa.txt') 删除文件
# os.rename(旧名字, 新名字) 给文件改名 也可以用来剪切一个文件