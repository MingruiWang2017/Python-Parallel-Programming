# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/9 19:51
@ desc: python多线程示例
"""
from threading import Thread
from time import sleep


# 创建一个类集成Thread类
class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.message = "Hello Parallel Python CookBook!!\n"

    def print_message(self):
        print(self.message)

    # 重写run方法, 打印10次message
    def run(self):
        print("Thread Starting")
        x = 0
        while x < 10:
            self.print_message()
            sleep(1)
            x += 1
        print("Thread Ended")


# 开启主进程
print("Process Started")
# 实例化MyThread类
my_thread = MyThread()
# 启动线程，通过start方法调用run方法，打印消息
my_thread.start()
# 进程结束
print("Process Ended")
