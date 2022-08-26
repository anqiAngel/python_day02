import socket

# EMS员工管理系统 命令行版的员工管理系统
# 具体需要实现的功能如下:
# 1.查询系统中的人员信息
# 2.添加系统中的人员信息
# 3.删除系统中的人员信息
# 4.退出
# 欢迎信息
print('-' * 20, '欢迎使用员工管理系统', '-' * 20)
# 要做的操作
my_list = ['孙悟空\t\t500\t\t男\t\t花果山水帘洞', '猪八戒\t\t500\t\t男\t\t高老庄']
while True:
    print('\t1.查询员工')
    print('\t2.添加员工')
    print('\t3.删除员工')
    print('\t4.退出')
    print("-" * 62)
    user_choose = int(input('请输入一个[1-4]的选项:'))
    if user_choose == 1:
        # 查询员工
        print('序号\t\t姓名\t\t年龄\t\t性别\t\t住址')
        n = 1
        for emp in my_list:
            print(f'{n}\t\t{emp}')
            n += 1
        pass
    elif user_choose == 2:
        # 添加员工
        ems_name = input('请输入人员的姓名:')
        ems_age = input('请输入人员的年龄:')
        ems_gender = input('请输入人员的性别:')
        ems_address = input('请输入人员的住址:')
        # 显示一个提示信息
        emp = f'{ems_name}\t\t{ems_age}\t\t{ems_age}\t\t{ems_address}'
        choice = input('员工:'+emp+'将会被添加到系统中，是否确认该操作[Y/N]')
        if choice == 'Y':
            my_list.append(emp)
            print('插入成功')
        else:
            pass
            print('插入已取消')
    elif user_choose == 3:
        # 删除员工 根据序号删除元素
        del_num = int(input('请输入要删除员工的序号:'))
        if 1 <= del_num <= len(my_list):
            del_index = del_num - 1
            print('以下员工将被删除')
            print(f'{del_num}\t\t{my_list[del_index]}')
            my_list.pop(del_index)
        else:
            print('您的输入有误请重新操作!')
    elif user_choose == 4:
        print('欢迎使用!再见!')
        print('点击回车退出!')
        break
    else:
        print('输入有误请重新输入选项!')
        pass
    print("-" * 62)