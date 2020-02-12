"""Consider below application which demonstrates types of Behaviours"""

print("---Bhushan Mahangare---")
print("Demonstration of Behaviours of Class")

class Demo :

    def __init__(self) :
        self.i = 0
        self.j = 0

    def fun(self) :
        print("Inside instance")

    @classmethod
    def gun(cls):
        print("Inside class method")

    @staticmethod
    def sun():
        print("Inside static")

#Create Object of Demo class
obj1 = Demo()
obj1.fun()

Demo.gun()
Demo.sun()

#Method Resolution Order (MRO) in Python
Demo.mro()