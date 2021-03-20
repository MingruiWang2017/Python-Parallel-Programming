# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/15 15:04
@ desc: 测试mpi4py
"""
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print("Hello world from process ", rank)


# 然后在终端中执行 mpiexec -n 5 python 10-hello_world.py
# 这将启动5个进程执行该程序