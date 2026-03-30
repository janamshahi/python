student = {
    "name": "Janam",
    "age": 21,
    "course": "BITM"
}
print("Keys:")
for key in student:
    print(key)
print("\nValues:")
for value in student.values():
    print(value)
print("\nKey-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)
