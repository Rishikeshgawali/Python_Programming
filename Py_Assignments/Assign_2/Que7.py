'''
 Write python program which accept one number and display below Pattern
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''

def Display(No):
    i = 0
    for i in range(0, No, 1):
        for j in range(1,No+1,1):
            print(j, end=" ")
        print()


def main():

    print("Enter a Number :")
    x = int(input())

    Display(x)

if __name__ == "__main__":
    main()

'''
Output : 

Enter a Number :
5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''