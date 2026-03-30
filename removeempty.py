data = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d',)]
result = [t for t in data if t]
print("List after removing empty tuples:")
print(result)
