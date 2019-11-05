"""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
2.  Write a program which accept one number and display below pattern.
    Input   5
    Output :
    1   2   3   4   5
    1   2   3   4   5
    1   2   3   4   5
    1   2   3   4   5
    1   2   3   4   5
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"""

import logging

if __name__ == '__main__':
    logging.basicConfig(filename='/tmp/python.log', level=logging.DEBUG) #initialize logging filename
    logging.info('Inside the Main() function')

    for i in range(1,6) :

        for j in range(1,6):

            print ("",j,end=" ")

        print("\n")