my_dict={
    "math": 90,
    "english": 85,
    "science": 95,
    "history": 80
}
max_key = max(my_dict, key=my_dict.get)
print("key with the maximum value:", max_key)
print("maximum value:", my_dict[max_key])
