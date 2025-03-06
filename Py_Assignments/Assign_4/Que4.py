'''
Write a program which contains filter(),map(),reduce() in it. Python application which contains one list of numbers.List contains the numbers which are accepted
from user.
Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90.
Map Function will increase each number by 10.
Reduce will return product of all that numbers.
'''

ChkEven = lambda No:(No %2 == 0)

Square = lambda No:(No * No)

Addition = lambda A,B : (A+B)


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
    Result = []
    Ans = 0
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
    filter_Data = filterX(Data,ChkEven)
    print("Filtered Data is :  ",filter_Data)

    map_Data = mapX(filter_Data,Square)
    print("Mapped Data is :  ",map_Data)

    Output = reduceX(map_Data,Addition)
    print("Final Output After Reducing is :  ",Output)

if __name__ == "__main__":
    main()

'''
Output :

Enter the number of elements that you want to store :
10
Please Enter Elements :
5
2
3
4
3
4
1
2
8
10
Enetered Elements are :  [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
Filtered Data is :   [2, 4, 4, 2, 8, 10]
Mapped Data is :   [4, 16, 16, 4, 64, 100]
Final Output After Reducing is :   204
'''