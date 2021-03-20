# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/15 11:16
@ desc: 使用管理器载进程间管理状态
"""
import multiprocessing


def worker(dictionary, key, item):
    print("key = %s; item = %s" % (key, item))
    dictionary[key] = item


if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    dictionary = mgr.dict()
    jobs = [multiprocessing.Process(target=worker, args=(dictionary, i, i * 2))
            for i in range(10)]

    for job in jobs:
        job.start()
    for job in jobs:
        job.join()

    print("Results:", dictionary)
