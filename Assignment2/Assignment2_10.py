"""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
10. Write a program which accept number from user and return addition of digits in that number.
    Input : 5187934 Output : 37
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"""

def getSum(num):
    sum = 0
    while (num != 0):
        sum = sum + int(num % 10)
        num = int(num / 10)
    return sum

num = 5187934
print(getSum(num))