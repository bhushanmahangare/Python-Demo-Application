"""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
3.  Write a program which accept one number from user and return its factorial.
    Input   :   5   Output  :   120
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"""

import logging

def fact(num = 5):
    logging.info('Inside the fact() function Request Parameter %s ' % num)
    factorial = 1
    for i in range(1, num + 1) :
        factorial = factorial*i;
    return factorial

if __name__ == '__main__':
    logging.basicConfig(filename='/tmp/python.log', level=logging.DEBUG) #initialize logging filename
    logging.info('Inside the Main() function')

    num = int(input("Enter the number"))
    factorial = fact(num)

    print("The factorial of", num, "is", factorial)
    logging.info('The Factorial of %s is %s ' % (num,factorial))