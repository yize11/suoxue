from urllib import request
from urllib import parse
# parse:是urllib下的一个解析模块,可以拆分,作何,编码url
# quote可以对中文字符进行url编码
#quote_str = parse.quote('新年愿望')
#print(quote_str)
# unquote:将url编码的中文字符,反序列化为中文字符(解码)
#print(parse.unquote(quote_str))
#url = 'https://www.baidu.com/s?wd='+quote_str
# 添加请求头
#req_headers = {
    #'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
#}
# 构建一个请求对象
#req = request.Request(url=url, headers=req_headers)
# get 请求传递的参数
parmas = {
    'wd':'新年愿望'
}
parmas = parse.urlencode(parmas)
print(parmas)
url = 'https://www.baidu.com/s?' + parmas