import sys
print("---BHUSHAN MAHANGER---")
print("Demonstration of Scope of Recursion")

print("Maximum number of recursive call are {} in python".format(sys.getrecursionlimit()))

#Changing recursion limit
sys.setrecursionlimit(1500)

print("Maximum number of recursive call are {} in python".format(sys.getrecursionlimit()))

#Recursive function which goes into infinite recurive calls

def fun() :
    print("Inside fun")
    fun()
#fun()


#Recursive function which performs recurive calls 10 times
i = 1
def gun() :
    global  i
    if( i <= 10 ) :
        print(i)
        i+=1
        gun()

gun()#call the gun function


def fact(no) :
    if( no == 0 ) :
        return 1;
    return no * fact( no - 1 )

value = 5
ret = fact( 5 )
print("Factorial of {} is {} ".format(value,ret))