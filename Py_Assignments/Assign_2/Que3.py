'''
 Write python program which accept one number and return its factorial
'''

def Factorial(No):
    i=0
    Ans = 1
    for i in range(1,No+1,1):
        Ans = Ans*i
    return Ans

def main():

    print("Enter a Number :")
    x = input()

    Ans = Factorial(int(x))
    print("Factorial of {0} is : {1} ".format(x,Ans))


if __name__ == "__main__":
    main()

'''
Output : 

Enter a Number :
5
Factorial of 5 is : 120
'''