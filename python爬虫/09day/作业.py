from selenium import webdriver
import time
import requests
from lxml import etree


class DouBan(object):

    def __init__(self):
        # 创建浏览器驱动
        self.brower = webdriver.Chrome(
            executable_path='/home/yize/下载/chromedriver'
        )
        # 使用get方法打开页面
        self.brower.get('https://movie.douban.com/')
        self.brower.find_element_by_id('inp-query').send_keys('驯龙高手3')
        self.brower.find_element_by_class_name('inp-btn').click()
        print('搜索成功')
        self.get_live_data(self.brower.page_source)

        time.sleep(1)
        self.brower.find_element_by_id('inp-query').clear()
        self.brower.find_element_by_id('inp-query').send_keys('成龙')
        self.brower.find_element_by_class_name('inp-btn').click()

    def get_live_data(self):
        # x_html = etree.HTML(html_Data)
        li_list = self.brower.find_elements_by_xpath('//div[@class="item-root"]')
        print(len(li_list))
        # 遍历
        # for li in li_list:
        #     book_info = {}
        #     # 封面图片
        #     book_info['coverImage'] = 'https:' + li.xpath('./div[@class="item-root"]//img/@src')[0]
        #     print(book_info)


if __name__ == '__main__':
    spider = DouBan()
