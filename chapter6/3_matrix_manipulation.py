import numpy as np
from numpy.core.shape_base import block
from pycuda import driver, compiler, gpuarray, tools

# 初始化设备
import pycuda.autoinit

MATRIX_SIZE = 5

kernel_code_templete= """
__global__ void MatrixMulKernel(float *a, float *b, float *c){
    int tx = threadIdx.x;
    int ty = threadIdx.y;
    float Pvalue = 0;
    for (int k=0; k < %(MATRIX_SIZE)s; ++k){
        float Aelement = a[tx * %(MATRIX_SIZE)s + k];
        float Belement = b[k * %(MATRIX_SIZE)s + ty];
        Pvalue += Aelement * Belement;
    }
    c[tx * %(MATRIX_SIZE)s + ty] = Pvalue;
}
"""
# 以上是加载给device的kernel，因为thread是并行的，
# 所以不需要为tx和ty进行循环，每个tx和ty会使用一个thread

# 产生数据
a_cpu = np.random.randn(MATRIX_SIZE, MATRIX_SIZE).astype(np.float32)
b_cpu = np.random.randn(MATRIX_SIZE, MATRIX_SIZE).astype(np.float32)
c_cpu = np.dot(a_cpu, b_cpu)  # 使用cpu计算相乘结果

a_gpu = gpuarray.to_gpu(a_cpu)
b_gpu = gpuarray.to_gpu(b_cpu)
c_gpu = gpuarray.empty((MATRIX_SIZE, MATRIX_SIZE), np.float32)

# 为kernel代码字符串中的字符占位符填充数据
kernel_code = kernel_code_templete % {
    "MATRIX_SIZE": MATRIX_SIZE
}

# 定义内核函数并获取执行函数的标识
mod = compiler.SourceModule(kernel_code)
matrix_mul = mod.get_function("MatrixMulKernel")

# 调用标识进行计算，同时指定block大小
matrix_mul(
    a_gpu, b_gpu,
    c_gpu,
    block = (MATRIX_SIZE, MATRIX_SIZE, 1)
)

# 打印结果
print("-" * 80)
print("Matrix A (GPU):")
print(a_gpu.get())

print("-" * 80)
print("Matrix B (GPU):")
print(b_gpu.get())

print("-" * 80)
print("Matrix C (GPU):")
print(c_gpu.get())

print("-" * 80)
print("CPU-GPU DIFFERENCE:")
print(c_cpu - c_gpu.get())

# 判断两个矩阵在给定的宽容度内是否相接近
is_cloase = np.allclose(c_cpu, c_gpu.get())
print(is_cloase)