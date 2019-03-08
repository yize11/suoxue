#parse:可以对url进行拆分,组合,编码,解码,拼接
from urllib import parse

#parse.urlencode():将字典类型的参数转为url编码格式
form_data ={
    'first': 'false',
    'pn': 2,
    'kd': '后端',
}
#get请求直接使用urlencode将参数转为url编码格式
form_data1 = parse.urlencode(form_data)
print(form_data1)
#post请求urlencode将参数转为url编码格式,然后使
# 用encode方法将字符串转为bytes类型
form_data2 = parse.urlencode(form_data).encode('utf-8')
print(form_data2)

# parse.parse_qs():将url编码格式的字符串转化为字典类型
#注意key对应的value是一个list
parmas = parse.parse_qs(form_data1)
print(parmas)

#parse.quote()将中文字符转为url编码的字符
key = '我的国'
result = parse.quote(key)
print(result)

#parse.unquote()将url编码的字符转换为中文字符
unquote_result = parse.unquote(result)
print(unquote_result)

#将不完整的url参照基类url,拼接完整
base_url = 'http://www.qidian.com/book/123456.html'
sub_url = '12345789.html'
full_url = parse.urljoin(base_url,sub_url)
print(full_url)

#parse.urlparse():将url进行拆分
base_url = 'http://www.qidian.com/book/123456.html'
result = parse.urlparse(base_url)
"""
ParseResult(
 scheme='http',:协议
 netloc='www.qidian.com', ip或域
 path='/book/123456.html', 路径
 params='', 参数
 query='', 查询参数(?后面拼接的参数)
 fragment='' : 锚点
 )

"""
print(result)
print(result.scheme)
#parse.urlunparse():将url的各个部分合并为一个完整的url
#scheme, netloc, url, params, query, fragment
url_datas = ('https','www.baidu.com','book','','wd=xxx','1234')
full_url = parse.urlunparse(url_datas)
print(full_url)
