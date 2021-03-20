# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/20 15:38
@ desc: 使用mpi4py进行进程间的点对点通信
"""
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
print("my rank is : ", rank)

if rank == 0:
    data = 1000000
    destination_process = 4
    comm.send(data, dest=destination_process)
    print("Sending data: %s to process %d" % (data, destination_process))

if rank == 1:
    destination_process = 8
    data = "hello"
    comm.send(data, dest=destination_process)
    print("Sending data: %s to process %d" % (data, destination_process))

if rank == 4:
    data = comm.recv(source=0)
    print("Received data: %s" %data)

if rank == 8:
    data = comm.recv(source=1)
    print("Received data: %s" %data)

# 在cmd中启动9个进程
# mpiexec -n 9 python 11-p2p_comm.py