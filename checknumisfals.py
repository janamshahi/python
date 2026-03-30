def check_range(number, start, end):
    if start <= number <= end:
        return True
    else:
        return False
num = 10
print("Does the number fall within range:", check_range(num, 2, 20))
