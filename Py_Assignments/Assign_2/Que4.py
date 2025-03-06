'''
 Write python program which accept one number and return addition of its Factors
'''

def AddFactors(No):
    Ans=0
    i=0
    print("Factors are : ")
    for i in range(1,(No//2)+1,1):
        if(No % i == 0):

            print(i,end=" ")
            Ans = Ans+i
    print()
    return Ans

def main():

    print("Enter a Number :")
    x = int(input())

    Ans = AddFactors(x)
    print("Addition of factors of {0} is : {1} ".format(x,Ans))


if __name__ == "__main__":
    main()

'''
Output : 

Enter a Number :
12
Factors are :
1 2 3 4 6
Addition of factors of 12 is : 16
'''