import numpy as np

# Create a 2d array from a list of lists
list2 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
arr2d = np.array(list2)
print(arr2d)

# Create a float 2d array
arr2d_f = np.array(list2, dtype='float')
print(arr2d_f)

# Convert to 'int' datatype
print(arr2d_f.astype('int'))
