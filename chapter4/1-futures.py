# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/4/30 17:26
@ desc: 有一个由数字1-10 组成的列表 number_list，
        针对列表中的每个元素，执行1000万次计数迭代（为了消耗时间），
        然后将得到的值与该元素相乘。
		然后，比较以下两种情况
			线性执行
			具备5个worker线程的线程池
			具备5个worker进程的进程池
"""

import concurrent.futures as cf
import time

number_list = [i for i in range(1, 11)]


def evaluate_item(x):
    # 计数，只是为了执行一些操作而已
    result_item = count(x)
    # 打印输入项及结果
    print("item " + str(x) + " result" + str(result_item))


def count(number):
    for i in range(0, 10000000):
        i += 1
    return i * number


if __name__ == '__main__':
    ## 线性执行
    start_time_1 = time.clock()
    for item in number_list:
        evaluate_item(item)
    print("Sequential execution in " +
          str(time.clock() - start_time_1) + "seconds")

    ## 线程池执行
    start_time_2 = time.clock()
    with cf.ThreadPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate_item, item)
    print("Thread pool execution in " +
          str(time.clock() - start_time_2) + "seconds")

    ## 进程池执行
    start_time_3 = time.clock()
    with cf.ProcessPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate_item, item)
    print("Process pool execution in " +
          str(time.clock() - start_time_3) + "seconds")
