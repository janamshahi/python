number = {
    "a": 1,
    "b": 4,
    "c": 9,
}
result = 1
for value in number.values():
    result *= value
print("Multiplication of all items:", result)