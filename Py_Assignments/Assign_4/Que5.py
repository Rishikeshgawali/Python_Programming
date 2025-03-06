'''
Write a program which contains filter(),map(),reduce() in it. Python application which contains one list of numbers.List contains the numbers which are accepted
from user.
Filter should filter out all prime numbers .
Map Function will multiply each number by 2.
Reduce will return maximum number from that number.
'''

def ChkPrime(No):
    Flag = True
    for i in range(2,(No//2)+1,1):

        if(No % i == 0):
            Flag = False
            break
    return Flag


def Multiply(No):
    return No*2

def Maximum(A,B):
    if(A>=B):
        return A
    else:
        return B

def filterX(Arr,Helper_Function):
    Result = []
    for No in Arr:
        if(Helper_Function(No)):
            Result.append(No)
    return Result

def mapX(Arr,Helper_Function):
    Result = []
    for No in Arr:
        value = Helper_Function(No)
        Result.append(value)
    return Result

def reduceX(Arr,Helper_Function):

    Value = 0
    for No in Arr:
        Ans = Helper_Function(Ans,No)
    return Ans

def main():
    Data = list()
    print("Enter the number of elements that you want to store : ")
    x = int(input())

    print("Please Enter Elements : ")

    for i in range(0,x,1):
        i = int(input())
        Data.append(i)

    print("Enetered Elements are : ",Data)
    filter_Data = filterX(Data,ChkPrime)
    print("Filtered Data is :  ",filter_Data)

    map_Data = mapX(filter_Data,Multiply)
    print("Mapped Data is :  ",map_Data)

    Output = reduceX(map_Data,Maximum)
    print("Final Output After Reducing is :  ",Output)


if __name__ == "__main__":
    main()

'''
Output :

Enter the number of elements that you want to store :
5
Please Enter Elements :
89
20
101
7
9
Enetered Elements are :  [89, 20, 101, 7, 9]
Filtered Data is :   [89, 101, 7]
Mapped Data is :   [178, 202, 14]
Final Output After Reducing is :   202
'''