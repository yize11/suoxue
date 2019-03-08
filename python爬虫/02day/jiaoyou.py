from urllib import request, parse
import json
import ssl

url = 'http://search.jiayuan.com/v2/search_v2.php'

form_data = {
    "sex": "f",
    "key": "",
    "stc": "1:11,2:20.28,23:1",
    "sn": "default",
    "sv": "1",
    "p": "1",
    "f": "search",
    "listStyle": "bigPhoto",
    "pri_uid": "0",
    "jsversion": "v5"
}
b_form_data = parse.urlencode(form_data).encode('utf-8')
# 请求头
req_header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
# 实例化一个request对像
req = request.Request(url, headers=req_header, data=b_form_data)
# 发起请求
    try:
        response = request.urlopen(req,timeout=10)
        if response.status == 200:
            print('请求成功')
    except error.HTTPError as err:
                print(err.)

req1 = response.read().decode('utf-8')
req2 = req1.replace("##jiayser##", "")
req3 = req2.replace("//", "")
result_data = json.loads(req3)
positiones = result_data['express_search']
print(positiones)

for position in positiones:
    jobInfo = {}
    jobInfo['work_location'] = position['work_location']
    jobInfo['realUid'] = position['realUid']
    jobInfo['fxly'] = position['fxly']
    jobInfo['uid'] = position['uid']
    jobInfo['age'] = position['age']
    jobInfo['helloUrl'] = position['helloUrl']
    print(jobInfo)
    with open('jiaoyou.json', 'a+') as file:
        data = json.dumps(jobInfo, ensure_ascii=False)
