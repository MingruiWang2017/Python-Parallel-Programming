# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/15 10:34
@ desc: 使用Barrier 来同步两个进程，共有4个进程，其中1、2由屏障语句管理，3、4则没有使用同步指令。
"""
import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime


def test_with_barrier(synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    now = time()
    with serializer:
        print("process %s ---> %s" % (name, datetime.fromtimestamp(now)))


def test_without_barrier():
    name = multiprocessing.current_process().name
    now = time()
    print("process %s ---> %s" % (name, datetime.fromtimestamp(now)))


if __name__ == '__main__':
    synchronizer = Barrier(2)  # 参数2表示要管理的进程数量
    serializer = Lock()

    Process(name='p1 - test_with_barrier',
            target=test_with_barrier,
            args=(synchronizer, serializer)).start()
    Process(name='p2 - test_with_barrier',
            target=test_with_barrier,
            args=(synchronizer, serializer)).start()

    Process(name='p3 - test_without_barrier',
            target=test_without_barrier).start()
    Process(name='p4 - test_without_barrier',
            target=test_without_barrier).start()
