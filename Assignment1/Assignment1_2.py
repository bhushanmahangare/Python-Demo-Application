"""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
 2. Write a program which contains one function named as ChkNum() which accept one
    parameter as number. If number is even then it should display Even number otherwise
    display Odd number on console.
    Input : 11  Output : Odd Number
    Input : 8   Output : Even Number
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"""

import logging

def ChkNum(no = 17):
    logging.info('Inside the ChkNum() functions Request Parameter %s' % (no))
    if(no % 2 == 0 ) :
        print("Even Number")
        logging.info('Even Number')
    else :
        print("Odd Number")
        logging.info('Odd Number')

if __name__ == '__main__':
    logging.basicConfig(filename='/tmp/python.log', level=logging.DEBUG) #initialize logging filename
    logging.info('Inside the Main() functions')
    #print ("Enter the number ")
    #no = input();
    #ChkNum(no)
    ChkNum(11)
    ChkNum(8)
    ChkNum()