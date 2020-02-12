"""Object Oriented Application"""

print("Application program which demonstrates Object Oriented in Python . Bank example")

class Bank:

    ROI = 10.3

    def __init__( self , custname , value ):
        self.name = custname
        self.amount = value

    def Deposit( self, value ):
        self.amount = self.amount + value

    def Withdraw( self , value ):
        self.amount = self.amount - value

    @classmethod
    def DisplayROI( cls ):
        print( cls.ROI )

    @staticmethod
    def BankInfo():
        print(" It is nationalised bank of India ")
        print("Location in Pune ")

def main():

    obj1 = Bank("Ajay",2000)
    print(obj1.name)
    print(obj1.amount)

    obj2 = Bank("Nitin",5000)
    print(obj2.name)
    print(obj2.amount)

    obj1.Deposit(500)
    obj2.Deposit(500)

    print(obj1.amount)
    print(obj2.amount)

    obj1.Withdraw(200)
    obj2.Withdraw(300)

    print(obj1.amount)
    print(obj2.amount)

    Bank.DisplayROI()
    Bank.BankInfo()

if __name__ == '__main__':
    main()