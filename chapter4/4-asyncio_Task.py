# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/5/1 16:59
@ desc: 通过Task并发执行3个数学函数
"""
import asyncio


@asyncio.coroutine
def factorial(number):
    """阶乘"""
    f = 1
    for i in range(2, number + 1):
        print("Asyncio.Task: Compute factorial(%s)" % i)
        yield from asyncio.sleep(1)
        f *= i
    print("Asyncio.Task - factorial(%s) = %s" % (number, f))


@asyncio.coroutine
def fibonacci(number):
    """斐波那契数列"""
    a, b = 0, 1
    for i in range(number):
        print("Asyncio.Task: compute fibonacci (%s)" % i)
        yield from asyncio.sleep(1)
        a, b = b, a + b
    print("Asyncio.Task - fibonacci(%s) = %s" % (number, a))


@asyncio.coroutine
def binomial_coeff(n, k):
    """二项式系数 site：https://cnblogs.com/huyuchengus/p/10198603.html
    B(n,k) = factorial(n) / (factorial(k) * factorial(n-k))
           = n! / k! * (n-k)!
    """
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) / i
        print("Asyncio.Task：compute binomialCoeff (%s)" % i)
        yield from asyncio.sleep(1)
    print("Asyncio.Task - binomialCoeff(%s, %s) = %s" % (n, k, result))


if __name__ == '__main__':
    # 将3个协程方法设置为并行任务
    tasks = [asyncio.Task(factorial(10)),
             asyncio.Task(fibonacci(10)),
             asyncio.Task(binomial_coeff(20, 10))]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))  # 等待协程任务执行完成
    loop.close()
