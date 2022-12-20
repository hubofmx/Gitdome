import requests
from lxml import etree

#获取网页的信息 并  解析
def downer(url,hd):
    r = requests.get(url,headers=hd)
    #print(r.text)
    #种树
    tree = etree.HTML(r.text)
    # 标题
    # //*[@id="wp_news_w6"]/ul/li[1]/div[1]/span[2]/a
    # //*[@id="wp_news_w6"]/ul/li[2]/div[1]/span[2]/a
    titles= tree.xpath("//*[@id='wp_news_w6']/ul/li/div[1]/span[2]/a/text()")
    #print(titles)
    # 日期
    dates = tree.xpath('//*[@id="wp_news_w6"]/ul/li/div[2]/span/text()')
    #print(dates)
    list_all = []
    for i in range(len(titles)): # i= 0 1 2
        t = [ titles[i]+'    ',dates[i]+'\n' ]   #---- 列表元祖
        #print(t)
        list_all.append(t)
    #print(len(list_all))
    to_file(list_all)   # 杨涛  --- 买奶茶


def to_file(list_all):
    #print(list_all[0][0])  # list_all:列表   list_all[i]:列表--->字符串
    # 文件写东西，写的是字符串
    with open("d:/jzinfo.txt","a+",encoding="utf8") as f:
        for i in range(len(list_all)):
            f.writelines(list_all[i])
        print('写入成功！')
    #for i in list_all:
     #   print(i)


# 分析目标网页  主程序
if __name__ == '__main__':   # 李老师  ---买奶茶
    # https://www.cswu.cn/38/list1.htm
    # https://www.cswu.cn/38/list2.htm
    # https://www.cswu.cn/38/list3.htm
    # https://www.cswu.cn/38/list6.htm
    # 1  2  3  4  5  6  ???????
    hd = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    for i in range(1,7): # i = 1 2 3 4 5 6
        url = "https://www.cswu.cn/38/list" + str(i) + ".htm"
        #print(url)
        downer(url,hd)   # 陈杰 ---买奶茶
