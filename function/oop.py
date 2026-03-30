class bim:
    Name= "ram"
    age= 20
    def bim1(self):
        print(f"my name is {self.Name} and my age is {self.age}")
b=bim()  #object creation
b.bim1()  


# class bim2:
#     def __init__(self,name,age):  
#         self.name=name
#         self.age=age
# a1=bim2("shyam", 25) 
# print(a1,name)
# print(a1.age)


class animal:
    def __init__(self,name):
        self.name=name
    def info(self):
        print("animal name ",self.name)
class dog(animal):
    def sound(self):
        print(self.name,"barks")
d=dog("tommy")
d.info()
d.sound()


add= lambda a,b: a+b
r=add(10,20)
print(r)

print((lambda a,b: a*b)(10,20))   # lambda in one line


def bim1(a,b):
    r=lambda a,b: a+b
    return r(a,b)
print(bim1(10,20))



# single inheritance
class parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class employee(parent):
    def show(self):
        print(self.name,"is an employe")
        print(self.age,"age is ",self.age)
em =employee("ram", 20)
print("name is ",em.name)
em.show()        
    