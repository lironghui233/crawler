
# 1. 定位到2020必看片
# 2. 从2020必看片中提取到子页面的链接地址
# 3. 请求子页面的链接地址，拿到我们想要下载的地址


import requests
import re

domain = "https://www.dyttcn.com/"
resp = requests.get(domain, verify=False)
resp.encoding = 'gb2312' # 指定字符集
# print(resp.text)

# 拿到ul里面的li
obj1 = re.compile(r"最新更新.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名(?P<movie>.*?)</p>.*?<a href="(?P<download>.*?)">', re.S)

result1 = obj1.finditer(resp.text)
child_href_list = []
for it in result1:
    ul = it.group("ul")

    # 提取子页面链接
    result2 = obj2.finditer(ul)
    for itt in result2:
        # 拼接子页面的url地址： 域名+子页面地址
        child_href = domain + itt.group("href").strip("/")
        child_href_list.append(child_href)  # 把子页面链接保存起来


# 提取子页面内容
for href in child_href_list:
    child_resp = requests.get(href, verify=False)
    child_resp.encoding = "gb2312"
    print(child_resp.text)
    result3 = obj3.search(child_resp.text)
    print(result3.group("movie"))
    print(result3.group("download"))
    break 