
import time 
import asyncio

async def func1():
    print("你好啊，我叫吴尊")
    await asyncio.sleep(3)                         # 异步睡眠，让出当前协程
    print("你好啊，我叫吴尊2")

async def func2():
    print("你好啊，我叫吴彦祖")
    await asyncio.sleep(2)                         # 异步睡眠，让出当前协程
    print("你好啊，我叫吴彦祖2")

async def func3():
    print("你好啊，我叫黄晓明")
    await asyncio.sleep(5)                         # 异步睡眠，让出当前协程
    print("你好啊，我叫黄晓明2")


async def main():
    # 第一种写法
    # f1 = func1()    
    # await f1            # 一般await挂起操作放在协程对象前面
    # f2 = func1()    
    # await f2            # 一般await挂起操作放在协程对象前面
    # f3 = func1()    
    # await f3            # 一般await挂起操作放在协程对象前面

    # 第二种写法（推荐）
    tasks = [
        asyncio.create_task(func1()),  # python3.8后加上asyncio.create_task()
        asyncio.create_task(func2()),  
        asyncio.create_task(func3()), 
    ]
    await asyncio.wait(tasks)

if __name__ == '__main__':
    t1 = time.time()

    # 一次性启动多个任务（协程）
    asyncio.run(main())
     
    t2 = time.time()
    print(t2-t1)



