# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/9 20:28
@ desc: 确定使用的哪个线程
"""
import threading
import time


def first_func():
    print(threading.current_thread().getName() + ' is starting')
    time.sleep(2)
    print(threading.current_thread().getName() + ' is exiting')
    return


def second_func():
    print(threading.current_thread().getName() + ' is starting')
    time.sleep(2)
    print(threading.current_thread().getName() + ' is exiting')
    return


def third_func():
    print(threading.current_thread().getName() + ' is starting')
    time.sleep(2)
    print(threading.current_thread().getName() + ' is exiting')
    return


if __name__ == '__main__':
    t1 = threading.Thread(name='first_func', target=first_func)
    t2 = threading.Thread(name='second_func', target=second_func)
    t3 = threading.Thread(name='third_func', target=third_func)

    t1.start()
    t2.start()
    t3.start()
