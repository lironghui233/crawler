
# <video src="不能播的视频.mp4"></video>
# 一般视频网站是怎么做的？
# 用户上传 —> 转码（把视频做处理，2K，1080，标清） -> 切片处理（把单个的文件进行拆分）
# 用户在进行拉动进度条的时候
# ==========/===========/==========/========
# 需要一个文件记录： 1. 视频播放顺序 2.视频存放的路径
# M3U8 txt json => 文本


# 想要抓取一个视频：
# 1. 找到m3u8（各种手段）
# 2. 通过m3u8下载ts文件
# 3。可以通过各种手段（不仅仅是编程手段） 把多个ts文件合并为一个mp4文件


"""
流程：
    1. 拿到548121-1-1.html的页面源代码
    2. 从源代码中提取到m3u8的url
    3. 下载m3u8
    4. 读取m3u8文件，下载视频
    5. 合并视频
"""

import requests
import re

obj = re.compile(r"url: '(?P<url>.*?)'", re.S) # 用来提取m3u8的url地址

url = "https://www.91kanju.com/vod-play/54812-1-1.html"

resp = requests.get(url)
m3u8_url = obj.search(resp.text).group("url") # 拿到m3u8的地址
print(m3u8_url)

# 下载m3u8文件
resp2 = requests.get(m3u8_url)

with open("test.m3u8", mode="wb") as f:
    f.write(resp2.content)

resp2.close()
print("下载完毕")


# 解析m3u8文件
n = 1
with open("test.m3u8", mode="r") as f:
    for line in f :
        line = line.strip() # 先去掉空格，空白，换行符
        if line.startswith("#"): # 如果以#开头
            continue
        
        # 下载视频片段
        # 同步阻塞方式下载
        resp3 = requests.get(line)
        f = open(f"{n}.ts", mode="wb")
        f.write(resp3.content)
        f.close()
        resp3.close()
        n+=1
        print("完成了一个")


# 合并视频
# 外部第三方软件合并