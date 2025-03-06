'''
Write a program which accept N numbers from user and store it into List.
Accept one another number from user and return frequency of that number from List.
'''

def Frequency(Arr,x):
    i = 0
    iCnt = 0
    for i in range(0,len(Arr),1):
        if(x == Arr[i]):
            iCnt = iCnt+1
    return iCnt


def main():
    Arr = list()

    print("Enter the size of List : ")
    size = int(input())
    print("Enter the Numbers : ")
    for i in range(0,size,1):
        i = int(input())
        Arr.append(i)
    print(Arr)

    print("Enter a Number to Count the frequency : ")
    x = int(input())

    Ret = Frequency(Arr,x)
    print("Frequency of {0} is {1}".format(x,Ret))

if __name__ == "__main__":
    main()

'''
Output : 

Enter the size of List :
5
Enter the Numbers :
1
2
3
2
2
[1, 2, 3, 2, 2]
Enter a Number to Count the frequency :
2
Frequency of 2 is 3
'''