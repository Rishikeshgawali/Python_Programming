import os
from sys import *

def File_Write(F_Name1,F_Name2):
    if(os.path.exists(F_Name1) and os.path.exists(F_Name2)):
        fd1 = open(F_Name1,'r')
        Data1 = fd1.read()

        fd2 = open(F_Name2,'r')
        Data2 = fd2.read()

        if(Data1 == Data2):
            print("Both files having Same data")
        else:
            print("Files are not same")
    else:
        print("One or both the files are not exists")

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

    File_Write(argv[1],argv[2])


if __name__ == "__main__":
    main()