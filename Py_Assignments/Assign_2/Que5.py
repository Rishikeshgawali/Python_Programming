'''
 Write python program which accept one number and return addition of its Factors
'''

def ChkPrime(No):

    for i in range(2,(No//2)+1,1):
        if(No % i == 0):
            return True

def main():

    print("Enter a Number :")
    x = int(input())

    Ans = ChkPrime(x)
    if(Ans == True):
        print(x,"is Prime Number")
    else:
        print(x, "is not Prime Number")

if __name__ == "__main__":
    main()

'''
Output : 

Enter a Number :
12
12 is Prime Number
---------------------------
Enter a Number :
5
5 is not Prime Number
'''