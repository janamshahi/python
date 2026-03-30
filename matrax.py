import numpy as np
matrax = np.arange(2,11).reshape(3,3)
print(matrax)


start_date = '2026-02-01'
end_date = '2026-02-28'
date_range = np.arange(np.datetime64(start_date), np.datetime64(end_date) + np.timedelta64(1, 'D'))
print(date_range)


arr = np.arange(1, 26).reshape(5,5)
print("original array:\n",arr)
row_index = [1, 3]
col_index =[0,2,4]
subarray = arr[np.ix_(row_index, col_index)]
print("subarray:\n",subarray)

#example 2
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("original array:\n", arr)
row_index = [0, 2]
col_index = [1, 2]
subarray = arr[np.ix_(row_index, col_index)]
print("subarray:\n", subarray)






