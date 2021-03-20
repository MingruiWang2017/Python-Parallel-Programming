# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/11 19:33
@ desc: 在后台运行进程
"""
import multiprocessing
import time


def foo():
    name = multiprocessing.current_process().name
    print("Starting %s" %name)
    time.sleep(2)
    print("Exiting %s" %name)


if __name__ == '__main__':
    background_process = multiprocessing.Process(
        name='background_process',
        target=foo
    )
    background_process.daemon = True

    no_background_process = multiprocessing.Process(
        name='No_backgroun_process',
        target=foo
    )
    no_background_process.daemon = False

    background_process.start()
    no_background_process.start()