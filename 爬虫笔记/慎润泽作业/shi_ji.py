import json
import pymysql
from urllib import request, parse, error


def sjjy_spider():
    url = "http://search.jiayuan.com/v2/search_v2.php"
    formdata = {
        "sex": "m",
        "key": "",
        "stc": "1:1308,2:18.19,23:1",
        "sn": "default",
        "sv": 1,
        "p": 1,
        "f": "search",
        "listStyle": "bigPhoto",
        "pri_uid": 0,
        "jsversion": "v5",
    }
    send_request(url, formdata)


def send_request(url, formadata):
    # 将参数转为url编码格式的bytes类型数据
    b_form_data = parse.urlencode(formadata).encode('utf-8')
    # 设置请求头
    req_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    # 实例化一个request对象
    req = request.Request(url, data=b_form_data, headers=req_headers)
    # 发起请求
    try:
        response = request.urlopen(req, timeout=10)
        if response.status == 200:
            print('请求成功')
            # print(response.read().decode('utf-8'))
            data = response.read().decode('utf-8').replace('##jiayser##', '')
            data1 = data.replace('//', '')
            parse_data(data1)
    except error.HTTPError as err:
        print(err.reason)
    except error.URLError as err:
        print(err.reason)


def parse_data(data1):
    print(data1)
    data_dict = json.loads(data1)
    userInfos = data_dict['userInfo']
    for userinfo in userInfos:
        # print(userinfo)
        info = {}
        info['image'] = userinfo['image']
        info['nickname'] = userinfo['nickname']
        info['age'] = userinfo['age']
        info['adress'] = userinfo['work_location']
        info['tags'] = ';'.join(userinfo['randTag'].replace('<span>', '').split('</span'))
        info['sex'] = userinfo['sex']
        print(info)
        save_mysql(info)


def save_mysql(info):
    '''
    进行数据持久化
    :param info:
    :return:
    '''
    # # 创建插入语句
    # insert_sql = """
    # INSERT INTO sjjy(image,nickname,age,adress,tags,sex)
    # VALUE (%s,%s,%s,%s,%s,%s)
    # """
    insert_sql = """
    INSERT INTO sjjy(%s)
    VALUES(%s)
    """ % (','.join(info.keys()), ','.join(['%s'] * len(info)))

    try:
        # mysql_cursor.execute(insert_sql,[info['image'],info['nickname'],info['age'],info['adress'],info['tags'],info['sex']])
        mysql_cursor.execute(insert_sql, list(info.values()))
        mysql_con.commit()
        print('数据插入成功', info['nickname'])
    except Exception as err:
        print(err)
        mysql_con.rollback()


if __name__ == '__main__':
    # 创建数据库链接
    mysql_con = pymysql.Connect(
        '127.0.0.1',
        'root',
        '123456',
        'shijijiayuan',
        3306,
        charset='utf8'
    )
    # c创建游标
    mysql_cursor = mysql_con.cursor()

    sjjy_spider()
