# error模块:在我们请求过程中,可能因为服务器错误,弱网环境...
# 造成请求失败,这时我们需要对这些错误进行异常处理,不然会造成代码崩溃
from urllib import request,error
'''
error.URLError:
产生的原因主要有：
    没有网络连接
    服务器连接失败
    找不到指定的服务器
有一个reason属性:返回错误的原因
'''
'''
error.HTTPError
    HTTP请求错误，比如未认证，页面不存在
    code:请求的状态码
    reason:返回错误的原因
    headers:返回响应头部
'''
import ssl

context = ssl._create_unverified_context()

# url = 'https://www.baidu.com/12345.htm'
url = 'https://www.qidian.com/all/nsacnscn.htm'

try:
    response = request.urlopen(url,timeout=0.01,context=context)
    print(response.status)
except error.HTTPError as err:
    print('HTTPError')
    print(err.code)
    print(err.reason)
    print(err.headers)
except error.URLError as err:
    print('URLError',err.reason)

