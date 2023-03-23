import numpy as np

n = np.array([[1, 2, 3,8],
             [4, 5, 6,5],
             [7, 8, 9,3]])
sub_arr = n[:2, :2]
print(sub_arr)
sub_arr[0, 0] = 21
print(n)