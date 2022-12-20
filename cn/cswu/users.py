import requests
from lxml import etree
from multiprocessing import Pool
def crawl(url):
    hd = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    r = requests.get(url, headers=hd)
    tree = etree.HTML(r.text)
    l1 = tree.xpath('/html/body/div/div/div/div/a[1]/h4/text()')
    for i in range(len(l1)):
        print(l1[i])
if __name__ == '__main__':
    for i in range(1, 11):
        url = ['https://www.jianshu.com/recommendations/users?page={}'.format(i) for i in range(1, 11)]
    hu = Pool(processes=4)
    hu.map(crawl, url)
