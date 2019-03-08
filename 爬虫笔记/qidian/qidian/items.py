# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QidianNovalItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 封面
    coverImage = scrapy.Field()
    #标题
    title = scrapy.Field()
    #作者
    author = scrapy.Field()
    #分类
    category = scrapy.Field()
    #状态
    status = scrapy.Field()
    #简介
    content = scrapy.Field()

def get_sql_info(tablename,dataDict):

    insertSql = """
            INSERT INTO %s (%s)
            VALUES (%s)
    """ % (
        ','.join(dataDict.keys()),
        ','.join(['%s'] * len(dataDict))
    )
    data = list(data)
