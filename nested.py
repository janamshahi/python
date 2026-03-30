keys_list = ["a", "b", "c", "d"]
nested_dict = current = {}
for key in keys_list:
    current[key] = {}
    current = current[key]
print("Nested Dictionary:", nested_dict)
