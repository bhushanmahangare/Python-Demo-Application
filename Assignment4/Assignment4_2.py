"""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    2.Write a program which contains one lambda function which accepts two parameters and return its multiplication.
    Input : 4   3   Output : 12
    Input : 6   3   Output : 18
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"""
def main() :
    no1 = int(input("Enter the element : "))
    no2 = int(input("Enter the element : "))

    fp = lambda no1 , no2 : no1 * no2

    powerOfTwo = fp(no1,no2)
    print("Multiplication of number ",powerOfTwo)

if __name__ == "__main__" :
    main()