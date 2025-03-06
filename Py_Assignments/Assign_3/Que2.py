'''
Write a program which accept N numbers from user and store it into List.Return Maximum number elements from that List
'''
def Maximum(Arr):
    i=0
    Max = 0
    for i in range(0,len(Arr),1):
        if(Arr[i]>Max):
            Max = Arr[i]
    return Max


def main():
    Arr = list()
    print("Enter a Size for the List : ")
    size = int(input())
    print("Enter the Values : ")
    for no in range(0,size,1):
        no = int(input())
        Arr.append(no)
    print(Arr)

    Ret = Maximum(Arr)
    print("Maximum Number is : ",Ret)

if __name__ == "__main__":
    main()



'''
Output : 

Enter a Size for the List :
5
Enter the Values :
12
3
52
8
6
[12, 3, 52, 8, 6]
Maximum is :  52
'''