# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/22 11:14
@ desc: 使用gather 实现聚合通信，
        每个进程构建自己的数据发送给root进程，root进程收集数据
"""
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()  # 获取MPI通信器的进程数

data = (rank + 1) ** 2
data = comm.gather(data, root=0)
if rank == 0:
    print("rank = %d receiving data from other process" % rank)

    for i in range(1, size):
        value = data[i]
        print("Process %d receiving %s from process %s"
              % (rank, value, i))

# mpiexec -n 5 python 18-gather.py
