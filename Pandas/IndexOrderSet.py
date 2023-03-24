import pandas as pd

#Indexing
ind = pd.Index([2, 3, 5, 7, 11])
print(ind[1])
print(ind[::2])
print(ind.size, ind.shape, ind.ndim, ind.dtype)

#OrderSet
var1 = pd.Index([1,9,3,8])
var2 = pd.Index([3,8,7,4])

print(var1.intersection(var2))
print(var1.union(var2))
print(var1.symmetric_difference(var2))

