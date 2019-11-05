import logging

def add(no1 = 10 , no2 = 2) :
    logging.info('Inside the add() function Request Parameter %s + %s ' % (no1,no2))
    return no1+no2

def sub(no1 = 10 , no2 = 2) :
    logging.info('Inside the sub() function Request Parameter %s - %s ' % (no1,no2))
    return no1-no2

def div(no1 = 10 , no2 = 2) :
    logging.info('Inside the div() function Request Parameter %s / %s ' % (no1,no2))
    return no1/no2

def mul(no1 = 10 , no2 = 2) :
    logging.info('Inside the mul() function Request Parameter %s * %s ' % (no1,no2))
    return no1*no2
