# create a numpy array of 10 ramdom indeger

import numpy  as np
arr = np.random.randint(1,100,size=10)
print("random array:",arr)


# write a program to check a prime or not.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = 29
print(f"{num} is prime:", is_prime(num))


# wite program using function to find sum of of any number passed to the functon

def sum_of_digit(n):
    total = 0
    while n > 0:
        total += n % 10
        n //=10
    return total
num = 1234
print("sum of digit:",sum_of_digit(num))