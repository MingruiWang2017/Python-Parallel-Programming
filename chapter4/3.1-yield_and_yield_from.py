# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/5/1 14:02
@ desc: yield与yield from用法
"""


# 用yield方式来生成斐波那契数列
def fab(max):
    n = 0
    a, b = 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1


def f_yield(iterator):
    for i in iterator:
        yield i


print("yield:")
f = f_yield(fab(5))
for n in f:
    print(n, end=" ")


# yield from 方式等同于for item in iterable; yield item的缩写版
# 主要用在多层yield嵌套使用时，用来降低程序复杂度
def f_yield_from(iterator):
    yield from iterator


print("\n\nyield from:")
f_2 = f_yield_from(fab(5))
for i in f_2:
    print(i, end=" ")

print("\n\nyield from包含多个子程序:")
def gen(x):
    yield from range(x, 0, -1)
    yield from range(x + 1)


print(list(gen(5)))
for g in gen(6):
    print(g, end=",")
