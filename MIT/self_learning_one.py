import numpy as np
import math

# What I have learned so far: 
# 1. Trogonometric functions: np.sin(), np.cos(), np.tan()
# 2. Exponenet function: np.exp()
# 3. Logarithmic function: np,log(), np.log10() 
# 4. Operation of array and matrix: +, -, *, /, **, 1/array (inverse)
# 5. Matrix muliplication: @ or np.matmul() 
# 6. Transpose of Matrix: np.transpose() or array.T 
# 7. Minimun and Maximun value of Matrix: np.min(), np.max()
# 8. Function to generate random numbers: np.random.rand(), np.random.randint()
# 9. Mean and Standard Deviation of Matrix: np.mean(), np.std()
# 10. Reshape of array: array.reshape((rows, columns))
# 11. np.arange() function to create an array with evenly spaced values within a given interval. 
# 12. np.linspace() function to create an array with evenly spaced values over a specified range.
# 13. np.zeros(), np.ones(), np.eye() function to create an array filled with zeros, ones, and identitly martrix. 
# 14. Convert array to numpy array: np.array() 
# 15. Access elements from array using np.arange(start, stop, steps), then 
# this will the indexes, and based on this you could access. 
# 16. Access elements from array using index and slicing.
# 17. Access elements from matrix using [row, column] or [row][column]
# 18. Access elements from matrix using slicing [row1:row2, column1:column2]
# 19. Access elements from matrix based on their values using boolean values.
# 20. Modify elements in the matrix using slicing.



arr_str = ['Hello', 'World', 'Python', 'is', 'great']
print ("Usual Array: ", arr_str)

# def print_array(arr): 
#     for i in range(len(arr)): 
#         print(arr[i]) 

# print_array(arr_str)

# To convert the array to NumPy array, you can use the following code: 

arr_str_numpy = np.array(arr_str) 
print("Numpy Array: ", arr_str_numpy)

print('Type of two arrays:', type(arr_str), type(arr_str_numpy)) 

#  Matrix of Numbers 

matrix = np.array([[1,2], [4,5], [6,7]])
print( matrix)

# matrix = np.array([[1,2,1],[4,5,9],[1,8,9]])
# print(matrix) 


# np.arange() function creates an array with evenly spaced values within a given interval. 

# create an array with evenly spaced values from 0 to 10 with a step of 2. 10 does not get included in the array, while 0 is included. 
np_arange_array = np.arange(0, 10.1 , 2)  
print('Array created using np.arange():', np_arange_array) 

#  There is another way to create an array with evenly spaced values using np.arange() function. 
#  Which is to specify the number of elementes in the array. 
#  For example: 

np_arange_array2 = np.arange(start= 0, stop= 10, step =2)
print('Array created using np.arrange() with specified number of elements:', np_arange_array2) 


#  To create an array with evenly spaced values usnig np.linspace() fnuction, 
#  you can specify the start and end values, as well as the number of elements you want in the array. 
# For example: 
# In this example, np.linspace(0, 1, num=10) generates an array of 10 
# numbers between 0 and 1, including both endpoints./
# The start value is 0 by default, and you can change it by specifying the start point. 
# The default number of elements is 50, but you can change it by specifying the num point. 



linspace_array = np.linspace(0,1, num=10)
print('Array created using np.linspace(): ', linspace_array) 
# Another example: 
linspace_array2 = np.linspace(start=0, stop=2, num = 10)
print('Array created using np.linspace() with specified start and stop values:', linspace_array2)

#  To understand how values are spaced in the array: 
#  (stop - start)/ (num - 1) 
#  For example: 5 - 0 / 10 - 1 = 0.5555

print("*" * 30)

linspace_array3 = np.linspace(start= 1, stop = 3, num = 10) 
print('Array created using np.linspace with specified start and stop values:', linspace_array3) 

# np.linspace() is a function in NumPy that generates an array of evenly spaced values over a specified range. 


# There is a funciton called np.zeros() which creates an array filled with zeros. 

print("#" * 30)
zeros_array = np.zeros([3,5])
print('Array created using np.zeros():', zeros_array)

