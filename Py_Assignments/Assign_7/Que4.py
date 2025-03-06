import time
import threading
import os

def Small(arr):
    i = 0
    for i in range(len(arr)):
        if(ord(arr[i]) >=97 and ord(arr[i])<=122):          #we have used ord() function to convert a character to an integer (ASCII value).
                                                           # This function returns the Unicode code point of that character.
            print("ID is {} Small letter is : {}".format(os.getpid(),arr[i]))


def Capital(arr):
    for i in range(len(arr)):
        if(ord(arr[i]) >=65 and ord(arr[i])<=90):
            print("ID is {} and Capital letter is : {}".format(os.getpid(),arr[i]))


def Digit(arr):
    i = 0
    for i in range(len(arr)):
        if(ord(arr[i]) >=48 and ord(arr[i])<=57):
            print("ID is {} and Digit is : {}".format(os.getpid(),arr[i]))


def main():
    str = input("Enter a String : ")
    Arr = list(str)

    print(str)
    print(Arr)

    small = threading.Thread(target = Small,args = (Arr,))
    capital = threading.Thread(target = Capital,args = (Arr,))
    digit = threading.Thread(target = Digit,args = (Arr,))


    small.start()
    capital.start()
    digit.start()

    small.join()
    capital.join()
    digit.join()

    print("Exit from main")

if __name__ == "__main__":

    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Execution time is : ",end_time - start_time)
