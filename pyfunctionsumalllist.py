def sum_list(number):
    total = 0
    for num in number:
        total += num
    return total
numbers = [10, 20, 30, 40, 50]
print("The sum of the list is:", sum_list(numbers))
