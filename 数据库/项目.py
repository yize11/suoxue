import hashlib
from pymysql import *
from redis import *



def mysql_login(username,upwd):
    try:
        conn=connect(host='localhost',port=3306,user='root',password='0.0',database='D1',charset='utf8')
        csl=conn.cursor()
        r = csl.execute('select upwd from users where uname = "{}"'.format(username))
        a = csl.fetchone()
        a = a[0]
        print(a)
        if r == None:
            print('请去注册')
        else:
            if upwd == a:
                sr = StrictRedis(decode_responses=True)
                
                print('登陆成功')
                main_data()
            else:
                print('输入有误')
    except Exception as e:
        # print(e)
        print('输入错误')
def redis_login():
    username = input('请输入用户名:')
    password = input('请输入密码:')
    s1 = hashlib.sha1()
    s1.update(password.encode('utf8'))
    upwd = s1.hexdigest()
    try:
        sr = StrictRedis(decode_responses=True)
        r = sr.get(username)
        if r == None:
            mysql_login(username,upwd)
        else:
            if upwd == r:
                print('登录成功')
                main_data()
            else:
                print('密码错误')
    except Exception as e :
        print(e)
        print('redis的登录函数')
def register():
    username = input('请输入账户:')
    password = input('请输入密码:')
    s1 = hashlib.sha1()
    s1.update(password.encode('utf8'))
    upwd = s1.hexdigest()
    print(username,upwd)
    try:
        conn = connect(host='localhost',port=3306,user='root',password='0.0',database='D1',charset='utf8')
        csl = conn.cursor()
        csl.execute('insert into users values(0,"{}","{}")'.format(username,upwd))
        conn.commit()
    except Exception as e:
        print(e)
def main():
    while True:
        a = input('请选择 【1】注册 【2】登录 【0】退出')
        if a == '1':
            register()
        elif a == '2':
            redis_login()
        elif a == '0':
            exit()
        else:
            print('输入有误')

def main_data():
    print('欢迎来到水果店管理系统')
    a = input('是否登录系统:（y确定，其余返回)')
    if a == 'y':    
        while True:
            print('||||||||||||||||||||||||||||||||')
            print('1.查看水果')
            print('2.修改水果的价格')
            print('3.删除水果')
            print('4.添加的水果')
            print('5.退出系统')
            print('||||||||||||||||||||||||||||||||')
            x = input('请输入您要选择的功能:')
            if x == '1':
                find_data()
            elif x == '2':
                ALTER()
            elif x == '3':
                delete()
            elif x == '4':
                ADD()
            elif x == '5':
                print('退出程序成功')
                exit()
        else:
            print('退出成功')
            exit()


#查看水果
def find_data():
    c=input('请输入你要查看的水果名字:')
    try:
        conn = connect(host='localhost',port=3306,user='root',password='0.0',database='D1',charset='utf8')
        cs1 = conn.cursor()
        sql = """select * from shop where commodity=%s"""
        cs1.execute(sql,c)
        result = cs1.fetchall()
        conn.commit()
        print(result)
    except Exception as e:
        print(e)
    conn.close()
    cs1.close()



#添加水果
def ADD():
    
    c = input('请输入要添加的水果名字:')
    price = input('请输入价格:')
    much = input('请输入要添加的数量')

    try:
        conn = connect(host='localhost',port=3306,user='root',password='0.0',database='D1',charset='utf8')
        cs1 = conn.cursor()
        sql = """insert into shop values (0,%s,%s,%s)"""
        
        cs1.execute(sql,(c,price,much))
     
        conn.commit()
        print('添加成功')
    except Exception as e:
        print(e)
    conn.close()
    cs1.close()

        
   

#修改
def ALTER():
    price = input('请输入修改的水果价格:')
    name = input('请输入需要修改的水果名:')
    try:
        conn = connect(host='localhost',port=3306,user='root',password='0.0',database='D1',charset='utf8')
        cs1 = conn.cursor()
        sql = """update shop set price = %s where commodity = %s"""
        cs1.execute(sql,(price,name))
        cs1.fetchone()
        conn.commit()
        print('修改成功')
    except Exception as e:
        print(e)
    conn.close()
    cs1.close()


#删除
def delete():
    name = input('请输入要删除的水果名字:')
    try:
        conn = connect(host='localhost',port=3306,user='root',password='0.0',database='D1',charset='utf8')
        cs1 = conn.cursor()
        sql = """delete from shop where commodity = %s"""
        # c = a.execute('delete from shop where commodity = "{}"'.format(name))
        res = cs1.execute(sql,name)        
        if res:
            print('删除成功')
        conn.commit()
    except Exception as e:
        print(e)
    conn.close()
    cs1.close()


if __name__ == '__main__':
    main()