#Write a program which contain 1 funtion named as Add() which accept 2 paremeter as number from user and return Addition of 2 numbers


def Add(No1,No2):

    Ans = No1 + No2
    return Ans


def main():
    print("Inside stater")
    print("Enter First Number : ")
    x = int(input())
    print("Enter Second Number : ")
    y = int(input())

    Ans = Add(x,y)

    print("Addition of 2 numbers is :",Ans)

if __name__ == "__main__":
    main()

'''
Output : 

Inside stater
Enter First Number :
10
Enter Second Number :
11
Addition of 2 numbers is : 21

'''