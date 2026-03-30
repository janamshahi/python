import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
reparted_arr = np.repeat(arr,3)
print("original_arr:", arr)
print("reparted_arr:", reparted_arr)



#write numpy program to repeat all the elements three time of given aray of strang

arr = np.random.rand(4,4)
print("original_arr:\n", arr)
arr[[0,-1]] = arr[[-1,0]]
print("array after swapping first and last row:\n", arr)

