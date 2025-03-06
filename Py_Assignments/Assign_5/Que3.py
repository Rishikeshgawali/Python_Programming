
class Arithmetic:
    def __init__(self):
        No1 = 0
        No2 = 0

    def Accept(self):
        print("Enter First Number : ")
        self.No1 = int(input())
        print("Enter Second Number : ")
        self.No2 = int(input())

    def Addition(self):
        Ans = self.No1 + self.No2
        return Ans

    def Subtraction(self):
        Ans = self.No1 - self.No2
        return Ans

    def Multiplication(self):
        Ans = self.No1 * self.No2
        return Ans

    def Division(self):
        Ans = self.No1 / self.No2
        return Ans

def main():

    obj1 = Arithmetic()

    obj1.Accept()
    Add_Value = obj1.Addition()
    print("Addition of {0} and {1} is {2}".format(obj1.No1,obj1.No2,Add_Value))

    Sub_Value = obj1.Subtraction()
    print("Subtraction of {0} and {1} is {2}".format(obj1.No1,obj1.No2,Sub_Value))

    Mul_Value = obj1.Multiplication()
    print("Multiplication of {0} and {1} is {2}".format(obj1.No1,obj1.No2,Mul_Value))
    
    Div_Value = obj1.Division()
    print("Division of {0} and {1} is {2}".format(obj1.No1,obj1.No2,Div_Value))

if __name__ == "__main__":
    main()

'''

Enter First Number :
10
Enter Second Number :
5
Addition of 10 and 5 is 15
Subtraction of 10 and 5 is 5
Multiplication of 10 and 5 is 50
Division of 10 and 5 is 2.0

'''