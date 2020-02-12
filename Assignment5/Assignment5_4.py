"""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    Write a recursive program which accept number from user and return summation of its digits
    Input   :   879
    Output  :   24
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"""

def additionRecursive(num) :
    sum = 0
    no = num
    while num :
        sum += num % 10
        num //= 10
    print("Input {} digits summation is {} ".format(no,sum))

def sum_digits1(n) :
    sum = 0
    num = n

    while num :
        num , remainder = divmod( num , 10)
        sum += remainder

    print("Input {} digits summation is {} ".format(n,sum))


def sum_digits2(n) :
    sum = 0
    num = n

    while n != 0 :
        m = n % 10
        n = n / 10
        sum = int( sum + m )

    print("Input {} digits summation is {} ".format(num, sum))


def sum_digits3(number) :
    if number == 0 :
        return 0
    else :
        return ( number % 10 ) + sum_digits3( number // 10 )


def main() :
    print("Inside the main() function")

    additionRecursive(879)
    sum_digits1(879)
    sum_digits2(879)
    print(sum_digits3(879))

    num = 879
    print(sum([int(k) for k in str(num)]))

    print(sum(list(map(int,input("Enter your number ")))))


if __name__ == '__main__' :
    main()