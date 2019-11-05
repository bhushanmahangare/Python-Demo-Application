"""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
6.  Write a program which accept number from user and check whether that number is positive or negative or zero.
    Input : 11  Output : Positive Number
    Input : -8  Output : Negative Number
    Input : 0   Output : Zero
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"""

import logging

def checkNumber():
    logging.info('Inside the checkNumber() function')

    num = int(input("Enter a number : "))
    if num > 0 :
        print ("Positive Number")
    elif num == 0 :
        print ("zero")
    else :
        print ("Negative Number")

if __name__ == '__main__':
    logging.basicConfig(filename='/tmp/python.log', level=logging.DEBUG) #initialize logging filename
    logging.info('Inside the Main() function')
    checkNumber();