import requests

# 创建session对象,支持跨请求访问
cus_session = requests.session()
url = 'https://passport.jiayuan.com/dologin.php?pre_url=http://www.jiayuan.com/usercp/'
formdata = {
    'name': '18518753265',
    'password': 'ljh123456',
    'remem_pass': 'on',
    '_s_x_id': '7a106b00170857e594da431080ae0761',
    'ljg_login': '1',
    'm_p_l': '1',
    'channel': '',
    'position': '',
}

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}

response = requests.post(url=url, data=formdata, headers=headers)
print(response.status_code)

if response.status_code == 200:
    pageurl = 'http://usercp.jiayuan.com/v2/?from=login'
    cus_session.get(url=pageurl, headers=headers)
    if response.status_code == 200:
        with open('page.html', 'w') as file:
            file.write(response.text)
