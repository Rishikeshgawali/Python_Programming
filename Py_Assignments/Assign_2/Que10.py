'''
 Write python program which accept one number from user and return Addition of no.of digits in it.

'''

def Display(No):
    iCnt = 0
    Sum = 0
    while(No!=0):
        Digit = No%10
        Sum = Sum+Digit
        No = No//10
        
    return Sum

def main():

    print("Enter a Number :")
    x = int(input())

    Ans = Display(x)
    print("Addition of Digits of {0} is {1}".format(x,Ans))
    

if __name__ == "__main__":
    main()

'''
Output : 

Enter a Number :
123456
Addition of Digits of 123456 is 21
'''