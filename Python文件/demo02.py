# 打开文件
file_name = 'hello/文本01.txt'
# 调用open()来打开文件
# 当我们获取了文件的对象后,所有的对文件
file_obj = open(file_name, encoding='utf-8')
content = file_obj.read()
print(content)
# 关闭文件
# 调用close()文件来关闭文件
file_obj.close()

# with ... as 语句
# 在with语句中可以直接使用file_obj来做文件操作
# 此时这个文件只能with中使用,一旦with结束则文件会自动close()
file_name = 'hello'
try:
    with open(file_name, encoding='utf-8') as f:
        content = f.read()
except (FileNotFoundError, PermissionError):
    print('hello文件不存在')

# print(content)
