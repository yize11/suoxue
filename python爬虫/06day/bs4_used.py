# Beautifulsoup4?
# 是python的一个xml和html的解析器,目的是从xml或html中提取数据

# 安装 pip3 install beautifulsoup4

# bautifulsoup4 要比xpath解析数据慢,因为beautifulsoup4载入的是整个html文档
# findall() 查找所有节点
# find() 查找单个
# 支持css选择器

# 获取标签的属性 p['class'] => p.attrs['class']
# 获取标签的文本 p.get_text() => p.string

# 腾讯招聘
import requests
from bs4 import BeautifulSoup


def tenXunJobSpider():
    start_url = 'https://hr.tencent.com/position.php?keywords=&tid=0&lid=2218'
    start_request(start_url)


def start_request():
    # 构建请求头
    headers = {
        'User - Agent': 'Mozilla / 5.0(X11;Linuxx86_64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 71.0.3578.98Safari / 537.36'
    }
    response = requests.get(url=start_url, headers=headers)
    if response.status_code == 200:
        print('请求成功')
        html = response.text
        parse_job_list(html)


def parse_job_list(htmlData):
    html_soup = BeautifulSoup(htmlData, features='lxml')

    tr_even = html_soup.find_all(name='tr', attrs={'class': 'even'})
    tr_odd = html_soup.find_all(name='tr', attrs={'class': 'odd'})
    print(tr_even, tr_odd)

    for tr in tr_even + tr_odd:
        # print(tr)
        # css选择器
        detail_url = tr.select('.l.square a')[0]['href']
        detail_url = tr.select('.l.square a')[0].attrs['href']
        print(detail_url)


if __name__ == '__main__':
    tenXunJobSpider()
