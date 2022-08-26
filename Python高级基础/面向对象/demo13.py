# 开箱即用
# 为了实现开箱即用的思想,Python中为我们提供了一个模块的标准库
# 在这个标准库中,有很多强大的模块我们可以直接使用
# 并且标准库会随着Python的安装一同安装
# sys模块,它里面提供了一些变量和函数,使我们可以获取到Python解析器的信息
# 或者通过函数来操作Python解析器
# 引入sys模块

import sys
import pprint

# pprint 模块它给我们提供了一个方法 pprint()该方法可以用来对打印的数据做简单的格式化
# sys.argv
# 获取执行代码时,命令行中所包含的参数
print(sys.argv)
# sys.modules
# 获取当前程序中引入的所有模块
# modules是一个字典,字典的key是模块的名字,字典的value是模块的对象
print(sys.modules)
pprint.pprint(sys.modules)
# sys.path 他是一个列表,列表中保存的是模块的搜索路径
print(sys.path)
pprint.pprint(sys.path)
# sys.platform Python程序运行的平台
# sys.exit('异常!!!')
print(sys.platform)
# os 模块让我们可以对操作系统进行访问
import os

# 通过这个属性可以获取到系统的环境变量
# os.environ
print(os)
pprint.pprint(os.environ['path'])
# os.system()
# 可以用来执行操作系统的命令cmd
os.system('dir')
os.system('notepad')
