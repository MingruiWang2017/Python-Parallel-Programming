# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/5/1 9:22
@ desc: 使用Asyncio的异步事件循环创建一个异步模式的应用
"""
import asyncio
import datetime
import time


def function_1(end_time, loop):
    print("Function 1 called")
    if loop.time() + 1.0 < end_time:
        loop.call_later(1, function_2, end_time, loop)
    else:
        loop.stop()


def function_2(end_time, loop):
    print("Function 2 called")
    if loop.time() + 1.0 < end_time:
        loop.call_later(1, function_3, end_time, loop)  # 延迟1秒后调用function_2
    else:
        loop.stop()


def function_3(end_time, loop):
    print("Function 3 called")
    if loop.time() + 1.0 < end_time:
        loop.call_later(1, function_1, end_time, loop)
    else:
        loop.stop()


def function_4(end_time, loop):
    print("Function 4 called")
    if loop.time() + 1.0 < end_time:
        loop.call_later(1, function_1, end_time, loop)
    else:
        loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()  # 获取整个事件循环
    end_loop = loop.time() + 9.0

    loop.call_soon(function_1, end_loop, loop)  # 立即调用function_1
    # loop.call_soon(function_4, end_loop, loop)

    loop.run_forever()  # 一直执行知道stop()被调用
    loop.close()
