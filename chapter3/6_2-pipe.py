# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/13 11:08
@ desc: 使用管道进行进程间通信
        第一个管道，输入0-9这10个数字；
        第二个管道，输出这些数字的平方
"""
import multiprocessing


def create_items(pipe):
    """发送0-9这10个数字"""
    output_pipe, _ = pipe
    for item in range(10):
        output_pipe.send(item)
    output_pipe.close()


def multiply_items(pipe_1, pipe_2):
    """从管道1获取数据，求平方，再通过管道2发送"""
    close, input_pipe = pipe_1
    close.close()
    output_pipe, _ = pipe_2
    try:
        while True:
            item = input_pipe.recv()
            output_pipe.send(item * item)
    except EOFError:
        output_pipe.close()


if __name__ == '__main__':
    # 第一个管道输入数字
    pipe_1 = multiprocessing.Pipe(True)
    process_pipe_1 = multiprocessing.Process(
        target=create_items, args=(pipe_1,)
    )
    process_pipe_1.start()

    # 第二个管道从管道1中获取数字求平方，然会再发送出去
    pipe_2 = multiprocessing.Pipe(True)
    process_pipe_2 = multiprocessing.Process(
        target=multiply_items, args=(pipe_1, pipe_2,)
    )
    process_pipe_2.start()

    pipe_1[0].close()
    pipe_2[0].close()

    try:
        while True:
            print(pipe_2[1].recv())
    except EOFError as e:
        print("End")
