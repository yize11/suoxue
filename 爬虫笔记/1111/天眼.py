import requests
from lxml import etree


class TianYanSpider():
    def __init__(self):
        pass

    def start_request(self, url):
        headers = {
            'User-Agent': 'Mozilla / 5.0(X11;Linuxx86_64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 71.0.3578.98Safari / 537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print('成功')
            str = response.content
            start_url = str.decode('utf-8')
            self.pares_noval_data(start_url)

    def pares_noval_data(self, htmlData):
        # print(htmlData)
        ty_html = etree.HTML(htmlData)
        lis_list = ty_html.xpath('.//div[@class="right -scroll js-industry-container"]//a')
        # print(len(lis_list))
        for li in lis_list:
            # print(li)
            tianyan_info = {}
            tianyan_info['region'] = li.xpath('./text()')[0]
            tianyan_info['region_url'] = li.xpath('./@href')[0]
            print(tianyan_info)
            end_url = li.xpath('./@href')[0]
            print(end_url)
            html = self.send_book_detail_request(end_url)
            self.parse_chpater_list(html)

    def send_book_detail_request(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            print('详情请求成功')
            str = response.content
            start_url = str.decode('utf-8')
            return start_url

    def parse_chpater_list(self, html):
        print('详情')
        print(html)
        x_html = etree.HTML(html)
        # print(x_html)
        # lis = x_html.xpath('.//div[@class="filter-scope"]//span//text()')[0]
        # print(lis)
        # for li in lis:
        #     tianyan_info = {}
        #
        #     tianyan_info['region_url'] = li.xpath('./@href')[0]
        #     print(tianyan_info)


if __name__ == '__main__':
    start_url = 'https://www.tianyancha.com/'
    tianyanspider = TianYanSpider()
    tianyanspider.start_request(start_url)
