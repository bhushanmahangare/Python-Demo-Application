""" Consider below application which demonstrates types of characteristics """

print("---Bhushan Mahangare---")
print("Demonstration of characteristics of Class")

class Demo :
    x = 10

    def __init__(self , no1 , no2 ) :
        self.i = no1
        self.j = no2

#Create object of Demo class
obj1 = Demo( 10 , 20 )
obj2 = Demo( 11 , 21 )

print(obj1.i)
print(obj1.j)

print(obj2.i)
print(obj2.j)
print(obj2.x)

print(Demo.x)