

from threading import Thread

def func(name):
    for i in range(1000):
        print(name, i)

if __name__ == '__main__':
    t1 = Thread(target=func, args=('周杰伦',)) # 创建线程，并给线程安排任务  #传参必须是元组
    t1.start() # 多线程状态为可以开始工作状态，具体的执行时间由CPU决定

    t2 = Thread(target=func, args=('王力宏',)) # 创建线程，并给线程安排任务  #传参必须是元组
    t2.start() # 多线程状态为可以开始工作状态，具体的执行时间由CPU决定

    for i in range(1000):
        print("main", i)