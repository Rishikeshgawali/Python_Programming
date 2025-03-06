#Write a program which accept name from user and display length of its name.


def Display(str):
    print("Your entered String is : ",str)
    print("Length of entered String is : ",len(str))

def main():
    print("Inside stater")
    print("Enter a String :")
    x = input()
    
    Display(x)


if __name__ == "__main__":
    main()

'''
Output : 

Inside stater
Enter a String :
abc
Your entered String is :  abc
Length of entered String is :  3
'''