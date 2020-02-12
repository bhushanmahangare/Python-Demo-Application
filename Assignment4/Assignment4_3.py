"""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    3.Write a program which contains filter(), map() and reduce() in it. Python application which contains one list
    of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which
    greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10.
    Reduce will return product of all that numbers.
    Input List         = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
    List after filter  = [76, 89, 86, 90, 70]
    List after map     = [86, 99, 96, 100, 80]
    Output of reduce   = 6538752000

    def reduce(function, iterable, initializer=None):
        it = iter(iterable)
        if initializer is None:
            value = next(it)
        else:
            value = initializer
        for element in it:
            value = function(value, element)
        return value
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"""
from functools import reduce

def acceptData() :
    num = int(input("Enter the how many element you want ? "))
    arr = []
    for i in range(0,num) :
        #no = int(input("Num "))
        arr.append(int(input("Num ")))
    return arr

def filterDataFun(no) :
    if( no >= 70 and no <= 90) :
        return no

def add(no) :
    return  no + 10

def mul(a,b) :
    return a * b

def main() :

    arr = acceptData()
    print("Input List ",arr)

    filterData = list(filter(filterDataFun,arr))
    print("Input List after filter by greater than or equal to 70 and less than or equal to 90 ", filterData)

    addData = list(map(add,filterData))
    print("Input List after increase each number by 10 ",addData)

    productNo = reduce(mul,addData)
    print("Input List product of all numbers ",productNo)

    # Demonstration of Filter, Map reduce using lambda functions
    arr = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

    arr =  list( filter( lambda no : ( no >= 70 and no <= 90 ) , arr  ) )
    print("Data after filter using lambda", arr)

    arr = list( map( lambda no : no + 10 , arr ) )
    print("Data after map using lambda", arr)

    prodNo = reduce( lambda a,b : a * b , arr )
    print("Product of numbers using lambda",prodNo)

if __name__ == "__main__" :
    main()