'''Write a program which contain 1 funtion named as ChkNum() which accept one paremeter as number.
   If nunber is even then it should display "Even Number" otherwise display "Odd Number" on console.
'''

def ChkNum(No):
    if(No%2 == 0):
        return 1


def main():
    print("Inside stater")
    print("Enter a Number : ")
    x = int(input())
    Ans = ChkNum(x)

    if(Ans == 1):
        print("Number is Even")
    else:
        print("Number is Odd")

if __name__ == "__main__":
    main()

'''
Output : 

Inside stater
Enter a Number :
56
Number is Even
-----------------------
Inside stater
Enter a Number :
55
Number is Odd

'''