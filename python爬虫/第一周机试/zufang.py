import requests
from lxml import etree


class zufang():
    def __init__(self):
        pass

    def start_request(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print('请求成功')
            self.parse_noval_data(response.text)

    def parse_noval_data(self, htmlData):
        x_html = etree.HTML(htmlData)
        li_list = x_html.xpath('//div[@class="content__list"]')
        print(len(li_list))
        # 遍历
        for li in li_list:
            book_info = {}
            # 标题
            book_info['title'] = li.xpath('./div[@class="content__list--item--main"]/div/p/a/text()')[0]
            print(book_info)



if __name__ == '__main__':
    staart_url = 'https://bj.lianjia.com/ershoufang/pg2/'
    zufang = zufang()
    zufang.start_request(staart_url)