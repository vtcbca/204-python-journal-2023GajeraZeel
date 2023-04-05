SCRIPT 14
#Write a NumPy program to get the values and indices of the elements that are bigger than 10 in a given array.

import numpy as np

# create a 1D array with some values
arr = np.array([8, 12, 5, 16, 10, 3, 9, 20, 25])

# get the values and indices of the elements that are bigger than 10
values = arr[arr > 10]
indices = np.where(arr > 10)[0]

# print the values and indices
print("Values bigger than 10:", values)
print("Indices of values bigger than 10:", indices)