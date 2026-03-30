dict1 ={
    "a": 10,
    "b": 20,
    "c": 30
}
dict2 = {
    "b": 10,
    "c": 25,
    "d": 40
}
result ={}
for key in dict1.keys() | dict2.keys():
    result[key] = dict1.get(key, 0) + dict2.get(key, 0)
print("Combined Dictionary:", result)
