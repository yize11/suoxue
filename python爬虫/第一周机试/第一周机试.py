import requests
from lxml import etree


class ershou():
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
        li_list = x_html.xpath('//li[@class="clear LOGCLICKDATA"]')
        print(len(li_list))


        # 遍历
        for li in li_list:
            book_info = {}
            # 标题
            book_info['title'] = li.xpath('./div[@class="info clear"]/div/a/text()')[0]
            # 地址
            book_info['dizhi'] = li.xpath('.//div[@class="address"]/div/a/text()')[0]
            # 室内
            book_info['shinei'] = li.xpath('.//div[@class="address"]/div/text()[1]')[0]
            # 平方
            book_info['ping'] = li.xpath('.//div[@class="address"]/div/text()[2]')[0]
            # 方向
            book_info['fangwei'] = li.xpath('.//div[@class="address"]/div/text()[3]')[0]
            # 精装
            book_info['jingzhuang'] = li.xpath('.//div[@class="address"]/div/text()[4]')[0]
            # 电梯
            book_info['dianti'] = li.xpath('.//div[@class="address"]/div/text()[5]')[0]
            # 楼层
            book_info['louceng'] = li.xpath('.//div[@class="flood"]/div/text()[1]')[0]
            # 多少年建的楼
            book_info['year'] = li.xpath('.//div[@class="flood"]/div/text()[2]')[0]
            # 名字
            book_info['name'] = li.xpath('.//div[@class="flood"]/div/a/text()')[0]
            # 关注
            book_info['guanzhu'] = li.xpath('.//div[@class="followInfo"]/text()[1]')[0]
            # 浏览量
            book_info['liulan'] = li.xpath('.//div[@class="followInfo"]/text()[2]')[0]
            # 值钱数
            book_info['wan'] = li.xpath('.//div[@class="totalPrice"]/span/text()')[0] + '万'
            # 一平方多少钱
            book_info['danjia'] = li.xpath('.//div[@class="unitPrice"]/span/text()')[0]
            
            print(book_info)

            # # nextpage(下一页)
            # next_page = x_html.xpath('//div[@class="page-box fr"]/div/a/@href')
            # if len(next_page) > 0:
            #     next_page = 'https:' + next_page[0]
            #     self.start_request(next_page)
            # else:
            #     print('数据获取完毕')


if __name__ == '__main__':
    staart_url = 'https://bj.lianjia.com/ershoufang/pg2/'
    ershou = ershou()
    ershou.start_request(staart_url)
