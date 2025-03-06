'''
 Write python program which accept one number from user and return no.of digits in it.

'''

def Display(No):
    iCnt = 0
    while(No!=0):
        No = No//10
        iCnt = iCnt+1
    return iCnt

def main():

    print("Enter a Number :")
    x = int(input())

    Ans = Display(x)
    print("{0} contains {1} digits".format(x,Ans))
    

if __name__ == "__main__":
    main()

'''
Output : 

Enter a Number :
456987
456987 contains 6 digits
'''