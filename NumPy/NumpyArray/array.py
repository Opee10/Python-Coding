import numpy as np
print(np.__version__)

op = np.array([44,33,22,11])
print(op)


op = np.array([44.4,33,22.3,11])
print(op)
#creating array from python list
print(np.array([1,2,3,4,5,6,7,8]))

#upcasting array from int to float
print(np.array([2.2, 4, 5.2, 8]))

#Creating an int array and converting it into a float array
arr_int = np.array([1, 2, 3])
arr_float32 = arr_int.astype(np.float32)
print("Original array:", arr_int)
print("Converted array:", arr_float32)


#Creating an int array and converting it into string array
arr_int = np.array([1, 2, 3])
arr_str = arr_int.astype(np.str_)
print("Original array:", arr_int)
print("Converted array:", arr_str)


import numpy as np

# Create an array of floating-point numbers
arr_float = np.array([9.2, 8.5, 7.7])

# Convert the array to an integer array
arr_int64 = arr_float.astype(np.int64)

# Print the original and converted arrays
print("Original array:", arr_float)
print("Converted array:", arr_int64)