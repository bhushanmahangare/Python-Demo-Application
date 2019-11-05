"""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
4.  Write a program which display 5 times Marvellous on screen.
    Output :
    Marvellous
    Marvellous
    Marvellous
    Marvellous
    Marvellous
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"""

import logging

def printFun(str = "Marvellous" , itertaionCount = 5):
    logging.info('Inside the printFun() function Request Parameter %s   %s ' % (str , itertaionCount))
    for x in range(itertaionCount) :
        print (str)

if __name__ == '__main__':
    logging.basicConfig(filename='/tmp/python.log', level=logging.DEBUG) #initialize logging filename
    logging.info('Inside the Main() function')
    printFun()
    printFun("Data",7)