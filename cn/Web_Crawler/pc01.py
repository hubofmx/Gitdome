import requests
hd = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
url1="https://www.sogou.com/web?query=%E8%83%A1%E5%8D%9A"
request = requests.get(url=url1,headers=hd)
data_text=request.text
print(data_text)
with open("D:/temp/pc/tao.html","w+",encoding="utf-8") as f :
    f.write(data_text)
print("爬取结束！")