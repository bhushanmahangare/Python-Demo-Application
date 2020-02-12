"""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    Write a recursive program which accept number from user and return its factorial
    Input   :   5
    Output  :   120
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"""

def recurion_factorial(n) :
    if n == 1 :
        return n
    else :
        return n * recurion_factorial( n - 1 )

#Take input from the user

num = int(input("Enter the number "))

#check is the number is negative

if num < 0 :
    print("Sorry,factorial does not exits for negative numbers")
elif num == 0 :
    print("The factorial of 0 is 1")
else :
    print("The factorial of ",num,"is",recurion_factorial(num))