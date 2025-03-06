'''
Write a program which accept N numbers from user and store it into List.Return Minimum number elements from that List.
'''
def Minimum(Arr):
    i=0
    Min = Arr[0]
    for i in range(0,len(Arr),1):
        if(Arr[i]<Min):
            Min = Arr[i]
    return Min


def main():
    Arr = list()
    print("Enter a Size for the List : ")
    size = int(input())
    print("Enter the Values : ")
    for no in range(0,size,1):
        no = int(input())
        Arr.append(no)
    print(Arr)

    Ret = Minimum(Arr)
    print("Minimum Number is : ",Ret)

if __name__ == "__main__":
    main()



'''
Output : 

Enter a Size for the List :
5
Enter the Values :
12
3
45
69
2
[12, 3, 45, 69, 2]
Minimum Number is :  2
'''