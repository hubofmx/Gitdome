import requests
url="https://www.cqc.edu.cn/34/list1.htm"
hd = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56"}
r = requests.get(url,headers=hd)
print(r.text)
