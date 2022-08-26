my_list = []
for i in range(4):
    num = int(input("请输入:"))
    my_list.append(num)
for i in range(4):
    my_list[i] = (my_list[i] + 3) % 9
temp = my_list[0]
my_list[0] = my_list[2]
my_list[2] = temp
print(my_list)