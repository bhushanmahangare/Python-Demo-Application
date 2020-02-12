"""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
4.  Write a program which accept one number form user and return addition of its factors.
    Input : 12  Output : 16 (1+2+3+4+6)
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"""
def fact(num = 5):
    factorial = 1
    sum
    for i in range(1, num + 1) :
        factorial = factorial*i;
    return factorial

if __name__ == '__main__':

    num = int(input("Enter the number"))
    factorial = fact(num)

    print("The factorial of", num, "is", factorial)