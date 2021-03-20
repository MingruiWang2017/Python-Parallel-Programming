# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/13 14:22
@ desc: 测试非双工管道的单向性
        con1 只能接收；con2只能发送
"""
from multiprocessing import Process, Pipe

con1, con2 = Pipe(False)

try:
    con1.send("你好")
    r = con2.recv()
    print(r)
except BaseException as e:
    print(e)

try:
    con2.send("你好2")
    r = con1.recv()
    print(r)
except BaseException as e:
    print(e)