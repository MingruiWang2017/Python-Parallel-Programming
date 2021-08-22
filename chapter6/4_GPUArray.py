import numpy as np
import pycuda.gpuarray as gpuarray
import pycuda.driver as cuda
import pycuda.autoinit

a_gpu = gpuarray.to_gpu(np.random.randn(4,4).astype(np.float32))
a_double = (2 * a_gpu).get()

print(a_double)
print(a_gpu)