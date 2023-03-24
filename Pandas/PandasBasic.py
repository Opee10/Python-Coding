import pandas as pd

data = pd.Series(['opee', 'ajam', 'shaf', 'megh'])
data1 = pd.Series([2, 4, 6, 8])

print(data)

print(data.values)
print(data1.index)
print(data[2])
print(data1[1:3])

var = pd.Series([0.78, 0.88, 0.97, 0.99], index= ['Index1', 'Index2', 'Index3', 'Index4'])
print(var) #acessing full series
print(var[2]) #acessing index 2 or element 3
print(var.index[2]) #Checking index 2 or 3rd element Index name
print(var['Index2']) #Acessing second elements index value

