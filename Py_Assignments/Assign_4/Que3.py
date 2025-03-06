'''
Write a program which contains filter(),map(),reduce() in it. Python application which contains one list of numbers.List contains the numbers which are accepted
from user.
Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90.
Map Function will increase each number by 10.
Reduce will return product of all that numbers.
'''

ChkNumber = lambda No : (No >=70 and No<=90)

Increment = lambda No:(No + 10)

Product = lambda A,B:(A*B)

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
    Ans = 1
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
    filter_Data = filterX(Data,ChkNumber)
    print("Filtered Data is :  ",filter_Data)

    map_Data = mapX(filter_Data,Increment)
    print("Mapped Data is :  ",map_Data)

    Output = reduceX(map_Data,Product)
    print("Final Output After Reducing is :  ",Output)

if __name__ == "__main__":
    main()

'''
Output :

Enter the number of elements that you want to store :
5
Please Enter Elements :
10
25
75
80
90
Enetered Elements are :  [10, 25, 75, 80, 90]
Filtered Data is :   [75, 80, 90]
Mapped Data is :   [85, 90, 100]
Final Output After Reducing is :   765000
'''