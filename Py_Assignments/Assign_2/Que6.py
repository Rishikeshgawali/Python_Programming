'''
 Write python program which accept one number and display below Pattern
* * * * *
* * * *
* * *
* *
*
'''

def Display(No):
    i = 0
    for i in range(0, No, 1):
        for j in range(No, i, -1):
            print("*", end=" ")
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
* * * * *
* * * *
* * *
* *
*
'''