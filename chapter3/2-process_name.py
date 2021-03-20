# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/11 19:21
@ desc: 给进程命名
"""
import multiprocessing
import time


def foo():
    name = multiprocessing.current_process().name
    print("Starting %s" % name)
    time.sleep(2)
    print("Exiting %s" % name)


if __name__ == '__main__':
    process_with_name = multiprocessing.Process(
        name='foo_process',
        target=foo
    )
    # process_with_name.daemon = True  # 设置为守护进程

    process_with_default_name = multiprocessing.Process(target=foo)

    process_with_name.start()
    process_with_default_name.start()
    process_with_name.join()
    process_with_default_name.join()
