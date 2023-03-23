import numpy as np

p = np.array([5, 0, 3, 3, 7, 9])
print(p[0])
             #0   1  2  3 column
p = np.array([[3, 5, 2, 4],    #0th row
              [7, 6, 8, 80],   #1st row
              [1, 41, 11, 9]]) #2nd row
p[1,3] = 88
print(p)
p[1,1] = 9.222 #It wil be truncated!
print(p)
print(p[2,2])
print(p[2, -1])