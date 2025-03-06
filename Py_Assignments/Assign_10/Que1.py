import os
from sys import *

def Directory_Find(Dir,Ext):
    for Foldername,subfolder,filename in os.walk(Dir):
        print("Folder name is : ",Foldername)
        for fname in filename:
            if fname.endswith(Ext):
                print(fname)

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

    Output = Directory_Find(argv[1],argv[2])


if __name__ == "__main__":
    main()


