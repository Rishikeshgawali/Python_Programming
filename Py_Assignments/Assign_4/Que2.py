'''
Write a program which contains one lambda function which accepts 2 parameter and return its Multiplication
'''

'''
def Power(No1,No2):
    Ans = No1*No2
    return Ans
'''

Multiply = lambda No1,No2 : No1*No2

def main():
    print("Enter First Number : ")
    x = int(input())
    print("Enter Second Number : ")
    y = int(input())

    Ret = Multiply(x,y)
    print("Multipication of {0} and {1} is {2}".format(x,y,Ret))

if __name__ == "__main__":
    main()

'''
Output : 

Enter First Number :
12
Enter Second Number :
5
Multipication of 12 and 5 is 60
'''