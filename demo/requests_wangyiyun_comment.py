

# 1. 找到未加密的参数
# 2. 想办法把参数进行加密（必须参考网易的逻辑做法），params，encSecKey 【【通过调用堆栈找到最后send发出的comment请求的函数，然后打断点，逆向查找加密参数，找到未加密和加密后的中间函数，然后找到加密函数】】
# 3. 请求到网易，拿到评论信息

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="


import requests
import json

# 请求方式是post
data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_2638631174",
    "threadId": "R_SO_4_2638631174",
}

# js处理加密过程 读懂下面加密操作后，我们用python写法代替下面的加密操作！
"""
    function a(a = 16) {    # 返回随机的16位字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)          # 循环16次
            e = Math.random() * b.length,   # 随机数
            e = Math.floor(e),              # 取整
            c += b.charAt(e);               # 取字符串中的xxx位置
        return c
    }
    function b(a, b) {  # a是要加密的内容，b是定值
        var c = CryptoJS.enc.Utf8.parse(b)  # c是密钥
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)  # e是数据
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,  # AES算法中iv是偏移量
            mode: CryptoJS.mode.CBC # 模式使用CBC模式
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);  # i就是一个包含16个字符的随机字符串
        h.encText = b(d, g),            # g是密钥   第一次加密
        h.encText = b(h.encText, i),    # 返回的就是params i也是密钥   第二次加密
        h.encSecKey = c(i, e, f),       # 返回的就是encSecKey, 因为e和f是定值，如果此时我把i固定，得到的key一定是固定的
        return h
    }
"""

# 服务于上面函数d
e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
i = "ElTuu7rPnRFGBVGZ"  # 这里i我固定了，原逻辑是随机的，为了方便起见固定该值

# 转化成16的倍数，为AES算法而服务
def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data

from Crypto.Cipher import AES   # 安装 pip install pycryptodome/pycrypto
from base64 import b64encode
# 加密过程
def enc_params(data, key): 
    iv = "0102030405060708"
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"),IV=iv.encode("utf-8"),mode=AES.MODE_CBC) # 创建加密器
    bs = aes.encrypt(data.encode("utf-8"))   # 加密 加密的内容的长度必须是16的倍数（AES要求）
    return str(b64encode(bs),"utf-8")   # 转化成字符串返回

# 由于i是固定了，那么encSecKey一定是固定的（根据原js代码的c函数逻辑推断）
def get_encSecKey():    
    return "567c56f56eba538402a4210cec11333d99ccc23859d4f002e47da190c71459698da651752c03d228cde696f0edcafa18c23ef895faa28c1b890715f91154650d93d9224272a02a0c7e79d32d0a2a6c0b8a0fdcf5db6aa3eb0252287ac28a9f112359d296b6fec7c8c7c567bd1acd3dfba4a18ccef7b659e9e79c44b44a9e7565"

# 把参数进行加密
def get_params(data):   # 默认这里data是字符串
    first = enc_params(data, g) # 第一次加密
    second = enc_params(first, i)   # 第二次加密
    return second   # 返回的就是params

# 发送请求得到结果
resp = requests.post(url, data={
    "params":get_params(json.dumps(data)),
    "encSecKey":get_encSecKey()
})

print(resp.text)