
import os
from sys import *

def File_Write(F_Name1,FName2):
    if(os.path.exists(F_Name1)):
        print(F_Name1+"Named File is already exist")

    else:
        fd1 = open(FName2, 'r')
        Data = fd1.read()

        fd2 = open(F_Name1, 'w')
        fd2.write(Data)


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