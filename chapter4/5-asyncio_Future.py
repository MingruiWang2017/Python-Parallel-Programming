# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/5/2 9:36
@ desc: 使用Future管理两个协程任务
        两个任务分别计算前n个整数之和与n的阶乘
"""
import asyncio


@asyncio.coroutine
def firt_coroutine(future: asyncio.Future, n: int):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    yield from asyncio.sleep(1)
    # 将协程结果设置给future
    future.set_result("first coroutine (sum of N integers) result = %d" % sum)


@asyncio.coroutine
def second_coroutine(future: asyncio.Future, n: int):
    result = 1
    for i in range(2, n + 1):
        result *= i
    yield from asyncio.sleep(2)
    future.set_result("second coroutine (factorial) result = %d" % result)


def get_result(future: asyncio.Future):
    print(future.result())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    future1 = asyncio.Future()
    future2 = asyncio.Future()

    # 将协程关联到future
    tasks = [firt_coroutine(future1, 100),
             second_coroutine(future2, 10)]

    # 为future添加执行完成之后的回调方法
    future1.add_done_callback(get_result)
    future2.add_done_callback(get_result)
    # 等待协程任务执行完成
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
