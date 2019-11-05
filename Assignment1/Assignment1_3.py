"""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
3.  Write a program which contains one function named as Add() which accepts two numbers
    from user and return addition of that two numbers.
    Input : 11 5    Output : 16
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"""

import logging

def add(no1 = 11 , no2 = 5):
    logging.info('Inside the add() function Request Parameter %s + %s ' % (no1,no2))
    return no1 + no2

if __name__ == '__main__':
    logging.basicConfig(filename='/tmp/python.log', level=logging.DEBUG) #initialize logging filename
    logging.info('Inside the Main() function')
    print ("Enter the 1st number ")
    no1 = input()
    print ("Enter the 2nd number")
    no2 = input()

    sum = add(no1,no2)
    print('Addition is ',sum)
    logging.info('Addition is %s' % sum)

    sum = add()
    print('Addition is ', sum)
    logging.info('Addition is %s' % sum)

    sum = add(20)
    print('Addition is ', sum)
    logging.info('Addition is %s' % sum)
