"""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
7.  Write a program which contains one function that accept one number from user and returns true if number is divisible
    by 5 otherwise return false.
    Input : 8   Output : False
    Input : 25  Output : True
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"""

import logging

def checkDivisbleBy5(no = 25) :
    logging.info('Inside the checkDivisbleBy5() functions Request Parameter %s' % (no))
    if(no % 5 == 0 ) :
        return True
    else :
        return False

if __name__ == '__main__':
    logging.basicConfig(filename='/tmp/python.log', level=logging.DEBUG) #initialize logging filename
    logging.info('Inside the Main() functions')

    ret = checkDivisbleBy5()
    print ("True or False",ret)

    no = float(input("Enter the number :"))
    ret = checkDivisbleBy5(no)
    print ("True or False", ret)