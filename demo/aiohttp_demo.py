
# request.get() 同步代码 --> 异步操作 aiohttp

# pip install aiohttp

import asyncio
import aiohttp
# from aiohttp import ClientSession

urls = [
    "https://i1.huishahe.com/uploads/allimg/202205/9999/eca5519e81.jpg",
    "https://i1.huishahe.com/uploads/tu/201909/9999/a43e195069.jpg",
    "https://i1.huishahe.com/uploads/tu/201911/9999/9c871bca57.jpg"
]

async def aiodownload(url):
    name = url.rsplit("/", 1)[1]
    async with aiohttp.ClientSession() as session:  # 相当于 requests
        async with session.get(url) as resp:    # 相当于 resp = requests.get()
            # 请求回来了，写入文件
            # 下面其实可以使用 aiofiles 替换
            with open(name, mode="wb") as f:    # 创建文件
                f.write(await resp.content.read() ) # 读取内容是异步的，需要await挂起
    print(name, "finish")

async def main():
    tasks = []
    for url in urls:
        tasks.append(aiodownload(url))

    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())