

# （正向）代理 原理： 通过第三方的一个机器去发送请求

import requests

# 27.185.0.164:999
proxies = {
    "http":"http://27.185.0.164:999"
}

resp = requests.get("https://www.baidu.com", proxies=proxies)
resp.encoding = 'utf-8'
print(resp.text)