numbers = [10, 20, 4, 45, 99, 99, 45]
unique_numbers = set(numbers)
if len(unique_numbers) < 3:
    print("Not enough unique numbers to find the third largest.")
else:
    sorted_numbers = sorted(unique_numbers, reverse=True)
    third_largest = sorted_numbers[2]
    print("Third largest number:", third_largest)
