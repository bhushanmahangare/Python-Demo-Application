"""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    5.Write a program which accept N numbers from user and store it into List. Return addition of all
    prime numbers from that List. Main python file accepts N numbers from user and pass each
    number to ChkPrime() function which is part of our user defined module named as
    MarvellousNum. Name of the function from main python file should be ListPrime().
    Input : Number of elements : 11
    Input Elements : 13 5 45 7 4 56 10 34 2 5 8
    Output : 54 (13 + 5 + 7 + 2 + 5)
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"""

def accpetData() :
    arr = []
    num = int(input("Enter no of element you want ?"))
    for i in range(0,num) :
        no = int(input("Num "))
        arr.append(no)
    return arr

def checkPrime(arr) :
    primeNoArray = []
    for i in range(0,len(arr)) :
        #if ( arr[i] % i == 0 )  :
        if ( arr[i] % i) == 0 :
            primeNoArray.append(arr[i])
    return  primeNoArray

def main() :

    arr = accpetData()
    primeNoArray = checkPrime(arr)

    print("Prime number array is " , primeNoArray )

if __name__ == "__main__" :
    main()