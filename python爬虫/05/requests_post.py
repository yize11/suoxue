import requests

url = 'https://passport.jiayuan.com/dologin.php?pre_url=http://www.jiayuan.com/usercp/'

"""
'name': '18518753265',
'password': '123',
'remem_pas's: 'on',
_'s_x_id': '7a106b00170857e594da431080ae0761',
'ljg_login': '1',
'm_p_l': '1',
'channel': '',
'position': '',
"""

"""
name: 18518753265
password: ljh123456
remem_pass: on
_s_x_id: 7a106b00170857e594da431080ae0761
ljg_login: 1
m_p_l: 1
channel: 
position: 
"""

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

cookiejar = response.cookies
print(cookiejar)
print(type(cookiejar))
# pageurl = 'http://usercp.jiayuan.com/v2/?from=login'
