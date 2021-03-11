# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/10 18:17
@ desc: 使用with来测试threading中的对象
"""
import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(threadName)-10s %(message)s',)

def threading_with(statement):
    with statement:
        logging.debug('%s acquired via with' % statement)


def threading_not_with(statement):
    statement.acquire()
    try:
        logging.debug('%s acquired directly' % statement)
    finally:
        statement.release()


if __name__ == '__main__':
    # 创建一个测试组合
    threading_synchronization_list = [
        threading.Lock(),
        threading.RLock(),
        threading.Condition(),
        threading.Semaphore(1)
    ]

    # 在for循环中，调用threading_with与threading_no_with方法
    for statement in threading_synchronization_list:
        t1 = threading.Thread(target=threading_with, args=(statement,))
        t2 = threading.Thread(target=threading_not_with, args=(statement,))

        t1.start()
        t2.start()
        t1.join()
        t2.join()