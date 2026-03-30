def find_max(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
num1 = 10
num2 = 20
num = 30
result = find_max(num1, num2, num)
print("the maximum number is:", result)



def find_max(a, b, c):
    return max(a, b, c)

print("The maximum number is:", find_max(10, 25, 15))
