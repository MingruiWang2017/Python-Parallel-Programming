# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/12 17:09
@ desc: 实现进程子类
"""
import multiprocessing


class MyProcess(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)

    def run(self):
        print("called run method in process: %s" % self.name)
        return


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = MyProcess()
        jobs.append(p)
        p.start()

    for p in jobs:
        p.join()
