"""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of
    numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which
    are even. Map function will calculate its square.Reduce will return addition of all that numbers
    Input List          =   [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
    List after filter   =   [2, 4, 4, 2, 8, 10]
    List after map      =   [4, 16, 16, 4, 64, 100]
    Output of reduce    =   204
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"""
from functools import reduce

def acceptData() :
    iNo = int(input("Enter the no element you want "))
    iArr = []
    for i in range(0,iNo) :
        #no = int(input())
        #iArr.append(no)
        iArr.append(int(input("Num ")))
    return iArr

def main() :
    print("In main() function")
    #iArrData = acceptData()
    iArrData = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
    print("Input List ",iArrData)

    evenArr = list( filter( lambda no :  ( no % 2 == 0 ), iArrData ) )
    print("Data after filter ", evenArr)

    calSeq = list( map( lambda no : ( no * no ) , evenArr) )
    print("Data after Map by calculate its square ", calSeq)

    iSum = reduce( lambda a , b : ( a + b ), calSeq )
    print("Data after addition of all that numbers ", iSum )

if __name__ == "__main__":
    main()