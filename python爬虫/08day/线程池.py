# 线程池:目的是为了方便快捷的创建线程
# 线程池中的线程不需要手动管理,我们只要需要往线程池中添加任务,线程池
# 会自动分配任务给线程执行,线程执行完毕后
# 我们可以设置回调函数,处理结果

from concurrent.futures import ThreadPoolExecutor
import time, threading


def download_data(url):
    # 让线程执行这个请求任务
    print(url, threading.currentThread().name)
    # 等待1秒模拟发起请求
    time.sleep(1)
    return 200, '请求成功', url


def download_done(futures):
    code, html, url = futures.result()
    print(code, html, url)


if __name__ == '__main__':
    # 创建线程池
    # max_workers:设置线程池中线程数(并不是越大越好)
    pool = ThreadPoolExecutor(10)
    for i in range(1, 100):
        url = 'https://www.baidu.com/' + str(i)
        result = pool.submit(download_data, url)
        result.add_done_callback(download_done)

    pool.shutdown()
    print('结果', threading.currentThread().name)
