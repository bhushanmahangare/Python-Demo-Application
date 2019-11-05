"""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
9.  Write a program which display first 10 even numbers on screen.
    Output : 2 4 6 8 10 12 14 16 18 20
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"""

import logging

if __name__ == '__main__':
    logging.basicConfig(filename='/tmp/python.log', level=logging.DEBUG) #initialize logging filename
    logging.info('Inside the Main() function')

    for num in range(1,20 + 1):
        if num % 2 == 0:
            print(num)