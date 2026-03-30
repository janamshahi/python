# write a pandas program  to create a dataframe from a dictonary and display it

import pandas as pd
# Dictionary
data = {
    'Name': ['Ram', 'Shyam', 'Hari'],
    'Age': [20, 22, 19],
    'City': ['Kathmandu', 'Pokhara', 'Lalitpur']
}
# Create DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print(df)


# Write a panadas program to get the first three row of a given dataframe.

import pandas as pd

data = {
    'A': [10, 20, 30, 40, 50],
    'B': [5, 15, 25, 35, 45]
}

df = pd.DataFrame(data)

# First three rows
print(df.head(3))


# write a pandas program to convert pandas model series to python list.

import pandas as pd

# Create Series
series = pd.Series([1, 2, 3, 4, 5])

# Convert to list
my_list = series.tolist()

print(my_list)


# write a pandas program to compare the element yes of the two pandas series.

import pandas as pd

# Create two Series
s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([1, 0, 3, 5])

# Compare elements
comparison = s1 == s2

print(comparison)

