# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/20 15:58
@ desc: 这段代码，会引入一个典型的死锁问题：两个进程，其rank分别为 1 和 5,
        他们之间彼此通信，各自都拥有数据发送和接收的功能
"""
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print("My rank is: ", rank)

if rank == 1:
    data_send = 'a'
    destination_process = 5
    source_process = 5

    data_received = comm.recv(source=source_process)
    comm.send(data_send, dest=destination_process)

    print("Sending data %s to process %d" % (data_send, destination_process))
    print("Received data %s" % data_received)

if rank == 5:
    data_send = 'b'
    destination_process = 1
    source_process = 1

    data_received = comm.recv(source=source_process)
    comm.send(data_send, dest=destination_process)

    print("Sending data %s to process %d" % (data_send, destination_process))
    print("Received data %s" % data_received)

# 在cmd中启动6个进程执行脚本
# mpiexec -n 6 python 12-dead_lock_problem.py
