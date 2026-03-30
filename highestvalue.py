numbers = {
    "a": 45,
    "b": 12,
    "c": 78,
    "d": 34,
    "e": 90,
    "f": 67
}
sorted_items = sorted(numbers.items(), key=lambda item: item[1], reverse=True)
top_three = sorted_items[:3]
print("Top 3 highest values with keys:")
for key, value in top_three:
    print(key, ":", value)
