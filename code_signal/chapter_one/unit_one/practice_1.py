import numpy as np

# Create a Python list
py_list = [1, 2, 3, 4, 5]

# Convert list to a Numpy array
np_array = np.array(py_list)

print('Print the whole array: ',np_array) # Output: [1 2 3 4 5]

print('print the first element: ', np_array[0])

print('Use slicing the print the first two element: ', np_array[0:2])

matrix = np.array([[1,2,4], [4,5,4]])

print("Print the matrix: ", matrix)


print("Dimensions: ", matrix.ndim) # Dimensions:  2
print("Shape: ", matrix.shape)     # Shape:  (2, 3)
print("Size: ", matrix.size)       # Size: 6
print("Data Type: ", matrix.dtype) # Data Type:  int64

print('Indexed values: ', matrix[1,2])
print('Sliced Values: ', matrix[0:])



