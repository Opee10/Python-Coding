import numpy as np

import random
"""
n = np.array([[9, 3, 6],
             [4, 8, 12],
             [9, 16, 2]])
print(n)
print(n[0:1, 0:1])

n = np.array([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])
print(n)
print(n[2:1 , 1:])

x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7],
 [6, 5, 4]])
# vertically stack the arrays
print(np.vstack([x, grid]))

j = np.array([1,2,3])
k = np.array([7,9,6])

print(np.concatenate([j,k]))

z = [99, 99, 99]
print(np.concatenate([j, k, z]))
"""

var = np.random.randint(0, 10, (2, 2))
for i in np.nditer(var):
 print(i)
