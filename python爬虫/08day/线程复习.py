# 线程是为了实现多任务
# 线程是依赖于进程存在的,并且一个进程下,可以有多个线程
# 线程共享进程的资源,在python中多线程是并发进行的,GIL(全局解释器锁),所以同以时刻只有一个线程被执行
# 线程多用于处理I/O密集型操作(文件读写操作,网络I/O)

import threading


def add_data(num, ):
    global data_list
    for i in range(0, num):
        data_list.append(i)


# target=None,设置线程要执行的目标函数
# name=None, 线程名称
# args =(),目标函数需要的参数
# kwargs=None目标函数需要的参数
# daemon=None,(设置前台和后台线程)

if __name__ == '__main__':
    thread1 = threading.Thread(
        target=add_data,
        args=(100,),
        kwargs={'name': '张三'},
        name='嫦娥一号'
    )
