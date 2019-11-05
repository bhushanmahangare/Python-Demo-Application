"""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
5.  Write a program which display 10 to 1 on screen.
    Output : 10 9 8 7 6 5 4 3 2 1
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"""

import logging

def printNum(itertaionCount = 5) :
    logging.info('Inside the printFun() function Request Parameter %s ' % itertaionCount)
    #for i in reversed(range(itertaionCount)) :
     #   print (i)

    for i in range(itertaionCount, 0, -1) :
        print (i)

if __name__ == '__main__' :
    logging.basicConfig(filename='/tmp/python.log', level=logging.DEBUG) #initialize logging filename
    logging.info('Inside the Main() function')
    printNum(10)