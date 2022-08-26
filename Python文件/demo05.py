# 使用open()打开文件时必须要指定打开文件所要做的操作(读、写、追加) 默认是读文件 读文件是不能向文件中写入的
# r表示只读的
# w表示可写的,使用w写入文件时,如果文件不存在会创建文件,如果文件存在则会截断文件
# 截断文件表示删除文件中原来的内容
# a表示追加内容
# 如果文件不存在会创建文件,如果文件存在则会向文件中追加内容
# x用来新建文件,如果文件不存在则创建,存在则报错
# +为操作符增加功能
# r+、w+、a+
# r+即可读又可写
with open('hello/文本03.txt', mode='a', encoding='utf-8') as file_obj:
    # write()来向文件中写入内容
    # 如果操作的是一个文本文件的话,则write()需要传递一个字符串作为参数
    # 该方法会可以分多次向文件写入内容
    # 写入完成之后,该方法会返回写入字符的个数
    file_obj.write('hello\n')
    file_obj.write('hello\n')
    file_obj.write('hello\n')
    file_obj.write('hello\n')
