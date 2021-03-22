# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/22 16:43
@ desc: 创建螺旋的笛卡尔拓扑
"""
import numpy as np
from mpi4py import MPI

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
neighbor_processes = [0, 0, 0, 0]

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.rank
    size = comm.size

    grid_rows = int(np.floor(np.sqrt(comm.size)))  # 行数为对size 开方后取整数部分
    grid_cols = comm.size // grid_rows  # 列数为size 整除行数

    if grid_rows * grid_cols > size:
        grid_cols -= 1
    if grid_rows * grid_cols > size:
        grid_rows -= 1

    if rank == 0:
        print("Building a %d x %d grid topology:" % (grid_rows, grid_cols))

    # 创建笛卡尔拓扑
    cartesian_communicator = comm.Create_cart(
        (grid_rows, grid_cols), periods=(True, True), reorder=True)

    # 找到rank在拓扑中的位置
    my_mpi_row, my_mpi_col = cartesian_communicator.Get_coords(
        cartesian_communicator.rank)
    # 通过shift方法进行平移，找到rank上下左右的相邻节点
    # 第一个参数表示平移的维度（0为行，1为列...），第二个参数表示位移量
    # 方法返回平移的源进程号和目的进程号
    neighbor_processes[UP], neighbor_processes[DOWN] = \
        cartesian_communicator.Shift(0, 1)
    neighbor_processes[LEFT], neighbor_processes[RIGHT] = \
        cartesian_communicator.Shift(1, 1)

    print("""Process = %s 
          row = %s
          column = %s ----> 
          neighbor_processes[UP]   = %s  neighbor_processes[DOWN]  = %s
          neighbor_processes[LEFT] = %s  neighbor_processes[RIGHT] = %s"""
          % (rank, my_mpi_row, my_mpi_col,
             neighbor_processes[UP], neighbor_processes[DOWN],
             neighbor_processes[LEFT], neighbor_processes[RIGHT]))

# mpiexec -n 4 python 21-create_cart.py