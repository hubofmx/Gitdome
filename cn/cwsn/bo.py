import pymysql
import requests
connection = pymysql.connect( host="localhost",
                 port=3306,
                 user="root",
                 password="123456",
                 db="xscj",
                 charset='utf8'
)
print("数据库连接成功！")
url1 = "https://www.baidu.com/"
伪装请求头
hd = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
r = requests.get(url1,headers = hd,times=100)

cursor = connection.cursor()
# from bs4 import beautifulsoup4

r = requests.get(url1)
print(type(r))
print(r)
print(r.status_code)
# print(r.text)
print(r.content)
print(r.apparent_encoding)
