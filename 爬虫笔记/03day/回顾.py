爬虫代码基本步骤

step1:
 分析网站,寻找目标url
step2:
 分析目标url参数(get,post)

 get请求参数部分:把?后面的参数写在字典中,
 然后使用parse.urlencode(字典参数),得到
 了url编码格式的字符串

 post请求参数部分:是处理表单数据,将表单数据
 放在字典中,然后使用parse.urlencode(字典参数),
 得到了url编码格式的字符串,最后使用encode方法将
 字符串转为bytes类型.

step3(发起请求):
  (1):设置请求头,添加UA (cookie,referer)
  (2):实例化一个Request对象(request.Request)
  (3):根据实例化的Request对象,使用request.urlopen()
      方法发起请求

step4(处理响应结果):
  (1):Ajax请求得到的一般是json数据,使用json模块处理
     使用json.loads将json字符串,转为python数据类型
  (2):对于非结构化数据(数据在html页面中),可以使用re正
     则提取数据(xpath,BeautifulSoup,pyquery)
  (3):如果还有其他url,则继续发起请求

step5(数据的持久化):
  (1):文件存储(json,csv,txt...)
  (2):数据库存储(mysql,mongodb,redis)



