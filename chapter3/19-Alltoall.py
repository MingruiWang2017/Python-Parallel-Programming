# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/22 11:48
@ desc: 在一个通信器中，使用Alltoall方法，
        其中每个进程会向组中的其他进程发送一个数值类型的数组，
        也会从其他进程接收这样的数组。
"""
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

send_data = (rank + 1) * np.arange(size, dtype=int)
recv_data = np.empty(size, dtype=int)

comm.Alltoall(send_data, recv_data)

print("Process %s sending %s ; receiving %s" % (rank, send_data, recv_data))

# mpiexec -n 5 python 19-Alltoall.py
