# 1.发起请求:python自带的urllib模块
from urllib import request

url = 'https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=1'
# 如果请求需要添加请求头
"""
url:设置目标url
data=None,:默认为None,表示发起的是一个get请求,
反之,不为None,表示发起的是一个post请求
headers={}:设置请求头,传递一个字段类型的参数
"""
req_header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
req = request.Request(req_header)

# 使用urlopen方法faqi请求,获得响应结果
response = request.urlopen(url=url, timeout=20)
# print(response.read())
html = response.read().decode('utf-8')
print(len(html))
"""
# 获取源代码
文件读写模式:
r:打开一个文件,只有可读权限 rb:  r+  rb+
w:打开一个文件,有写入的权限 wb: w+: wb+:
a:打开一个文件,又追加权限  ab: a+:  ab+:
"""

with open('quanshu.html', 'w') as file:
    file.write(html)
    # 获取响应的状态码
code = response.status
print(code)

# 获取响应的响应头
response_headers = response.getheaders()
print(response_headers)

# 获取某一个响应头参数
server = response.getheader('Server')
print(server)
# 获取当前请求的url地址
current_url = response.url
print(current_url)
# 获取请求的reason(如果成功返回的是OK)
reason = response.reason
print(reason)
