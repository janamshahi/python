import math
def calculate_factorial(n):
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."
    else:
        return math.factorial(n)
num = int(input("Enter a non-negative integer: "))
print(f"The factorial of {num} is {calculate_factorial(num)}")



def calculate_factorial_iterative(n):
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
num = int(input("Enter a non-negative integer: "))
print(f"The factorial of {num} is {calculate_factorial_iterative(num)}")
