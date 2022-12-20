import requests
from lxml import etree
ur1="https://www.cswu.cn/38/list1.htm"
hd = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56"}
r = requests.get(ur1,headers=hd)
tree = etree.HTML(r.text)
# 第一页
# //*[@id="wp_news_w6"]/ul/li[1]
# //*[@id="wp_news_w6"]/ul/li[2]
# //*[@id="wp_news_w6"]/ul/li[3]/div[1]/span[2]/a
# # 第二页
# //*[@id="wp_news_w6"]/ul/li[1]
# //*[@id="wp_news_w6"]/ul/li[2]/div[1]/span[2]/a
# //*[@id="wp_news_w6"]/ul/li[3]/div[1]/span[2]/a
l1 = tree.xpath('//*[@id="wp_news_w6"]/ul/li//text()')
print(len(l1))





































for i in l1:
    print(i)
