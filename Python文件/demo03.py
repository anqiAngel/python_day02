import socket

# 一次性读取堆内存消耗比较大 最好分块读取
file_name = 'hello/文本02.txt'
try:
    with open(file_name, encoding='utf-8') as obj:
        # 通过read()来读取文件中的内容
        # 调用open()来打开一个文件,可以将文件分为两种类型
        # 一种,是纯文本文件(使用utf-8等编码编写的文本文件)
        # 一种,是二进制文件(图片、mp3、ppt等这些文件)
        # open()打开文件时,默认是以文本文件的形式打开的,但是open()默认的编码是None
        # 所以处理文本文件时,必须要指定文件的编码
        # 如果直接调用read()它会将文本文件的所有内容都
        # 如果要读取的文件较大的话,会一次性将文件的内容加载到内存中,容易内存泄漏
        # 所以对于较大的文件,不要直接调用read()
        # help(file_obj.read)
        # read()可以接收一个size作为参数,该参数用来指定要读取的字符的数量
        # content = obj.read()
        # 默认值为-1,他会读取文件中的所有字符
        # 可以为size指定一个值,这样read()会读取指定数量的字符
        # 每一次读取都是从我们上次读取到的位置开始读取的
        # 如果字符的数量小于size,则会读取剩余所有的
        # 如果已经读取到文件的最后了,则会返回''
        # 读取大文件的方式
        # 定义一个变量,来保存文件的内容
        file_content = ''
        # content = obj.read(6)
        # content = obj.read(5)
        # print(content)
        # print(len(content))
        chunk = 100
        # 创建一个循环来读取文件内容
        while True:
            # 读取chunk大小的内容
            content = obj.read(chunk)
            file_content = file_content + content
            # 检查是否读取到了内容
            if not content:
                break
            # print(content, end='')
            print(file_content)

except FileNotFoundError:
    print('文件不存在~')
