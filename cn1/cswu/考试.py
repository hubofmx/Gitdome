import requests
from lxml import etree
def pat(url, hd):
    r = requests.get(url, headers=hd)
    tree = etree.HTML(r.text)
    titles = tree.xpath('//*[@id="wp_news_w6"]/ul/li/div[1]/span[2]/a/text()')
    departs = tree.xpath('//*[@id="wp_news_w6"]/ul/li/span[1]/text()')
    dates = tree.xpath('//*[@id="wp_news_w6"]/ul/li/div[2]/span/text()')
    hits = tree.xpath('//*[@id="wp_news_w6"]/ul/li/span[2]/span/text()')
    list_all = []
    for i in range(len(titles)):
        t = [titles[i] + '  ', departs[i] + '\t\t\t\t', dates[i] + '  ', hits[i] + '\n']
        list_all.append(t)
    print(list_all)

if __name__ == "__main__":
    hd = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56"}
    # https://www.cswu.cn/34/list1.htm
    # https://www.cswu.cn/34/list2.htm
    for i in range(1, 687):
        url = "https://www.cswu.cn/34/list" + str(i) + ".htm"
        pat(url, hd)
