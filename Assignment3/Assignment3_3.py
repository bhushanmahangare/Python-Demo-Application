"""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    3.Write a program which accept N numbers from user and store it into List. Return Minimum
    number from that List.
    Input : Number of elements : 4
    Input Elements : 13 5 4 7
    Output : 5
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"""

def accpetData() :
    arr = []
    num = int(input("Enter no of element you want ?"))
    for i in range(0,num) :
        no = int(input("Num "))
        arr.append(no)
    return arr

def findMin(arr) :
    min = arr[0]
    for i in range(1,len(arr)) :
        if min > arr[i] :
            min = arr[i]
    return  min

def main() :

    arr = accpetData()
    minNo = findMin(arr)

    print("Minimum Number is " , minNo)

if __name__ == "__main__" :
    main()