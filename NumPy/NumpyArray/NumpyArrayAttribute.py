import numpy as np
import random

np.random.seed(0)
x1 = np.random.randint(10, size=6) # One-dimensional array
x2 = np.random.randint(10, size=(3, 4)) # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))

print(x1)
print(x2)
print(x3)

for i in range(5):
    #np.random.seed(0)
    print(random.randint(1, 1000))

print("x3 ndim: ", x3.ndim) # ndim (the number of dimensions)
print("x3 shape:", x3.shape) # shape (the size of each dimension)
print("x3 size: ", x3.size) # size (the total size of the array)
print("x3 dtype:", x3.dtype) # data type of the array
print("x3 itemsize:", x3.itemsize, "bytes") # size (in bytes) of each array element
print("x3 nbytes:", x3.nbytes, "bytes")


