# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/15 11:26
@ desc: 使用进程池
"""
import multiprocessing


def function_square(data):
    print("worker: %s" %multiprocessing.current_process().name)
    return data ** 2


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=4)  # 创建一个含有4个进程的进程池
    pool_outputs = pool.map(function_square, list(range(10)))  # 从进程池中获取进程并执行方法
    pool_outputs2 = pool.map_async(function_square, list(range(10, 20))).get()  # 使用map_async方法需要get() 结果

    pool.close()
    pool.join()  # pool必须先close，再调用join
    print("Pool: ", pool_outputs)
    print("Pool2: ", pool_outputs2)

