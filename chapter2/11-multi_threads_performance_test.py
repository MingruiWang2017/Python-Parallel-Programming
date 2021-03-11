# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/11 10:05
@ desc: 多线程性能评价
"""
import os
from threading import Thread
from timeit import Timer
import requests


class ThreadsObject(Thread):
    def run(self):
        function_to_run()


class NoThreadsObject(object):
    def run(self):
        function_to_run()


def non_threaded(num_iter):
    """使用单线程执行func"""
    funcs = []
    for i in range(int(num_iter)):
        funcs.append(NoThreadsObject())
    for i in funcs:
        i.run()


def threaded(num_threads):
    funcs = []
    for i in range(int(num_threads)):
        funcs.append(ThreadsObject())
    for i in funcs:
        i.start()
    for i in funcs:
        i.join()


def function_to_run():
    func4()


def func1():
    pass


def func2():
    a, b = 0, 1
    for _ in range(10000):
        a, b = b, a + b


def func3():
    with open("test.dat", "r", encoding="utf8") as fh:
        for _ in range(1000):
            fh.readline()


# def write_data():
#     if os.path.exists("test.dat"):
#         return
#     with open("test.dat", 'w', encoding='utf8') as f:
#         for i in range(1000):
#             f.write(str([random.random() for _ in range(10)]) + "\n")


def func4():
    for i in range(3):
        resp = requests.get("http://www.baidu.com/")
        resp.status_code
        resp.close()


def show_results(func_name, results):
    print("%-23s %4.6f seconds" % (func_name, results))


if __name__ == '__main__':
    repeat = 100
    number = 1
    num_threads = [1, 2, 4, 8]

    print("Starting tests:::\n")
    for i in num_threads:
        #  测试单线程情况
        t = Timer("non_threaded(%s)" % i,  # 使用反射调用non_threaded()方法
                  "from __main__ import non_threaded")
        best_result = min(t.repeat(repeat=repeat, number=number))  # 重复repeat次timeit计时，取其中最小的
        show_results("\033[34;1m non_threaded (%s iters)\033[0m" % i, best_result)

        #  测试多线程情况
        t = Timer("threaded(%s)" % i,  # 使用反射调用threaded()方法
                  "from __main__ import threaded")
        best_result = min(t.repeat(repeat=repeat, number=number))
        show_results("\033[35;1m threaded(%s threads)\033[0m" % i, best_result)
    print("\nIterations complete!!!")
