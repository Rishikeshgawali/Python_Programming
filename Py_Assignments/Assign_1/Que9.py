#Write a program which accept number from user first 10 even numbers on screen


def DisplayEven(No):
    for i in range(2,(2*No)+2,2):
        print(i,end=" ")

def main():
    print("Inside stater")
    print("Enter a Number :") 
    x = int(input())
    
    DisplayEven(x)


if __name__ == "__main__":
    main()

'''
Output : 

Inside stater
Enter a Number :
5
2 4 6 8 10
--------------------
Inside stater
Enter a Number :
10
2 4 6 8 10 12 14 16 18 20
'''