import numpy as np
array = np.array([1, 2, 3, 4, 5])
print(array)


b = np.array([1,2,3,4,])
print(b)
c = np.array([1,2,3,4,5], dtype=np.float64)
print(c)

my_list = ['apple', 'banana', 'cherry','gapple']
print(my_list[1::4])

arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[1] = 42
print(arr)
print(x)

