'''
Write a program which accept N numbers from user and store it into List.Return Addition of all elements from that List
'''
def Add(Arr):
    i=0
    Sum = 0
    for i in range(0,len(Arr),1):
        Sum = Sum + Arr[i]
    return Sum


def main():
    Arr = list()
    print("Enter a Size for the List : ")
    size = int(input())
    print("Enter the Values : ")
    for no in range(0,size,1):
        no = int(input())
        Arr.append(no)
    print(Arr)

    Ret = Add(Arr)
    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()



'''
Output : 

Enter a Size for the List :
3
Enter the Values :
1
2
3
[1, 2, 3]
Addition is :  6
'''