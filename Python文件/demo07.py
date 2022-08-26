with open('hello/文本02.txt','rb') as file_obj:
    print(file_obj.read(10))
    # tell()方法用来查看当前阅读的位置
    # seek()方法用来修改当前读取的位置 有两个参数
    # 1.是要切换的参数
    # 2.计算位置方式
    # 可选值
    # 0从头计算,默认值
    # 1从当前位置计算
    # 2从最后位置开始计算

    print('当前读取到-->', file_obj.tell())