"""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
1.  Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
    for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
    parameters as number and perform the operation. Write on python program which call all the
    functions from Arithmetic module by accepting the parameters from user.
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"""
from arithmetic import *
import logging

if __name__ == '__main__':
    logging.basicConfig(filename='/tmp/python.log', level=logging.DEBUG) #initialize logging filename
    logging.info('Inside the Main() function')

    print ("Enter the 1st number ")
    no1 = int(input())
    print ("Enter the 2nd number")
    no2 = int(input())

    ret = add(no1,no2)
    print ('Addition is ',ret)
    logging.info('Addition is %s' % ret)

    ret = sub(no1,no2)
    print ('Subtraction is ', ret)
    logging.info('Subtraction is %s' % ret)

    ret = div(no1,no2)
    print ('Division is ', ret)
    logging.info('Division is %s' % ret)

    ret = mul(no2,no2)
    print ('Multiplication is %s ' % ret)
    logging.info('Multiplication is %s' % ret)