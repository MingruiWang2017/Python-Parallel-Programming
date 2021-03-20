# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/11 18:48
@ desc: 调用target的进程
"""
import multiprocessing
import target_function

if __name__ == '__main__':
    process_jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=target_function.function, args=(i,))
        process_jobs.append(p)
        p.start()

    for p in process_jobs:
        p.join()