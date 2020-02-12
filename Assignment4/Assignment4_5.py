"""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    Write a program which contains filter(), map() and reduce() in it. Python application which
    contains one list of numbers. List contains the numbers which are accepted from user. Filter
    should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
    return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).

    Input List          =   [2, 70 , 11, 10, 17, 23, 31, 77]
    List after filter   =   [2, 11, 17, 23, 31]
    List after map      =   [4, 22, 34, 46, 62]
    Output of reduce    =   62
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"""
from functools import reduce

def acceptData() :
    print("Inside acceptData() function ")
    iArr = []
    iNo = int(input("Enter how many elements you want ?"))
    for i in range(iNo) :
        iArr.append(int(input(" Num ")))
    return iArr

def checkPrime(iNum) :
    if iNum > 1 :

        for i in range(2,iNum) :
            if ( iNum % i ) == 0 :
                break
            else :
                return iNum

def main() :
    print("Inside main() function")

    #iArr = acceptData()
    iArr =  [2, 70 , 11, 10, 17, 23, 31, 77]
    print("Input List ",iArr)

    iPrimeArr = list(filter( checkPrime , iArr  ) )
    print("Data after filter ", iPrimeArr)

    iMulArr = list(map( lambda no : ( no * 2 )  , iPrimeArr))
    print("Data after map by multiply each number by 2 ", iMulArr)

    iMaxNo = reduce( max , iMulArr )
    print("Maximum number ",iMaxNo)


if __name__ == "__main__":
    main()