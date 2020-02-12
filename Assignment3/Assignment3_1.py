"""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    1. Write a program which accept N numbers from user and store it into List. Return addition of all
    elements from that List.
    Input : Number of elements : 6
    Input Elements : 13 5 45 7 4 56
    Output : 130
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"""

def acceptDataFromUser() :

    arr = list()  # create object of list

    num = int(input("Enter how many elements you want : "))

    # Iterate the for loop to accept N numbers
    for i in range(0, num):
        # Accept individual element from user
        no = int(input("num : "))
        # Insert that element into List
        arr.append(no)
    return arr;

def sum(arr) :
    sum = 0
    for i in range(0,len(arr)):
        sum += arr[i];
    return sum;

def main() :

    arr =  acceptDataFromUser()
    print("Entered elements are", arr)

    total = sum(arr)
    print("Elements sum is", total)

if __name__ == '__main__' :
    main()