import numpy as np
op = np.zeros(10, dtype=np.int64)
print(op)
op = np.ones(10, dtype=np.float32)
print(op)

#op = np.ones((3,4), dtype=np.float32)
p = np.ones((3, 4), dtype=np.int64)
print(p)

k = np.full((3, 4), 2.1416)
print(k)

op = np.arange(0,20,2, dtype=np.int32)
print(op)

op = np.linspace(0, 1, 6)
print(op)

op = np.random.random((3, 3))
print(op)

op = np.random.normal(0, 1, (3, 3))
print(op)

op = np.random.randint(0, 10, (3, 3))
print(op)

op = np.eye(5)
print(op)

# with mean 0 and standard deviation 1
op = np.random.normal(0, 1, (3, 3))
print(op)

op = np.empty(5)
print (op)
