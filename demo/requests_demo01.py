

import requests

query = input("请输入一个你喜欢的明星")

url = f'https://www.sogou.com/web?query={query}'

headers = {
    "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36 Edg/130.0.0.0"
} #伪装我是浏览器请求。

resp = requests.get(url, headers=headers)
print(resp)
print(resp.text) #拿到页面源码