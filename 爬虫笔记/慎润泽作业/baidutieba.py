from urllib import request, parse
import re


# url = 'https://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3&ie=utf-8&pn=50'

def tieba_spider():
    kw = input('请输入搜索贴吧名称：')
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入截止页码'))

    for page in range(start_page, end_page + 1):
        parmas = {
            'kw': kw,
            'ie': 'utf-8',
            'pn': (page - 1) * 50
        }
        b_data = send_request('https://tieba.baidu.com/f?', parmas)
        parse_page_data(b_data)


def send_request(url, parmas=None):
    if parmas:
        parmas = parse.urlencode(parmas)
        fullUrl = url + parmas
        print(fullUrl)
    req_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    req = request.Request(fullUrl, headers=req_headers)
    response = request.urlopen(req)
    if response.status == 200:
        print('请求成功')
        b_data = response.read()
        return b_data


def parse_page_data(b_data):
    html = b_data.decode('utf-8')
    # print(html)
    # re.S 让.符合匹配换行符
    pattern = re.compile(r'<div\sclass="threadlist_title pull_left j_th_tit.*?">.*?<a.*?href="(.*?)".*?>(.*?)</a>',
                         re.S)
    result = re.findall(pattern, html)
    print(result)
    for detailInfo in result:
        print('正在发起' + detailInfo[1] + '请求')
        base_url = 'https://tieba.baidu.com/f?pn=50&ie=utf-8&kw=%E7%BE%8E%E5%A5%B3'
        detail_url = parse.urljoin(base_url, detailInfo)
        b_data = send_request(detail_url)
        parse_detail_data(b_data)


def parse_detail_data(b_data):
    html = b_data.decode('utf-8')
    pattern = re.compile('<img\sclass="BDE_Image"\ssrc="(.*?)".*?>', re.S)
    result = re.findall(pattern, html)
    print(result)


if __name__ == '__main__':
    tieba_spider()
