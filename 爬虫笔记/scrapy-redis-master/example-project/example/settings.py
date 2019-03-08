# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'

# 表示使用scrapy_redis自定义的调度器组件

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 允许暂停,redis数据库中的保存的任务不会被清空,可以恢复暂停
# (断点爬取)
SCHEDULER_PERSIST = True
# 调度器存储request队列的模式(三种)
# SpiderPrityQueue:是scrapy_redis框架(默认)的请求队列形式
# 有自己的优先级,按照redis数据库中的有序集合的方式取
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# SpiderQueu:请求队列形式,按照先进先出的方式
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# SpiderStack:请求队列形式,按照先进后出的方式
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,
    # RedisPipeline:将爬虫文件获取到数据统一存放至redis数据库中
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

# 设置log日志等级
LOG_LEVEL = 'DEBUG'
# Introduce an artifical delay to make use of parallelism crawl
# 设置下载延时
DOWNLOAD_DELAY = 1

# 指定要存储数据的redis数据库的hsot(ip)
REDIS_HOST = '127.0.0.1'

# 指定要存储数据的redis数据库

LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 1
