# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/10 11:26
@ desc: 代码中有两个函数，分别是incre-ment（）与decrement（）。
    前者会增加共享资源的值，后者则会减少其值，每个函数都被插入到适合的线程中。
    每个函数都有一个循环，分别用来重复增加或是减少共享资源的值。
    确保通过对共享资源的恰当管理，让执行的结果等于共享变量的值，该共享变量的初始值为0。
"""
import threading

shared_resource_with_lock = 0
shared_resource_with_no_lock = 0
COUNT = 100000
shared_resource_lock = threading.Lock()


# 锁管理
def increment_with_lock():
    global shared_resource_with_lock
    for i in range(COUNT):
        shared_resource_lock.acquire()
        shared_resource_with_lock += 1
        shared_resource_lock.release()


def decrement_with_lock():
    global shared_resource_with_lock
    for i in range(COUNT):
        shared_resource_lock.acquire()
        shared_resource_with_lock -= 1
        shared_resource_lock.release()

# 没有锁管理
def increment_without_lock():
    global shared_resource_with_no_lock
    for i in range(COUNT):
        shared_resource_with_no_lock += 1


def decrement_without_lock():
    global shared_resource_with_no_lock
    for i in range(COUNT):
        shared_resource_with_no_lock -= 1


if __name__ == "__main__":
    t1 = threading.Thread(target=increment_with_lock)
    t2 = threading.Thread(target=decrement_with_lock)
    t3 = threading.Thread(target=increment_without_lock)
    t4 = threading.Thread(target=decrement_without_lock)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print("the value of shared variable with lock managment is %d" %shared_resource_with_lock)
    print("the value of shared variable with race condition is %d" %shared_resource_with_no_lock)