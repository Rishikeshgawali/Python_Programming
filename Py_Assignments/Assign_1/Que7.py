#Write a program which accept number from user and check weather that number is positive or negative or zero 


def ChkDiv(No):
    if (No % 5 == 0):
        return  True
    else:
       return  False


def main():
    print("Inside stater")
    print("Enter a Number :") 
    x = int(input())
    
    Ans = ChkDiv(x)
    if(Ans == True):
        print(x," is divisible by 5")
    else:
        print(x," is not divisible by 5")

if __name__ == "__main__":
    main()

'''
Output : 

Inside stater
Enter a Number :
10
10  is divisible by 5
---------------------------
Inside stater
Enter a Number :
12
12  is not divisible by 5
'''