# 什么叫可迭代对象
# 迭代是访问集合元素的一种方式,可以使用for循环的对象都是
# 可迭代对象(list,tuple,dict,set,str)
from collections import Iterable

data = 1
print(isinstance(data, Iterable))

data = ['1', '2', '3', '4', '5']
# for i in data:
#     print(i)
# n_data = iter(data)
# print(next(n_data))
# print(next(n_data))
# print(next(n_data))


# 什么是迭代器?

# 迭代器是一个可以记住遍历位置的对象






# 什么是生成器?
# 生成器是一个特殊的迭代器,内部保留的是一段算法,一边执行一边运算
# 创建生成器的方式
def getNum(num):
    currentNum = 0
    while currentNum <num:
        currentNum += 1
        yield currentNum

# 一个方法里面一旦出现了yield关键字,那么这个方法就不再是一个方法了,这时候就是一个生成器





# 什么是协程?
# 是除了线程、进程之外实现多任务的另一种方式,协程比线程暂用的资源
# 更少,拥有cpu寄存器上下文,这样协程和协程之间任务切换就会非常快



