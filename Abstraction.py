#Abstraction
from abc import ABC, abstractmethod
class BankApp(ABC):

    def database(self):
        print("Connected to database")

    @abstractmethod
    def security(self):
        pass
    
    @abstractmethod
    def display (self):
        pass

class MobileApp(BankApp):

    def mobile_login(self):
        print("login into mobile")

    def security(self):
        print("mobile security")

    def display (self):
        print("Display")

#Custom Exception
class CustomError(Exception):
    pass

class InventoryError(Exception):
    pass

def check_order(q):
    stock = 100
    if q > stock:
        raise InventoryError ("Insufficient stock")
    else:
        print("stock available")

try:
    quantity = int(input("Enter the required quantity"))
    check_order(quantity)
except InventoryError as ie:
    print(ie)

#Build Custom Exception Classes
class MyIndexError(Exception):

    def __init__(self, length):
        self.message = f"Yor are the only allowed to guess between {-1 * length} and {length * -1}"

x = [1,2,3,4]

try:
    user_input = int(input("Predict position:"))
    print(x[user_input])

except Exception as e:
    if e.__class__.__name__ == "Index Error":
        print(f"You are only allowed to guess between {-1 * len(x)} and {len(x)-1}")

    elif e.__class__.__name__ : "Value Error"
    print("You are only allowed integers")

 
 
#closures in python
#closures
def outer(a):

    def adder(b):

        return a+b
    return adder
    
    val = outer(10)

    print(val(5))
    print(val(10))
    