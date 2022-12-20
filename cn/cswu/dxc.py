import requests
import time
from lxml import etree
# 1、多进程：引入Pool池
from multiprocessing import Pool


def crawl(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
    tree = etree.HTML(resp.text)
    titles = tree.xpath('//*[@id="wp_news_w6"]/ul/li/div[1]/span[2]/a/text()')
    parts = tree.xpath('//*[@id="wp_news_w6"]/ul/li/span[1]/text()')
    dts = tree.xpath('//*[@id="wp_news_w6"]/ul/li/div[2]/span/text()')
    clicks = tree.xpath('//*[@id="wp_news_w6"]/ul/li/span[2]/span/text()')
    '''
    for title,part,click,dt in zip(titles,parts,clicks,dts):
         print(title,part,click,dt)
     '''


if __name__ == '__main__':
    # 列表推导式
    urls = ['http://www.cswu.cn/34/list{}.htm'.format(i) for i in range(1, 687)]
    # print(urls)
    ''' 
    #for循环生成多个网址
    for i in range(1,31):
        urls = 'http://www.cswu.cn/34/list{}.htm'.format(i)
        urls = 'http://www.cswu.cn/34/list'+str(i)+'.htm'.format(i)
    '''
    # 串行爬取，开始时间
    start1 = time.time()
    print(start1)
    for url in urls:  # url 取31个网页，调用31次crawl函数
        crawl(url)
    end1 = time.time()
    print(end1)
    print('串行爬虫时间：', end1 - start1)
    # 多进程爬取,开始时间
    start2 = time.time()
    print(start2)
    # 2、创建进程池,P140
    test_pool = Pool(processes=4)  # 规定用法,Pool（）函数
    # 3、使用map方法完成多线程爬取
    test_pool.map(crawl, urls)
    # map()函数：2个参数，第一个参数：crawl--指自己定义的爬虫函数，函数名；
    #                    第二个参数：urls--自己定义的装多个爬虫网页的变量；
    end2 = time.time()
    print(end2)
    print('并行爬虫时间：', end2 - start2)

'''
#使用多进程要完成的三个步骤
#1、多进程：引入Pool池
from multiprocessing import Pool
# 2、创建进程池,P140
test_pool = Pool(processes=4)  # 规定用法,Pool（）函数
# 3、使用map方法完成多线程爬取
test_pool.map(crawl, urls)
 '''
