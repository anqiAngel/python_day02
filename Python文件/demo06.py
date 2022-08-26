# 读取模式
# t读取文本文件(默认值)
# b读取二进制文件
file_name = 'hello/文本01.txt'
with open(file_name, mode='rb') as file_obj:
    # 读取文本文件时,size是以字符为单位的
    # 读取二进制文件时,size是以字节为单位
    print(file_obj.read(100))
    # 将读取到的内容写出来
    # 定义一个新的文件
    new_name = '新名字'
    with open(new_name, mode='wb') as new_obj:
        chunk = 1024 * 100
        while True:
            if not content:
                break
            content = file_obj.read(chunk)
            new_obj.write(content)