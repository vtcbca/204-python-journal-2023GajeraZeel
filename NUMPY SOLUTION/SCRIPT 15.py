SCRIPT 15
#Write a NumPy program to create a new shape to an array without changing its data.

import numpy as np

# create a 3x2 array
arr = np.array([[1, 2], [3, 4], [5, 6]])

# print the original array
print("Original array:")
print(arr)

# reshape the array to a 2x3 shape
new_arr = arr.reshape((2, 3))

# print the new array
print("New array with shape 2x3:")
print(new_arr)