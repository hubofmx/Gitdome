import requests
from lxml import etree
import pymysql

#建表函数
def  create_table():
    # 一、创建数据表
    sql = "CREATE TABLE jzinfo(" \
          "id  INT PRIMARY KEY AUTO_INCREMENT," \
          "title VARCHAR(100)," \
          "dat_e  VARCHAR(20)) "
    cursor.execute(sql)
    print("数据表创建成功！")
    connection.commit()
#网页抓取函数
def downer(url,hd):
    r = requests.get(url,headers=hd)
    #print(r.text)
    tree = etree.HTML(r.text)
    # 讲座的标题
    titles = tree.xpath('//*[@id="wp_news_w6"]/ul/li/div[1]/span[2]/a/text()')
    # 日期
    dates = tree.xpath('//*[@id="wp_news_w6"]/ul/li/div[2]/span/text()')
    list_all=[]
    # zip:打包，压缩     zip(x,y)-->x  y  都是带有多个值的序列--列表， x出一个值 y出一个值，形成一个小元祖
    for i in zip(titles,dates):
        #print(i)
        list_all.append(i)   # i 对应的 （一个标题 ， 一个日期）
    ''' 
    for i in range(len(titles)):
        print(titles[i],dates[i])
        # [ (),().....() ]---外面是列表，共有75个值， 里面的75个值是小列表/元祖
        # 小列表/元祖内容：讲座信息的标题 、日期
        list_all.append( [titles[i]+'   ',dates[i]+'\n'] )
    '''
    '''
    # 打印到屏幕
    for i in list_all:
        print(i)
    '''
    ''' 
    #写进文件
    to_file(list_all)
     '''
    #写进数据库
    to_mysql(list_all)
# 写进文件函数
def to_file(list_all):
    with open("d:/jzinfo.txt","a+",encoding="utf-8") as f:
        #writelines---写入列表中的多个字符串
        # list_all ---列表，但里面是列表/元祖
        # 列表/元祖里是字符串
        for i in range(len(list_all)):
            f.writelines(list_all[i])
        print("写入成功！")

# 1206作业：
#写进数据库
def  to_mysql(list_all):
    for i in range(len(list_all)):  # i = 0 1 3 4
        #print(list_all[i][0],list_all[i][1])
        sql = "insert into jzinfo(title,dat_e) values(%s,%s)"
        cursor.execute(sql, (  str(list_all[i][0]), str(list_all[i][1]) )  )
        connection.commit()
    print("数据插入成功！")
    #结果的展示，可有可无，看题干要求
    print("即将展示结果：")
    sql2 = "select * from jzinfo"
    cursor.execute(sql2)
    for t in cursor.fetchall():
        print(t)

# python  的主程序---  构建目标网页
if __name__ == '__main__':
# cursor  数据库的代表，之后数据库操作，全部以此开始
    connection = pymysql.connect(host='localhost',  # 主机
                                 port=3306,  # 端口号
                                 user='root',  # 用户名
                                 password='123456',  # 密码
                                 db='xscj',  # 连接的数据库名
                                 charset='utf8'  # 最后一个参数，没有逗号，字符集设定
                                 )
    print("数据库连接成功！")
    cursor = connection.cursor()
    hd = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    # 创建数据表，该语句只能执行一次，之后就将其注释
    create_table()
    for i in range(1,7):  # i =1 2 3 4 5 6
        url = "https://www.cswu.cn/38/list"+ str(i) +".htm"
        #print(url)
        downer(url,hd)
