# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/10 14:43
@ desc: 有两个线程，分别分producer（）与consumer（），
    它们共享一个共同资源，这是一个条目（item）。
    producer（）的任务是生成item，而consumer（）线程的任务则是使用所生成的item。
    如果item尚未生成，那么consumer（）线程就需要等待。
    当item生成后，producer（）线程会通知消费者资源可以使用了。
"""
import threading
import time
import random

# 可选参数为内部变量count，
# 默认值为1，如果其小于0，则抛出ValueError
semaphore = threading.Semaphore(0)


def consumer():
    print("consumer is waiting")
    # 获取信号量
    semaphore.acquire()
    # 消费者访问共享资源
    print("Consumer notify: consumed item number %s" % item)


def producer():
    global item
    time.sleep(1)
    item = random.randint(0, 100)
    print("producer notify: produced item number %s" % item)
    # 释放信号量，将内部的counter值加1.
    # 当其值等于0时，另一个线程就会再次等待它的值
    # 变为大于0，并唤醒该线程。
    semaphore.release()


if __name__ == '__main__':
    for i in range(0, 5):
        t1 = threading.Thread(target=producer)
        t2 = threading.Thread(target=consumer)
        t1.start()
        t2.start()
        t1.join()
        t2.join()

    print("program terminated")
