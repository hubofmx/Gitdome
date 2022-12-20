import requests
import time
from lxml import etree
import pymysql
def create_table():
    sql = "CREATE TABLE news(" \
          "id  INT PRIMARY KEY AUTO_INCREMENT," \
          "title VARCHAR(100)," \
          "dat_e  VARCHAR(20)) "
    cursor.execute(sql)
    print("数据表创建成功！")
    connection.commit()
def dowenr(url,hd):
    r = requests.get(url,headers=hd)
    tree = etree.HTML(r.text)
    tit = tree.xpath('//*[@id="wp_news_w14"]/ul/li/div[1]/span[2]/a/text()')
    print(tit[0])
    days = tree.xpath('//*[@id="wp_news_w14"]/ul/li/div[2]/span/text()')
    list_all = []
    for i in zip(tit,days):
        list_all.append(i)
    for i in range(len(tit)):
        print(tit[i],days[i])







if __name__ == '__main__':
    connection=pymysql.connect(host='localhost',
                    port=3306,
                    user='root',
                    password='123456',
                    db='hb',
                    charset='utf8')
    print("数据库连接成功！")
    cursor=connection.cursor()
    hd = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    # create_table()
    for i in range(1,6):
        url = "http://www.hfuu.edu.cn/4153/list"+str(i)+".htm"
        time.sleep(10)
        dowenr(url,hd)

