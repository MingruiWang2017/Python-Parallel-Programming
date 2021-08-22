import numpy as np
import pycuda.gpuarray as gpuarray
from pycuda.curandom import rand as curand
from pycuda.elementwise import ElementwiseKernel
import numpy.linalg as la

import pycuda.autoinit
from pytools import linear_combination

input_vector_a = curand((50,))
input_vector_b = curand((50,))
mult_coefficient_a = 2
mult_coefficient_b = 5

linear_combination = ElementwiseKernel(
    "float a, float *x, float b, float *y, float *c",  # 参数
    "c[i] = a*x[i] + b*y[i]",  # 对参数执行的操作
    "linear_combination"  # 操作名称
)
linear_combination_result = gpuarray.empty_like(input_vector_a)
linear_combination(mult_coefficient_a, input_vector_a,
                   mult_coefficient_b, input_vector_b,
                   linear_combination_result)

print("INPUT VECTOR A:")
print(input_vector_a)

print("INPUT VECTOR B:")
print(input_vector_b)

print("RESULTING VECTOR C:")
print(linear_combination_result)

print("CHECKING THE RESULT EVALUATING THE DIFFERENCE VECTOR \
BETWEEN C AND THE LINEAR COMBINATION OF A AND B:")
print("C - (%sA + %sB) = " % (mult_coefficient_a, mult_coefficient_b))
print(linear_combination_result - (mult_coefficient_a * input_vector_a
                                   + mult_coefficient_b * input_vector_b))

# 计算C-(2A+5B)的二范数（即欧氏距离），判断其二范数是否小于0.00001
# https://www.cnblogs.com/shuaishuaidefeizhu/p/11395762.html
assert la.norm((linear_combination_result - 
                (mult_coefficient_a * input_vector_a + 
                mult_coefficient_b * input_vector_b)).get()) < 1e-5