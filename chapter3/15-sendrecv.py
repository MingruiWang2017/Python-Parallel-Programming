# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/20 16:29
@ desc: 使用sendrecv方法解决死锁问题
"""
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print("My rank is ", rank)

if rank == 1:
    data_send = 'a'
    destination_process = 5
    source_process = 5
    data_received = comm.sendrecv(data_send, dest=destination_process,
                                  source=source_process)
    print("rank 1: send: %s ,recv: %s" % (data_send, data_received))

if rank == 5:
    data_send = 'b'
    destination_process = 1
    source_process = 1
    data_received = comm.sendrecv(data_send, dest=destination_process,
                                  source=source_process)
    print("rank 5: send: %s ,recv: %s" % (data_send, data_received))

# mpiexec -n 6 python 15-sendrecv.py