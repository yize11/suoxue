# 使用进程可以充分了用cpu资源,是,cpu分配资源的基本单元
# 每一个进程都有自己的内存空间,同样是无须执行,进程之间
# 资源不共享,多用进程处理计算密集型任务,进程可以实现并行的操作

# 并发:同时发起,但是不是同时执行,交替执行
# 并行:同时发起,同时执行
# multiprocessing并不是python自带的,是跨平台一个库
# 只是集成进来,提供给我们使用
from multiprocessing import Process,Queue

data_list = []


def add_data(num, **kwargs):
    print(num, kwargs)
    global data_list
    for i in range(0, num):
        data_list.append(i)


if __name__ == '__main__':

    # 使用multiprocessing的Queue实现数据的共享(传递)

    data_queue = Queue()


    process1 = Process(
        target=add_data, args=(100,), kwargs={'name': '进程1号'}
    )

    # 执行
    process1.start()
    # join设置进程阻塞,确保子进程中的任务执行完
    process1.join(timeout=10)
    # print(data_list)
 