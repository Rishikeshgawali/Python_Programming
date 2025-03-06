import os
from sys import *

def File_Write(F_Name1,str_in):
    i =0
    if(os.path.exists(F_Name1)):
        fd = open(F_Name1,'r')
        for line in fd:
            for word in line.split():
                if(word == str_in):
                    i = i+1
                    print(word)
        return i
    else:
        print("File not exists")

def main():

    print("Application name : ", argv[0])

    if (len(argv) != 3):
        print("Error : Invalid Number of Arguments")
        exit()

    if ((argv[1] == "-h") or (argv[1] == "-H")):
        print("This script is used log record of running processes")
        exit()

    if ((argv[1] == "-u") or (argv[1] == "-U")):
        print("usage : ApplicationName Create_File_Name Read_File_Name")
        exit()

    Output = File_Write(argv[1],argv[2])
    print("Count of given string is : ",Output)
    print("It was counted when space separates the exact string")

if __name__ == "__main__":
    main()


'''

command------>python Que5.py Que5.py def

Application name :  Que5.py
def
def
Count of given string is :  2
It was counted when space separates the exact string

'''