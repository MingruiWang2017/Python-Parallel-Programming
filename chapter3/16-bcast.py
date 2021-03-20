# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/20 16:44
@ desc: 使用广播在消息器中发送相同信息
"""
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

if rank == 0:
    variable_to_share = 1000
else:
    variable_to_share = None

variable_shared = comm.bcast(variable_to_share, root=0)
print("process= %d, variable shared = %s " % (rank, variable_shared))

# mpiexec -n 10 python 16-bcast.py
