"""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    2.Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.
    Input : Number of elements : 7
    Input Elements : 13 5 45 7 4 56 34
    Output : 56
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"""

def acceptData() :
    no = int(input("Enter no of element you want "))
    arr = [];
    for i in range(0, no) :
        num = int(input("Num "))
        arr.append(num)
    return arr

def findMax(arr) :

    max = arr[0]

    for i in range(1,len(arr)) :
        if arr[i] > max :
            max = arr[i]

    return max

def main() :

    arr = acceptData()
    maxNo = findMax(arr)
    print("Max Number is ",maxNo)

if __name__ == "__main__":
    main()