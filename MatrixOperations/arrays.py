import numpy as np
# Creating ndarray
    # 1.simple array
arr = np.array([4,5,6,7,8.3])
print(arr,arr.shape,arr.dtype)
    # 2.empty array
emp = np.empty([2,5])
print(emp)
    # 3.array of zeros
zero = np.zeros([5,5])
print(zero)
    # 4.array of ones
one = np.ones([2,2])
print(one)
# Creating an array of other arrays -
    # 1.stack vertically
array1 = np.array([46,29])
array2 = np.array([27,33])
array3 = np.vstack((array1,array2))
print(array3)
    # 2.stack horizontally
array1 = np.array([2.7,2.2])
array2 = np.array([3.0,1.2])
array3 = np.hstack((array1,array2))
print(array3)
