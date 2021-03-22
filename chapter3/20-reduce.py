# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/22 14:29
@ desc: 使用汇聚操作MPI.SUM计算一组数据元素的和
"""
import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

array_size = 3
recv_data = np.zeros(array_size, dtype=int)
send_data = (rank + 1) * np.arange(size, dtype=int)
print("Process %d sending %s" % (rank, send_data))

comm.Reduce(send_data, recv_data, root=0, op=MPI.SUM)
print("on task %d after Reduce: data = %s" % (rank, recv_data))

# mpiexec -n 3 python 20-reduce.py
