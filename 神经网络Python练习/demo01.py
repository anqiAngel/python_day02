import numpy as np
import matplotlib.pyplot as plt


def numpy_practice() -> None:
    list1 = [1, 2, 3]
    list2 = [2, 3, 4]
    # 创建向量或矩阵 用于运算 列表不能代表矩阵运算
    list1 = np.array(list1)
    list2 = np.array(list2)
    # 输出向量或矩阵的维数
    print(list1.shape)
    # 输出元素与列表类似
    for i in list1:
        print(i)
    print(list1, type(list1))
    print(list2, type(list2))
    # dot()矩阵乘法
    print(list1.T.dot(list2))
    print(np.dot(list1, list2))
    # 向量中对应元素直接相乘
    print(list1.T * list2)
    # 生成零矩阵
    z = np.zeros((3, 4))
    # 生成全一矩阵
    z = np.ones((3, 4),dtype=int)
    # 生成单位阵E
    z = np.eye(3)
    # 矩阵切片
    list3 = np.array([[1, 2, 3], [2, 3, 4]], dtype=float)
    print(list3)
    # 把二、三列切出来
    list4 = list3[:, 0:2]
    # 把二列切出来
    list5 = list3[:, 2]
    print(z)
    print(list4)
    print(list5)
    # 输出list3的(0,0),(0,1) (1,2)
    print(list3[[0, 0, 1], [0, 1, 2]])
    # 输出的每一个数都加10
    print(list3[[0, 0, 1], [0, 1, 2]] + 10)
    print('列求和', np.sum(list3, axis=0))
    print('行求和', np.sum(list3, axis=1))
    print('列最大值下标',np.argmax(list3, axis=0))
    print('行最大值下标',np.argmax(list3, axis=1))

def draw_practice() -> None:
    # 产生一个向量
    x = np.arange(0, 1, 0.1, dtype=float);
    # z = np.arange(0, 10, 0.1, dtype=float);
    print(x)
    # print(z)
    y1 = np.sin(x)
    y2 = np.cos(x)
    plt.plot(x, y1)
    plt.plot(x, y2)
    # 最后show()两条曲线会出现在同一个框中
    plt.show()


def main() -> int:
    print("hello")
    numpy_practice()
    draw_practice()
    return 1 + 1;


if __name__ == '__main__':
    a = main()
    print(a)
