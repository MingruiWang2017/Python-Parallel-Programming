import pycuda.gpuarray as gpuarray
import numpy as np
from pycuda.reduction import ReductionKernel

import pycuda.autoinit

vector_length = 100
input_vector_a = gpuarray.arange(vector_length, dtype=np.int)
input_vector_b = gpuarray.arange(vector_length, dtype=np.int)
dot_product = ReductionKernel(np.int,
                              arguments="int *x, int *y",
                              map_expr="x[i] * y[i]",
                              reduce_expr="a+b",
                              neutral="0")

dot_product = dot_product(input_vector_a, input_vector_b).get()

print("INPUT VECTOR A:")
print(input_vector_a)

print("INPUT VECTOR B:")
print(input_vector_b)

print("RESULT DOT PRODUCT OF A * B:")
print(dot_product)