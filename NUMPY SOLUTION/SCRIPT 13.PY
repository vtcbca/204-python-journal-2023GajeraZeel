SCRIPT 13
#Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

import numpy as np

# create a 3x3 matrix with values ranging from 2 to 10
matrix = np.arange(2, 11).reshape((3, 3))

# print the matrix
print("Matrix:")
print(matrix)

# print the dimension and size of each element and the array in memory
print("Dimension of the matrix:", matrix.ndim)
print("Size of each element in the matrix:", matrix.itemsize)
print("Size of the matrix:", matrix.size)
print("Bytes occupied by the matrix:", matrix.nbytes)
