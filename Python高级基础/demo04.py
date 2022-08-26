import ssl


# 函数的返回值  *nums以tuple元组的形式接收
# 返回值,返回值就是函数执行以后返回的结果
# 可以直接使用函数的返回值,也可以通过一个变量来接收函数的返回值
# return 后边跟什么值,函数就会返回什么值
# return 后边可以跟任意的对象,返回值甚至也可以是一个函数
def sum(*nums):
    print(nums)
    result = 0
    for i in nums:
        result += i
    print(result)
    return result


def fn():
    # return 'Hello'
    # return [1, 2, 3]
    def fn2():
        print('hello')

    return fn2  # 返回值为一个函数对象


# 如果只写一个return或者不写return  函数的返回值就是None
# return 在函数中return后的代码不会执行,return一旦执行函数自动结束
# 执行return 函数执行结束
def fn1():
    for i in range(5):
        if i == 3:
            # break
            continue
        print(i)
    print('循环执行完毕')
# fn1函数对象
# fn1()为调用函数

if __name__ == '__main__':
    result = sum(16, 17, 18)
    print(result)
    r = fn()
    r()
    fn1()
