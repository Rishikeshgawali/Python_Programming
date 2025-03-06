'''
 Write python program which accept one number and display below pattern
'''

def Display(No):
    i=0
    for i in range(0,No,1):
        for i in range(0, No, 1):
            print("*",end=" ")
        print()

def main():

    print("Enter a Number :")
    x = input()

    Display(int(x))

if __name__ == "__main__":
    main()

'''
Output : 

Enter a Number :
5
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''