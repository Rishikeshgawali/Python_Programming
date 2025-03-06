'''
Write a program which accept N numbers from user and store it into List.Return addition of all prime numbers from that List. Main python file accepts N numbers
from user and pass number to ChkPrime() function which is a part of our user defined module named as MarvellousNum. Name of the function from main python file
should be ListPrime()
'''

import copy
def ChkPrime(Arr):
    NewArr = copy.deepcopy(Arr)
    i=0
    Sum = 0
    for i in range(0,len(Arr),1):
        for j in range(2,((Arr[i]//2)+1),1):
            if((Arr[i] % j) == 0):
                NewArr.remove(Arr[i])
                break
    print("Prime Numbers are : ",NewArr)
    for Num in NewArr:
        Sum = Sum + Num
    return Sum
    
