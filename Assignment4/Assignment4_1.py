"""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    1.Write a program which contains one lambda function which accepts one parameter and return power of two.
    Input : 4   Output : 16
    Input : 6   Output : 64
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"""
def main() :

    no = int(input("Enter the element : "))
    fp = lambda no : no * no
    powerOfTwo = fp(no)
    print("Power of number ",powerOfTwo)

if __name__ == "__main__" :
    main()