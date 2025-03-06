'''
Write a program which contains one lambda function which accepts one parameter and return power of two.
'''

'''
def Power(No):
    Ans = No*No
    return Ans
'''

Power = lambda No : No*No

def main():
    print("Enter a Number : ")
    x = int(input())

    Ret = Power(x)
    print("Power of {0} is {1}".format(x,Ret))

if __name__ == "__main__":
    main()

'''
Output : 

Enter a Number :
45
Power of 45 is 2025
'''