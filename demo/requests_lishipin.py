# 1. 拿到contId
# 2. 拿到videoStatus返回的json -> 拿到srcURL
# 3. srcURL里面的内容进行修整
# 4. 下载视频

import requests 

url = "https://www.pearvideo.com/video_1796983"
conId = url.split("_")[1]

videoStatus = f"https://www.pearvideo.com/videoStatus.jsp?contId={conId}&mrd=0.419321808542203"
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
    # 防盗链：溯源，当前本次请求的上一级是谁
    "referer":url
}

resp = requests.get(videoStatus, headers=headers)
dic = resp.json()

srcUrl = dic["videoInfo"]["videos"]["srcUrl"]
systemTime = dic["systemTime"]
print(srcUrl)
srcUrl = srcUrl.replace(systemTime, f"cont-{conId}")
print(srcUrl)

# 下载视频
with open("D:/project/python/cap/a.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)