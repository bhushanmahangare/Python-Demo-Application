"""
__init__ :

"__init__" is a reserved method in python classes.
It is known as a constructor in object oriented concepts.
This method called when an object is created from the class and it allow the class to
initialise the attributes of a class.
In python for every instance method there is one implicit parameter as self.

self :

self represents the instance of the class. By using the "self" keyword we can access
the attributes and methods of the class in python """

print("---Bhushan Mahangare---")
print("Demonstration of Class")

class Demo :

    def __init__( self , value1 , value2 ):
        print("Inside init method")
        self.i = value1
        self.j = value2

    def fun(self) :
        print("Inside the fun")
        print( self.i , self.j )

    def add(self) :
        print( self.i + self.j )

# Create Object of Demo class
obj1 = Demo( 10 , 20 )

# Call the method fun
obj1.fun()

# Create Object of Demo class
obj2 = Demo( 50 , 60 )

# Call the method fun
obj2.fun()

# Call method add to perform addition of characteristics
obj1.add()
obj2.add()


