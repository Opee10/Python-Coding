import numpy as np

n = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(n[1:5:2])
print(n[3:8:3])
print(n[4:8:2])
print(n[-5::2])

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-2])