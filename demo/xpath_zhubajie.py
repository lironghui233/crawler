# 拿页面源代码
# 提取和解析数据

import requests
from lxml import etree

url = "https://www.zbj.com/fw/?type=new&kw=saas"
headers ={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
}
resp = requests.get(url, headers=headers)
# print(resp.text)

# 解析
html = etree.HTML(resp.text)

# 拿到每一个服务商的div
divs = html.xpath('//*[@id="__layout"]/div/div[3]/div/div[4]/div/div[2]/div[1]/div[2]/div')
for div in divs:  # 每一个服务商信息
    price = div.xpath("./div/div[3]/div[1]/span[1]/text()")[0].strip("¥")
    title = div.xpath("./div/div[3]/div[2]/a[1]/span/text()")
    company_name = div.xpath("./div/div[5]/div/div/div[1]/text()")
    print(title)