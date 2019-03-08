from urllib import request, parse, error
import pymysql
import json
import re


# 'https://maoyan.com/board/4?offset=0'
# 'https://maoyan.com/board/4?offset=10'

def cat():
    url = 'https://maoyan.com/board/4?offset=0'
    response = request.urlopen(url=url, timeout=20)
    # print(response.read())
    html = response.read().decode('utf-8')

    req_hearder = {

        'User-Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 71.0.3578.98Safari / 537.36'
    }
    req = request.Request(url, headers=req_hearder)
    try:
        response = request.urlopen(req)
        if response.status == 200:
            print('请求成功')
            html = response.read().decode('utf-8')
            # print(html)
            # < d1\sclass = "board-wrapper" >.* ? < dd >.* ? < i\sclass = "board-index board-index-1" >.* ? < / i >.* ? < a\shref = "(.*?)". *? >.* ? < img\ssrc = "(.*?)". *? >
            pattern = re.compile(r'<div\sclass="movie-item-info">.*?<p\sclass="name">.*?<a\shref="(.*?)".*?>(.*?)</a>',
                                 re.S)
            result = re.findall(pattern, html)
            print(result)
    except error.HTTPError as err:
        print(err.reason)
    except error.URLError as err:
        print(err.reason)

    data_dict = json.loads(html)
    userInfos = data_dict['/films/1203']
    for userinfo in userInfos:

        info = {}
        info['image'] = userinfo['image']
        info['nickname'] = userinfo['name']
        info['data'] = userinfo['data']
        info['adress'] = userinfo['work_location']
        info['tags'] = ';'.join(userinfo['randTag'].replace('<span>', '').split('</span'))
        info['sex'] = userinfo['sex']
        print(info)
        # insert_sql = """
        # INSERT INTO sjjy(%s)
        # VALUES(%s)
        # """ % (','.join(info.keys()), ','.join(['%s'] * len(info)))

        # 创建插入语句
        insert_sql = """
        INSERT INTO sjjy(image,nickname,age,adress,tags,sex)
        VALUE (%s,%s,%s,%s,%s,%s)
        """

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
        '0.0',
        'test1',
        3306,
        charset='utf8'
    )
    # 创建游标
    mysql_cursor = mysql_con.cursor()

    cat()
