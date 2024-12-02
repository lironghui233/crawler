
# import time 

# def func():
#     print("我爱黎明")
#     time.sleep(3)   #让当前线程处于阻塞状态，让出了CPU时间片
#     print("我爱黎明2")

# if __name__ == '__main__':
#     func()


# requests.get(bilibili) 在网络请求返回数据之前，程序也是处于阻塞状态的


###
###
###
# python编写协程的程序
###
###
###

import time 
import asyncio

async def func():
    print("你好啊，我叫爱丽丝")

async def func1():
    print("你好啊，我叫吴尊")
#     time.sleep(3)                       # 当程序出现了同步操作的时候，异步就中断了
    await asyncio.sleep(3)                         # 异步睡眠，让出当前协程
    print("你好啊，我叫吴尊2")

async def func2():
    print("你好啊，我叫吴彦祖")
#     time.sleep(3)                       # 当程序出现了同步操作的时候，异步就中断了
    await asyncio.sleep(2)                         # 异步睡眠，让出当前协程
    print("你好啊，我叫吴彦祖2")

async def func3():
    print("你好啊，我叫黄晓明")
#     time.sleep(3)                       # 当程序出现了同步操作的时候，异步就中断了
    await asyncio.sleep(5)                         # 异步睡眠，让出当前协程
    print("你好啊，我叫黄晓明2")

if __name__ == '__main__':
#     g = func()           # 此时的函数是异步协程函数，此时函数执行得到的是一个协程对象
#     print(g)             # <coroutine object func at 0x000001E2D3C09A10>
#     asyncio.run(g)       # 执行协程函数，协程程序运行需要asyncio模块的支持

     f1 = func1()
     f2 = func2()
     f3 = func3()
     tasks = [f1, f2, f3]

     t1 = time.time()
     
     # 一次性启动多个任务（协程）
     asyncio.run(asyncio.wait(tasks))
     
     t2 = time.time()
     print(t2- t1)