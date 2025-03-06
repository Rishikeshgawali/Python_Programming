#Write a program which accept number from user and check weather that number is positive or negative or zero 


def ChkNum(No):
    if (No > 0):
        print("Positive Number")
    elif (No < 0):
        print("Negative Number")
    else:
        print("Zero")


def main():
    print("Inside stater")
    print("Enter a Number :") 
    x = int(input())
    
    ChkNum(x)

if __name__ == "__main__":
    main()

'''
Output : 

Inside stater
Enter a Number :
11
Positive Number
----------------------
Inside stater
Enter a Number :
-10
Negative Number
----------------------
Inside stater
Enter a Number :
0
Zero
'''