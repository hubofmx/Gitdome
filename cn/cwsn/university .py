import requests
from bs4 import BeautifulSoup
url4="https://www.shanghairanking.cn/rankings/bcur/2022"
hd = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
r=requests.get(url4,headers=hd)
r.encoding="utf-8"
soup=BeautifulSoup(r.text,"html.parser")
w1=soup.select("#content-box > div.rk-table-box > table > tbody > tr > td:nth-child(1) > div")
w2=soup.select("#content-box > div.rk-table-box > table > tbody > tr > td.align-left > div > div.univname > div:nth-child(1) > div > div > a")
w3=soup.select("#content-box > div.rk-table-box > table > tbody > tr > td:nth-child(5)")
list1 = []
list2 = []
list3 = []
for i in range(0,len(w1)):
    list1.append(w1[i].string)
    list2.append(w2[i].string)
    list3.append(w3[i].string)

list4=[x.strip() for x in list1]
list5=[x.strip() for x in list2]
list6=[x.strip() for x in list3]
l7=['排名','名字','总分']
for i in range(len(w1)):
    l7.append(list4[i])
    l7.append(list5[i])
    l7.append(list6[i])

with open ("D:/temp/pc/nice_college.txt","w+",encoding="utf-8") as q :
    for i in range(0,len(l7)):
        if (i + 1) % 3 == 0:
            q.write(l7[i] + '\n')
        else:
            q.write(l7[i] + '\t\t\t\t')
print("写入成功")