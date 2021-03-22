# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/22 10:50
@ desc: 使用scatter将不同数据发送给不同进程
"""
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    array_to_share = range(1, 11)
else:
    array_to_share = None

recvbuf = comm.scatter(array_to_share, root=0)
print("Process = %d recvbuf = %d" % (rank, recvbuf))

# mpiexec -n 10 python 17-scatter.py
