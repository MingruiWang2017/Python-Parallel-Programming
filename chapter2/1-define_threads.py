# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/9 20:09
@ desc: 如何定义线程
"""
import threading
import time

def function(i):
    time.sleep(0.5)
    print("function called by thread %i" %i)
    return

threads = []

for i in range(5):
    t = threading.Thread(target=function, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()  # 等待线程结束
