#Write a program which accept number from user and check weather that number is positive or negative or zero 


def Display(No):
    for i in range(0,No,1):
        print("*",end=" ")

def main():
    print("Inside stater")
    print("Enter a Number :") 
    x = int(input())
    
    Display(x)


if __name__ == "__main__":
    main()

'''
Output : 

Inside stater
Enter a Number :
5
* * * * *
'''