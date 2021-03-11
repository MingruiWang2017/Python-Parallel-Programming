# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/11 14:38
@ desc: 生成并使用进程
"""
import multiprocessing


def foo(i):
    print("called function foo in process: %s" % i)
    return


if __name__ == '__main__':
    process_jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=foo, args=(i,))
        process_jobs.append(p)
        p.start()

    for _ in process_jobs:
        _.join()
