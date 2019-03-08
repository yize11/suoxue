from concurrent.futures import ThreadPoolExecutor


def crawlPageDate(url):
    print(url,kwargs)





if __name__ == "__main__":
    pool = ThreadPoolExecutor(max_workers=8)

    for page in range(1,57):
        # 往线程池中提交任务
        url = 'https: // www.meishij.net / chufang / diy / jiangchangcaipu /? & page =' + str(page)
        pool.submit(crawlPageDate,url)