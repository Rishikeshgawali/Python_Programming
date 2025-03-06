
class BankAccount:

    ROI = 10.5

    def __init__(self,name,amount):
        self.Name = name
        self.Amount = amount

    def Display(self):
        print("Name of Account Holder is : ",self.Name)
        print("Amount of Account_Holder: ",self.Amount)

    def Deposite(self,Value):
        self.Amount = self.Amount + Value

    def Withdraw(self, Value):
        self.Amount = self.Amount - Value

    def Calculate_Interest(self):
        Interest = ((self.Amount * self.ROI)/100)
        return Interest


def main():

    obj1 = BankAccount("Abhishek",2000)
    obj1.Display()
    obj1.Deposite(500)
    obj1.Display()
    Interest = obj1.Calculate_Interest()
    print("Interest on {} is {}".format(obj1.Amount,Interest))

    obj1.Withdraw(300)
    obj1.Display()
    Interest = obj1.Calculate_Interest()
    print("Interst on Amount is : ",Interest)


if __name__ == "__main__":
    main()

'''

Name of Account Holder is :  Abhishek
Amount of Account_Holder:  2000
Name of Account Holder is :  Abhishek
Amount of Account_Holder:  2500
Interest on 2500 is 262.5
Name of Account Holder is :  Abhishek
Amount of Account_Holder:  2200
Interst on Amount is :  231.0

'''
