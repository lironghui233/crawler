
# 0. 安装 pip install bs4
# 1. 拿到页面源代码
# 2. 使用bs4进行解析，拿到数据

import requests
from bs4 import BeautifulSoup
import csv

# url = "http://www.xinfadi.com.cn/index.html"
url = "http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"
resp = requests.get(url)
print(resp.text)

f = open("菜价.csv", mode="w")
csvwriter = csv.writer(f)

# 解析数据
#1. 把页面源代码交给BeautifulSoup进行处理，生成bs对象
page = BeautifulSoup(resp.text, "html.parser") # 指定html解析器
#2. 从bs对象中查找数据
#find(标签，属性=值)
#findall(标签，属性=值)
# table = page.find("table",class_="hq_table") # class是python的关键字，因此查找属性class需要加下划线class_
table = page.find("table",attr={"class":"hq_table"}) # 和上一行是一个意思，此时可避免class
print(table)
# 拿到所有数据行
trs = table.find_all("tr")[1:]
for tr in trs: 
    tds = tr.find_all("td") #拿到每行的所有td
    name = tds[0].text # .text表示拿到被标签标记的内容
    low_price = tds[1].text # .text表示拿到被标签标记的内容
    avg_price = tds[2].text # .text表示拿到被标签标记的内容
    hight_price = tds[3].text # .text表示拿到被标签标记的内容
    gui = tds[4].text # .text表示拿到被标签标记的内容
    kind = tds[5].text # .text表示拿到被标签标记的内容
    date = tds[6].text # .text表示拿到被标签标记的内容
    print(name, low_price, avg_price, hight_price, gui, kind, date)
    csvwriter.writerow([name, low_price, avg_price, hight_price, gui, kind, date])

f.close()
print("over!")