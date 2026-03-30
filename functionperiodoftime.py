import time
import math
def print_square_root(number):
    print(math.sqrt(number))
numbers = [16, 100, 25100]
delay =2
print("Square root after specific milliseconds:")
for num in numbers:
    time.sleep(delay)  
    print(math.sqrt(num))
