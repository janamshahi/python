def bim():
    print("hello bim")   #print statement
bim()  # called  function
    
    

def bim1(a,b):
    print(f"total sum is = {a+b}")   #print statement:
bim1(10,20)        
        

def bim2(a,b=10):
    print(f"sum ={a+b}")
bim2(12,8)
bim2(12)


def bim3(y):
    for x in y:
        print(x)
a=[1,2,3,4,5]

bim3(a)


def bim4(a,b):
    return a+b
b=bim4(10,20)
print(b)


def bim5(a,b):
    sum=a+b
    sub=a-b
    return sum,sub
a,b=bim5(10,20)
print(f"sum is = {a} and sub is = {b}")


def bim6(a):
    if a%2==0:
        return "even"
    else:
        return "odd"
print(bim6(10))


def bim7(a, b):
    if a>b:
        return a
    else:
        return b
print(bim7(10, 25))


def bim8(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print(bim8(10, 50, 30))


def bim9(a): # function 
    num=[]   # empty list
    for n in a:   # loop
        if n%2==0:  # condition
             num.append(n)   # add even number to list
    return num                   # return even number list
print(bim9([1, 2, 3, 4, 5]))       # call function with list of number





