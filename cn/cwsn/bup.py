import requests
from bs4 import BeautifulSoup
try:
    ur1 ="https://www.cswu.cn/34/list.htm"
    hd = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    r = requests.get(ur1,headers = hd)
    r.raise_for_status()
    r.encoding="utf-8"
    soup =BeautifulSoup(r.text,'html.parser')

except:
    print("异常")
#wp_news_w6 > ul > li.list_item.i1 > div.fields.pr_fields > span.Article_Title > a
#wp_news_w6 > ul > li.list_item.i2 > div.fields.pr_fields > span.Article_Title > a
list_s= soup.select("#wp_news_w6 > ul > li.list_item > div.fields.pr_fields > span.Article_Title > a")
list1 = []
for i in range(0,len(list_s)-4) :
    list1.append(list_s[i].string)
with open("D:/temp/pc/cwsn.txt","w+",encoding="utf-8") as f :
    for z in list1:
        f.writelines(z+'\n')
    print("爬取结束！")