#  The argument [3,5] specifies the shape of the array, which in this case is a 3 rows and 5 columns. 


#  There is another funciton called np.ones() which creates an array filled with ones. 
# example: 

ones_array = np.ones([3,3]) 
print('Array created using np.ones():', ones_array)

# The output will be a 3x3 array filled with ones. 


#  There is another function called np.eye() which creates an identity martrix. 

identity_matrix = np.eye(4)
print('Array created using np.eye():', identity_matrix)


# Here is would like to make a quick review about everything I learned so far 

# convert array to numpy array
arr_to_numpy_array = np.arange(start=1, stop=5, step=1) 
numbers_between_1_and_2 = np.linspace(start=1, stop=2, num=100)  # stop - start / (num - 1) 
matrix_with_zeros = np.zeros([3,3])
matrix_with_ones = np.ones([2,2])
identity_matrix = np.eye(3,3)
 
print(arr_to_numpy_array) 
print(numbers_between_1_and_2) 
print(matrix_with_ones) 
print(matrix_with_zeros)
print(identity_matrix) 

print("#" * 100) 
print("#" * 100) 
print("#" * 100) 

# reshape array 

array = np.arange(0,9)
print(array)

print(len(array))

reshape_array = array.reshape((3,3))
print(reshape_array)


print ("#" * 100)
print ("#" * 100)
print ("#" * 100)

# Trigonomatric function  

print('Sin function', np.sin(0))
print('Cos function', np.cos(math.pi))
print('Cos function', np.cos(3.141592653589793))
print('Tan function', np.tan(0))
print('Tan function', np.tan(math.pi))
print('Tan function', np.tan(3.141592653589793))

print("PI", math.pi)

# exponenet function e 

print('Exponenet function', np.exp(4))


print('*' * 100)

array_of_numbers = np.array(np.arange(0,5))
print(array_of_numbers)

print('Cos of array_of_numbers', np.cos(array_of_numbers))
print('Sin of array_of_numbers', np.sin(array_of_numbers))
print('Tan of array_of_numbers', np.tan(array_of_numbers))
print('Expo of array_of_numbers', np.exp(array_of_numbers))
print('Log of array_of_numbers', np.log(array_of_numbers))


# Log with base 10 

print('Log with base 10', np.log10(1000))


print("*" * 100) 

print("Operation of Matrix") 

arr_5 = np.arange(1,6)
arr_6 = np.arange(3,8) 
print(arr_5)
print(arr_6)


print('Addition', arr_5 + arr_6)
print('Subtraction', arr_5 - arr_6)
print('Multiplcation', arr_5 * arr_6)
print('Divition', arr_6 / arr_5) 
print('Inverse', 1/ arr_5)
print('Inverse', 1/ arr_6)
print('Powers', arr_5 ** arr_6)


print("*" * 100) 
# Operation of Matrix 
matrix_1 = np.arange(1,10).reshape(3,3)
matrix_2 = np.arange(10, 19).reshape(3,3)

print(matrix_1)
print(matrix_2)

print("Addition", matrix_1 + matrix_2)
print("Multip", matrix_1 * matrix_2)
print('Subtraction', matrix_1 - matrix_2)
print('Powers', matrix_1 ** 2)
print('Powers', matrix_1 ** matrix_2)
print('Division', matrix_2 / matrix_2)


# linear algebra 

print("Matrix Multi", matrix_1 @ matrix_2)


# Transpose Matrix 
print("Transpose Matrix", np.transpose(matrix_1))
# Another way to transpose. 
print(matrix_2.T)



print('Minimun Value of Matrix', np.min(matrix_1))
print('Maximun Value of Matrix', np.max(matrix_1))



print('Function to generate random numbers')
# Function to generte random numbers 

# np.random.rand(d0, d1, ..., dn), and the numbers represent the shape of the array are randomly between 0 and 1. 
# [0,1) 
# np.random.rand(rows, columns)
random_array = np.random.rand(3,3) 
print('Random Array', random_array) 
random_array2 = np.random.rand(4,2)
print('Random Array2', random_array2)

# Also, you can use the same function (np.random.rand()) to generate an array with one dim. 
random_number = np.random.rand(2)
print('Random Number', random_number)

