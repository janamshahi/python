number = int(input("Enter number: "))

def multipy(number):
    for i in range(1,11):
        print(f"{number} * {i} = {number*i}")
multipy(number)
