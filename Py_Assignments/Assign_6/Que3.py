
class Numbers:


    def __init__(self,value):
        self.Value = value

    def ChkPrime(self):
        for i in range(2,(self.Value),1):
            if((self.Value) % i == 0):
                return True

    def ChkPerfect(self):
        Sum = 0
        for i in range(2,(self.Value),1):
            if((self.Value) % i == 0):
                Sum = Sum+i
        if(self.Value == Sum+1):
            return True
    def Factors(self):
        result = []
        for i in range(2, (self.Value), 1):
            if ((self.Value) % i == 0):
                result.append(i)
        return result

    def SumFactors(self):
        Sum = 0
        for i in range(2, (self.Value), 1):
            if ((self.Value) % i == 0):
                Sum = Sum + i
        return Sum


def main():

    print("Enter a Number : ")
    x = int(input())
    obj1 = Numbers(x)
    Ans = obj1.ChkPrime()
    if(Ans == True):
        print("Number is Not Prime")
    else:
        print("Number is Prime")

    Ans = obj1.ChkPerfect()
    if (Ans == True):
        print("Number is Perfect")
    else:
        print("Number is Not Perfect")

    Result = obj1.Factors()
    print("Factors of Number are : ",Result)

    Ans = obj1.SumFactors()
    print("Sum of the Factors are : ",Ans)

if __name__ == "__main__":
    main()

'''
Output : 

Enter a Number :
6
Number is Not Prime
Number is Perfect
Factors of Number are :  [2, 3]
Sum of the Factors are :  5


'''
