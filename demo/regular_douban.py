
# 1. 拿到页面源代码 requests
# 2. 通过re来提取想要的有效信息 re

import requests
import re
import csv

url = "https://movie.douban.com/top250"

headers = {
    "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36 Edg/130.0.0.0"
}

resp = requests.get(url, headers=headers)
page_content = resp.text

# 解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
                 r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                 r'<span>(?P<number>.*?)人评价</span>', re.S)
# 开始匹配
result = obj.finditer(page_content)

#需要保存的文件
f = open("./data.csv", mode="w") 
csvwriter = csv.writer(f)

#遍历并保存
for it in result:
    print(it.group("name"))
    print(it.group("score"))
    print(it.group("number"))
    print(it.group("year").strip())
    dic = it.groupdict()
    dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values())
f.close()
print("over!")