# Mean of the martix and standard deviation. 
print('Mean of the martix', np.mean(random_array))
print('Standard Deviation of the martix', np.std(random_array))

# Another function to generate random numbers is np.random.randit(low, high, sizq)

print('Random Integer Numbers', np.random.randint(1,3,5))

# The difference between np.random.rand() and np.random.randint() 
# is that the first one generate random numbers between 0 and 1, 
# While the second one generate random integer numbers between low and high, and the size of the array. 

# This is a way to generete one random integer number between low and high. 
print('Random Integer Numbers', np.random.randint(1,10,1))


print("*" * 100) 

# Let generate an array with 2 random values. 
rand_arr = np.random.randn(10)
print(rand_arr)

# np.random.randn(number_of_entries)


# If you have an array with 10 entires and would you like to access the specific entry,
# you can do it like this: 
print(rand_arr[1:4])
print(rand_arr[1])

print("*" * 100)

# New topics 
# Now, how to access multiple non-consecutive entries using np.arange


access_element_array = np.arange(0, 10, 2)
print(access_element_array)

print('Index of values to access: ', np.arange(3,10,3))
print(access_element_array[np.arange(2,6,2)])


# Boolean Values: 

print("*" * 100)
arr_bool = np.linspace(start=0, stop=10, num = 10) 
print(arr_bool > 3)

# this a way to access elements based on their values. 
print(arr_bool[arr_bool>0])
print(arr_bool[arr_bool>3])



# Let generate a matrix with 10 entries: 
ten_elements_matrix = np.random.randn(5,5)

print("Matrix with 10 elements", ten_elements_matrix)
print("*" * 100)
print(ten_elements_matrix[ten_elements_matrix>0])

# Moreover, we could access specific rows, for example: 

print("*"* 100)
print('Print the first row of the matrix', ten_elements_matrix[0])
print('Print the second row of the matrix', ten_elements_matrix[1])
print('Print the third row of the matrix', ten_elements_matrix[2])
print('Print the four row of the matrix', ten_elements_matrix[3])
print('Print the five row of the matrix', ten_elements_matrix[4])

# We can also access specific element in the matrix using the following code. 

print("Specific element in the Matrix", ten_elements_matrix[0][0])
# or 
print('Specific element in the Matrix', ten_elements_matrix[0,0])
# [row, column]

# accessing first two rows with second and third column 
print("print specific elements", ten_elements_matrix[0:2,1:3])


# Let's have a matrix that has a 3x3 with integers values to test on it. 

print("/" * 100)
matrix_3 = np.arange(-1, 8).reshape(3,3).T
print(matrix_3)
print('/' * 100)
print("Print the modified matrix",matrix_3[0:1, 2:3])

# Now, I got how [0:1, 1:2] works. 
# The first part [0:1] means the first row, and the second column. 

# [row1: row2, column1: column2] 
# which means select rows from row1 to row2-1, and same for columns. 

print("/" * 100)
print("*" * 100)

matrix_4 = np.arange(1, 10).reshape(3,3)
print('Matrix 4', matrix_4)

print('First two rowas and first two columns', matrix_4[0:2, 0:2])

# Change some values in the matrix. 
matrix_4[0:1] = [0,1,1]
matrix_4[1:2] = [0,1,0]
matrix_4[2:3] = [0,0,0]
print('Modified Matrix 4', matrix_4)


print("*" * 100)
print("/" * 100)

matrix_5 = np.arange(start = 1, stop=10, step=1).reshape(3,3)
print(matrix_5) 

identity_matrix_of_three = np.eye(3) 

print("Print the transpose of the matrix: ", matrix_5.T)
print("The first element in row one and column one", matrix_5[0,0])
print("The last element of the matrix", matrix_5[2,2])
print("The frist two rows", matrix_5[0:2, 0:2])
print("Multiply identity matrix with matrix A * I = A: ", matrix_5 @ identity_matrix_of_three)
print("A matrix with it is transposed A * A^T = ", matrix_5 * matrix_5.T )


print("************ Review of random functions in numpy *********")

matrix_6 = np.random.randn(4).reshape(2,2)
print(matrix_6)

