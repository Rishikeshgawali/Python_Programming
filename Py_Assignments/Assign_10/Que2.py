import os
from sys import *

def Directory_Find(Dir,Ext1,Ext2):
    flag = os.path.isabs(Dir)
    if flag == False:
        path = os.path.abspath(Dir)

    for Foldername,subfolder,filename in os.walk(path):
        for fname in filename:
            if fname.endswith(Ext1):
                os.rename(os.path.join(Foldername, fname), os.path.join(Foldername, fname.replace(Ext1, Ext2)))

                '''
                    error---base = os.path.splitext(fname)[0]
                    os.rename(fname, base + Ext2)
                '''


def main():
    print("This Appication is for change the extension of file")
    print("Application name : ", argv[0])

    if (len(argv) != 4):
        print("Error : Invalid Number of Arguments")
        exit()

    if ((argv[1] == "-h") or (argv[1] == "-H")):
        print("This script is used log record of running processes")
        exit()

    if ((argv[1] == "-u") or (argv[1] == "-U")):
        print("usage : ApplicationName Directory_Name .extension1 .extension2")
        print(".extension1 = extenstion of existing_File .extension2 = extension we have to change")

        exit()

    Directory_Find(argv[1],argv[2],argv[3])


if __name__ == "__main__":
    main()


