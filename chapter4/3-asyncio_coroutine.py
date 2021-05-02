# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/5/1 10:04
@ desc: 使用Asyncio协程来模拟有限状态机
"""
import asyncio
import time
from random import randint


@asyncio.coroutine  # 标记为协程
def start_state():  # 自动机的状态S0
    print("Start state called")
    input_value = randint(0, 1)
    time.sleep(1)
    if input_value == 0:
        result = yield from state2(input_value)  # 调用下一个协程
    else:
        result = yield from state1(input_value)
    print("Resume of Transition: \nStart state calling " + result)


@asyncio.coroutine
def state1(transition_value):
    output_value = "State 1 with transition value = %s\n" % transition_value
    input_value = randint(0, 1)
    time.sleep(1)
    print("...Evaluating...")
    if input_value == 0:
        result = yield from state3(input_value)
    else:
        result = yield from state2(input_value)
    result = "State 1 calling " + result
    return output_value + result


@asyncio.coroutine
def state2(transition_value):
    output_value = "State 2 with transition value = %s\n" % transition_value
    input_vaue = randint(0, 1)
    time.sleep(1)
    print("...Evaluating...")
    if input_vaue == 0:
        result = yield from state1(transition_value)
    else:
        result = yield from state3(transition_value)
    result = "State 2 calling " + result
    return output_value + result


@asyncio.coroutine
def state3(transition_value):
    output_value = "State 3 with transition value = %s\n" % transition_value
    input_value = randint(0, 1)
    time.sleep(1)
    print("...Evaluating...")
    if input_value == 0:
        result = yield from state1(input_value)
    else:
        result = yield from end_state(input_value)
    result = "State 3 calling " + result
    return output_value + result


@asyncio.coroutine
def end_state(transition_value):  # S4
    output_value = "End state 4 with transition value = %s\n" % transition_value
    print("...Stop computing...")
    return output_value


if __name__ == '__main__':
    print("Finite State Machine simulation with Asyncio Coroutine")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_state())
