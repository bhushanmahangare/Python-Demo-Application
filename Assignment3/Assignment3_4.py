"""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    4.Write a program which accept N numbers from user and store it into List. Accept one another
    number from user and return frequency of that number from List.
    Input : Number of elements : 11
    Input Elements : 13 5 45 7 4 56 5 34 2 5 65
    Element to search : 5
    Output : 3
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"""
def accpetData() :
    arr = []
    num = int(input("Enter no of element you want ?"))
    for i in range(0,num) :
        no = int(input("Num "))
        arr.append(no)
    return arr

def findFrequencyNo(arr,searchNo) :
    searchNoCount = 0;
    for i in range(0,len(arr)) :
        if ( searchNo == arr[i] ) :
            searchNoCount += 1
    return  searchNoCount

def main() :

    arr = accpetData()

    searchNo = int(input("Element to search frequency : "))
    searchNoCount = findFrequencyNo(arr,searchNo)

    print("Frequency is " , searchNoCount )

if __name__ == "__main__" :
    main()