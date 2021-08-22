import pycuda.driver as cuda
# 自动根据GPU 可用性和数量选择要使用的GPU。
# 这也将创建一个在接下来的代码运行中所需的GPU上下文。
# 如果需要，选中的设备和创建的上下文均可从pycuda.autoinit中访问，并用作可导入的标识
import pycuda.autoinit
from pycuda.compiler import SourceModule

import numpy as np

a = np.random.randn(5,5)
a = a.astype(np.float32) # 转换为单精度模式
a_gpu = cuda.mem_alloc(a.nbytes)  # 分配设备上的内存
cuda.memcpy_htod(a_gpu, a)  # 从host向device复制内存

# SourceModule组件则是一个必须编写GPU所需的类C代码的对象
mod = SourceModule("""
  __global__ void doubleMatrix(float *a){
      int idx = threadIdx.x + threadIdx.y*5;
      a[idx] *=2;
  }
""")

func = mod.get_function("doubleMatrix")
func(a_gpu, block=(5, 5, 1))

a_double = np.empty_like(a)
cuda.memcpy_dtoh(a_double, a_gpu) #  从device向host复制内存
print("ORIGINAL MATRIX:")
print(a)
print("DOUBLE MATRIX AFTER PyCUDA EXECUTION")
print(a_double)