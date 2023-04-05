SCRIPT 12
#Write a NumPy program to convert a list of numeric value into a one-dimensional NumPy array. Print original list and array with its dimension , size and byte occupied in memory


import numpy as np

# create the original list of numeric values
original_list = [12.23, 13.32, 100, 36.32]

# convert the list to a one-dimensional NumPy array
numpy_array = np.array(original_list)

# print the original list and NumPy array
print("Original List:", original_list)
print("One-dimensional NumPy array:", numpy_array)

# print the dimension, size and byte occupied in memory of the NumPy array
print("Dimension of the NumPy array:", numpy_array.ndim)
print("Size of the NumPy array:", numpy_array.size)
print("Bytes occupied by the NumPy array:", numpy_array.nbytes)