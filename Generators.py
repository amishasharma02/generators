class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update  

class MappingSubclass(Mapping):

    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)

#Generators
squares_generator = (i * i for i in range(5))

for i in squares_generator:
    print(i)

#function for creating topten squares using generators 
def topten():
    n = 1

    while n <= 10:
        sq = n*n
        yield sq
        n += 1

values = topten()

for i in values:
    print(i)


#Decorators
def decor(addition):
    def inner():
        result = addition()

        num3=int(input("Third number:"))
        result=result+num3
        return result
    return inner
@decor
def addition():
    num1=int(input("First number:"))
    num2=int(input("Second number:"))
    result = num1 + num2
    return result
addition=decor(addition)
print("Add:",addition())

#Multiple Decorators in one function
def decor1(func):
    def inner():
        return func()
    return inner

def decor2(func):
    def inner():
        return func().split()
    return inner

@decor1
@decor2
def get_name():
    name=input("Enter first name:")
    lastname=input("Enter last name:")
    full_name=name+" "+lastname
    return full_name

print(get_name())