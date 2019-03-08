from urllib import request,parse,error
import json
import pymysql
#分心网站得到目标url:http://search.jiayuan.com/v2/search_v2.php

# post请求

"""
sex: f
key: 
stc: 1:11,2:20.28,23:1
sn: default
sv: 1
p: 1
f: search
listStyle: bigPhoto
pri_uid: 0
jsversion: v5
"""

def sjjy_spider():
    start_url = 'http://search.jiayuan.com/v2/search_v2.php'
    form_data = {
        'sex': 'f',
        'key': '',
        'stc': '1: 11, 2: 20.28, 23: 1',
        'sn': 'default',
        'sv': '1',
        'p': 1,
        'f': 'search',
        'listStyle': 'bigPhoto',
        'pri_uid': '0',
        'jsversion': 'v5',
    }
    send_request(start_url,form_data)

def send_request(url,form_data):
    #将参数转为url编码格式的bytes类型数据
    b_form_data = parse.urlencode(form_data).encode('utf-8')
    #设置请求头参数
    req_headers = {
        'User-Agnet':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    #实例化一个Request对象
    req = request.Request(url,data=b_form_data,headers=req_headers)
    #发请求
    try:
        response = request.urlopen(req,timeout=10)
        if response.status == 200:
            print('请求成功')
            # print(response.read().decode('utf-8'))
            data = response.read().decode('utf-8').replace('##jiayser##//','').replace('##jiayser##','')

            page_total = parse_data(data)
            #获取当前请求的页数
            cur_page = form_data['p']
            if page_total > cur_page:
                form_data['p'] += 1
                print('正在请求第'+str(form_data['p'])+'页')
                send_request(url,form_data)

    except error.HTTPError as err:
        print(err.reason)
    except error.URLError as err:
        print(err.reason)

def parse_data(data):
    print(data)
    data_dict = json.loads(data)
    #获取总页数
    page_total = int(data_dict['pageTotal'])
    userInfos = data_dict['userInfo']
    for userinfo in userInfos:
        # print(userinfo)
        info = {}
        info['coverImage'] = userinfo['image']
        info['name'] = userinfo['nickname']
        info['age'] = int(userinfo['age'])
        info['adress'] = userinfo['work_location']
        info['tags'] = ';'.join(userinfo['randTag'].replace('<span>','').split('</span>'))
        info['sex'] = userinfo['sex']
        print(info)
        save_userinfo_to_db(info)
    return page_total

def save_userinfo_to_db(info):
    """
    进行数据持久化
    :param info:
    :return:
    """
    #创建数据库插入语句
    # insert_sql = """
    # INSERT INTO sjjy(coverImage,name,age,adress,tags,sex)
    # VALUES (%s,%s,%s,%s,%s,%s)
    # """
    insert_sql = """
    INSERT INTO sjjy(%s)
    VALUES(%s)
    """ % (','.join(info.keys()),','.join(['%s']*len(info)))

    try:
        # my_cursor.execute(insert_sql,[info['coverImage'],info['name'],info['age'],info['adress'],info['tags'],info['sex']])
        my_cursor.execute(insert_sql,list(info.values()))
        mysql_con.commit()
        print('数据插入成功',info['name'])
    except Exception as err:
        print(err)
        mysql_con.rollback()


if __name__ == '__main__':

    #创建数据库连接
    """
    host=None, user=None, password="",
    database=None, port=0, charset=''
    """
    mysql_con = pymysql.Connect(
        '127.0.0.1','root','ljh1314',
        'shijijiayuan',3306,charset='utf8'
    )
    #创建游标
    my_cursor = mysql_con.cursor()

    sjjy_spider()