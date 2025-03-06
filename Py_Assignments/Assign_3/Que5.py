'''
Write a program which accept N numbers from user and store it into List.Return addition of all prime numbers from that List. Main python file accepts N numbers
from user and pass number to ChkPrime() function which is a part of our user defined module named as MarvellousNum. Name of the function from main python file
should be ListPrime()
'''
import MarvellousNum as MN

def main():
    Arr = list()

    print("Enter the size of List : ")
    size = int(input())
    print("Enter the Numbers : ")
    for i in range(0,size,1):
        i = int(input())
        Arr.append(i)
    print("Elements are : ",Arr)

    Ret = MN.ChkPrime(Arr)
    print("Addition of Prime Numbers : ",Ret)

if __name__ == "__main__":
    main()

'''
Output : 

Enter the size of List :
11
Enter the Numbers :
13
5
45
7
4
56
10
34
2
5
8
Elements are :  [13, 5, 45, 7, 4, 56, 10, 34, 2, 5, 8]
Prime Numbers are :  [13, 5, 7, 2, 5]
Addition of Prime Numbers : 32
'''