
import time 
import asyncio


## 在爬虫领域的应用
async def download(url):
    print("准备开始下载")
    await asyncio.sleep(2)            # 网络请求
    print("下载完成")

async def main():
    urls = [
        "http://www.baidu.com",
        "http://www.bilibili.com",
        "http://www.163.com"
    ]
    
    tasks = []              # 协程对象list
    for url in urls:
        d = download(url)   # 得到一个协程对象
        tasks.append(d)

    await asyncio.wait(tasks)      # 会阻塞当前协程，直到 tasks 中所有的任务都完成（无论是正常结束还是抛出异常）。 ## 等待多个异步任务完成

if __name__ == '__main__':
    # 一次性启动多个任务（协程）
    asyncio.run(main())
