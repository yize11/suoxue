# url = 'https://www.autohome.com.cn/all/'


import requests
from lxml import etree


class qiche(object):
    def __init__(self):
        pass

    def start_request(self, url):
        headers = {
            'User - Agent': 'Mozilla / 5.0(X11;Linuxx86_64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 71.0.3578.98Safari / 537.36',
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print('请求成功')
            content = response.content
            # content_str = content.decode('gb2312')
            self.parse_noval_data(content)

    def parse_noval_data(self, htmlData):
        x_html = etree.HTML(htmlData)
        li_list = x_html.xpath('//div[@class="article-wrapper"]/ul/li')
        print(len(li_list))
        # 遍历
        for lis in li_list:
            for li in lis:
                cat_info = {}
                # 图片
                cat_info['title'] = 'https:' + li.xpath('.//div[@class="article-pic"]//img/@src')[0]
                # 标题
                cat_info['biaoti'] = li.xpath('./h3/text()')[0]
                # 时间
                cat_info['shijian'] = li.xpath('.//div[@class="article-bar"]/span[1]/text()')[0]
                # 浏览量
                cat_info['liulan'] = li.xpath('.//div[@class="article-bar"]/span[2]/em[1]/text()')[0]
                # 评论
                cat_info['pinglun'] = li.xpath('.//div[@class="article-bar"]/span[2]/em[2]/text()')[0]
                # 内容
                cat_info['neirong'] = li.xpath('.//p/text()')[0]
                print(cat_info)
                # nextpage(下一页)
                next_page = x_html.xpath('//a[@class="page-item"]/@href')
                if len(next_page) > 0:
                    next_page = 'https:' + next_page[0]
                    # 继续发起请求
                    self.start_request(next_page)
                else:
                    print('数据获取完毕了')


if __name__ == '__main__':
    start_url = 'https://www.autohome.com.cn/all/'
    qidianspider = qiche()
    qidianspider.start_request(start_url)
